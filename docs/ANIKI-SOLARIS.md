# Aniki Solaris

This branch starts the Solaris-inspired visual adaptation while keeping Aniki ReMake as the source of truth for view models, commands, navigation, and Aniki Helper integration.

## Included in the current test build

- Adds Solaris Inspired as an Interface color preset.
- Retains Aniki's existing resource keys and changes the color palette toward deep blue-black surfaces, cool cyan focus accents, and high-contrast text.
- Adds a Windows GitHub Actions workflow that validates XAML/XML and settings YAML, then uploads a .pthm ZIP test artifact.

## Important scope note

This is the first source-level visual pass, not a complete port of Solaris's layouts, animations, media behavior, or screens. Those require comparing Solaris's actual release package with Aniki's XAML and then adapting each view while preserving its bindings and commands. The current workflow's package is a smoke-test archive; install and runtime behavior must still be verified in Playnite on Windows.

## Test

1. Open the Build Aniki Solaris test package workflow on the feature/aniki-solaris branch.
2. Download the Aniki-Solaris-test-build artifact.
3. Back up your existing Playnite profile before testing.
4. Install the .pthm only in a separate/test Playnite profile if Playnite accepts the package.
5. In Aniki ReMake theme settings, select Interface → Solaris Inspired.

If Playnite rejects the package, retain the validation output and use Aniki's normal source-to-theme packaging process to assemble the same Source contents. The archive is deliberately labeled a test build until runtime loading is confirmed.
