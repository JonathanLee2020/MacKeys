# How to Create a Release

This project uses GitHub Actions to automatically build and release the installer.

## Automatic Release (Recommended)

1. **Make your changes and commit them:**
   ```bash
   git add .
   git commit -m "Your changes"
   git push
   ```

2. **Create and push a version tag:**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

3. **GitHub Actions will automatically:**
   - ✅ Build the executable (`MacShortcuts.exe`)
   - ✅ Build the installer (`MacKeys-Setup-v1.0.0.exe`)
   - ✅ Create a GitHub Release
   - ✅ Upload the installer as a release asset
   - ✅ Generate release notes

4. **Check the release:**
   - Go to: https://github.com/JonathanLee2020/MacKeys/releases
   - Your release should appear in a few minutes
   - The installer will be available for download

## Manual Release (If needed)

If GitHub Actions doesn't work or you want to build locally:

1. **On a Windows machine:**
   ```bash
   # Build the executable
   python build.py

   # Install Inno Setup from https://jrsoftware.org/isdl.php
   # Open installer.iss in Inno Setup
   # Compile (Ctrl+F9)
   ```

2. **Create release on GitHub:**
   - Go to Releases → Draft a new release
   - Create a tag (e.g., `v1.0.0`)
   - Upload `installer_output/MacKeys-Setup-v1.0.0.exe`
   - Publish

## Version Numbering

Follow semantic versioning: `vMAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes

Examples:
- `v1.0.0` - Initial release
- `v1.1.0` - Added new shortcuts
- `v1.0.1` - Fixed bug in Alt+Backspace

## Testing Before Release

Before creating a release tag:

1. Test all shortcuts work
2. Test system tray icon appears
3. Test enable/disable toggle
4. Test on a clean Windows installation if possible
5. Check antivirus doesn't flag it

## Workflow Status

Check build status at:
https://github.com/JonathanLee2020/MacKeys/actions
