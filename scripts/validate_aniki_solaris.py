#!/usr/bin/env python3
"""Validate the Aniki Solaris theme source and create a test .pthm archive.

This is a packaging smoke test, not a Windows/Playnite runtime test.
"""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile

try:
    import yaml
except ImportError:
    print("PyYAML is required: python -m pip install pyyaml", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Source"
SETTINGS = SOURCE / "AnikiThemeSettings.yaml"
PALETTE = SOURCE / "Themes Option" / "2.Interface" / "ThemeColors" / "44.Solaris.xaml"
OUTPUT = ROOT / "dist" / "Aniki-Solaris-test-build.pthm"

if not SOURCE.is_dir():
    raise SystemExit(f"Missing theme source directory: {SOURCE}")
if not SETTINGS.is_file():
    raise SystemExit(f"Missing settings file: {SETTINGS}")
if not PALETTE.is_file():
    raise SystemExit(f"Missing Solaris palette: {PALETTE}")

with SETTINGS.open("r", encoding="utf-8-sig") as stream:
    settings = yaml.safe_load(stream)

try:
    preset = settings["Presets"]["Interface"]["Presets"]["Solaris"]
except (TypeError, KeyError) as exc:
    raise SystemExit("Solaris preset is missing from AnikiThemeSettings.yaml") from exc

configured_files = preset.get("Files", [])
expected = "Themes Option\\2.Interface\\ThemeColors\\44.Solaris.xaml"
if expected not in configured_files:
    raise SystemExit(f"Solaris preset does not reference {expected}")

xaml_files = sorted(SOURCE.rglob("*.xaml"))
if not xaml_files:
    raise SystemExit("No XAML files found in Source")
for path in xaml_files:
    try:
        ET.parse(path)
    except ET.ParseError as exc:
        raise SystemExit(f"Malformed XML/XAML: {path.relative_to(ROOT)}: {exc}") from exc

# Package Source contents at archive root. Runtime loading still needs testing
# in Playnite on Windows.
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=7) as archive:
    for path in sorted(SOURCE.rglob("*")):
        if path.is_file():
            archive.write(path, path.relative_to(SOURCE).as_posix())

print(f"Validated settings and {len(xaml_files)} XAML files.")
print(f"Created {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size:,} bytes).")
