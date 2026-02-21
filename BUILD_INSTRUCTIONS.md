# Build Instructions for Mac Shortcuts

This guide explains how to build a standalone `.exe` file that users can download and run without installing Python or dependencies.

## For Developers (Building the .exe)

### Prerequisites
- Windows 10 or later
- Python 3.7+ installed
- Git (optional)

### Build Steps

1. **Clone or download this repository**

2. **Open Command Prompt or PowerShell in the project directory**

3. **Run the build script:**
   ```bash
   build.bat
   ```

   Or manually:
   ```bash
   pip install -r requirements.txt
   python build.py
   ```

4. **Find your executable:**
   - Location: `dist/MacShortcuts.exe`
   - This is a single file that contains everything needed

5. **Test the executable:**
   - Right-click `MacShortcuts.exe` → "Run as administrator"
   - Look for the icon in your system tray
   - Test the shortcuts

### Distribution

The `MacShortcuts.exe` file is completely standalone and can be distributed as-is:

1. **Upload to GitHub Releases:**
   - Create a new release on GitHub
   - Upload the `dist/MacShortcuts.exe` file
   - Users can download directly

2. **Share via cloud storage:**
   - Upload to Google Drive, Dropbox, OneDrive, etc.
   - Share the download link

3. **Package as installer (optional):**
   - Use Inno Setup or NSIS to create an installer
   - This can add shortcuts, auto-start, etc.

## For End Users (Installing)

### Simple Installation

1. **Download `MacShortcuts.exe`** from the releases page or provided link

2. **Move it to a permanent location** (e.g., `C:\Program Files\MacShortcuts\`)

3. **Run as administrator:**
   - Right-click `MacShortcuts.exe`
   - Select "Run as administrator"
   - ⚠️ Admin privileges are required for keyboard hooking

4. **Look for the system tray icon:**
   - A small icon will appear in your system tray (bottom-right)
   - Right-click the icon to:
     - Enable/Disable shortcuts
     - View help
     - Quit the app

### Auto-Start on Windows Startup (Optional)

**Method 1: Task Scheduler (Recommended)**

1. Press `Win + R`, type `taskschd.msc`, press Enter

2. Click "Create Task" (not "Create Basic Task")

3. **General Tab:**
   - Name: `Mac Shortcuts`
   - Description: `Mac-like keyboard shortcuts for Windows`
   - Check "Run with highest privileges"
   - Check "Run whether user is logged on or not"

4. **Triggers Tab:**
   - Click "New"
   - Begin the task: "At log on"
   - Specific user: (your username)
   - Click OK

5. **Actions Tab:**
   - Click "New"
   - Action: "Start a program"
   - Program/script: Browse to `MacShortcuts.exe`
   - Click OK

6. **Conditions Tab:**
   - Uncheck "Start the task only if the computer is on AC power"

7. Click OK, enter your password if prompted

**Method 2: Startup Folder**

1. Press `Win + R`, type `shell:startup`, press Enter

2. Create a shortcut to `MacShortcuts.exe` in this folder

3. Right-click the shortcut → Properties → Advanced

4. Check "Run as administrator" (Note: This may prompt for password on startup)

## Building for Release

### Automated Build with GitHub Actions (Recommended)

Create `.github/workflows/build.yml`:

```yaml
name: Build Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Build executable
      run: python build.py

    - name: Upload artifact
      uses: actions/upload-artifact@v3
      with:
        name: MacShortcuts
        path: dist/MacShortcuts.exe

    - name: Create Release
      uses: softprops/action-gh-release@v1
      with:
        files: dist/MacShortcuts.exe
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

To trigger a build:
```bash
git tag v1.0.0
git push origin v1.0.0
```

## Troubleshooting Build Issues

### "PyInstaller not found"
```bash
pip install pyinstaller
```

### "Module not found during build"
Edit `build.py` and add the missing module to `--hidden-import` list

### Antivirus flags the .exe
- This is common with PyInstaller executables
- Add an exclusion in Windows Defender
- Sign the executable with a code signing certificate (for production)

### Build takes too long
- Use `--onefile` for single exe (slower startup)
- Or use `--onedir` for faster startup (multiple files)

## File Signing (Optional, for Production)

To avoid Windows SmartScreen warnings:

1. **Get a code signing certificate:**
   - Purchase from DigiCert, Sectigo, etc. (~$100-400/year)
   - Or use a free certificate from Let's Encrypt (limited)

2. **Sign the executable:**
   ```bash
   signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com MacShortcuts.exe
   ```

3. **Build reputation:**
   - SmartScreen warnings will decrease as more users download and run your app

## Testing Checklist

Before releasing:

- [ ] Test on clean Windows installation
- [ ] Verify all shortcuts work
- [ ] Test enable/disable toggle
- [ ] Test system tray icon shows up
- [ ] Test quit functionality
- [ ] Verify no console window appears
- [ ] Test on Windows 10 and 11
- [ ] Check file size is reasonable (<20MB)
- [ ] Scan with antivirus
- [ ] Test auto-start configuration

## Support & Issues

Users can report issues at: https://github.com/yourusername/windows_max/issues
