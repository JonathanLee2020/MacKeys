# Mac Shortcuts for Windows

> **Transform your Windows keyboard experience with Mac-style shortcuts**

A lightweight system tray app that brings Mac keyboard shortcuts to Windows. No complex setup—just download, run, and enjoy Mac-like productivity on Windows.

## 🎯 Quick Start for Users

### Download & Install (Easiest Method)

1. **Download** `MacKeys-Setup.exe` from [Releases](../../releases)
2. **Run the installer** (double-click the downloaded file)
3. **Follow the installation wizard**
4. **Look for the tray icon** in the bottom-right of your screen
5. **Start using Mac shortcuts!**

That's it! No Python, no dependencies, no manual configuration needed.

> **Note:** The installer will optionally set up auto-start and create shortcuts for you.

### System Tray Controls

Right-click the system tray icon to:
- ✅ **Enable/Disable** shortcuts on-the-fly
- 📖 **View help** with shortcut list
- ❌ **Quit** the application

---

## ✨ Features

### 1. **Alt + Backspace** - Delete Entire Line
Deletes the entire current line (like Cmd+Backspace on Mac)

### 2. **Win + Backspace** - Delete Word
Deletes the word before the cursor (like Option+Backspace on Mac)

### 3. **Alt + `** - Switch Between App Instances
Cycles through all open windows of the same application (like Cmd+` on Mac)

### 4. **Alt-based Shortcuts** - Replace Ctrl with Alt
All common keyboard shortcuts work with Alt instead of Ctrl:

**Text Editing:**
- `Alt + C/V/X/A` - Copy/Paste/Cut/Select All
- `Alt + Z` - Undo
- `Alt + Shift + Z` - Redo
- `Alt + S` - Save
- `Alt + F` - Find
- `Alt + N` - New
- `Alt + O` - Open
- `Alt + P` - Print

**Browser/Tab Management:**
- `Alt + R` - Reload page
- `Alt + T` - New tab
- `Alt + W` - Close tab
- `Alt + Shift + T` - Reopen closed tab
- `Alt + L` - Focus address bar
- `Alt + [` - Previous tab
- `Alt + ]` - Next tab
- `Alt + Shift + [` - Back
- `Alt + Shift + ]` - Forward

**Application:**
- `Alt + Q` - Quit application

**Text Navigation:**
- `Alt + Left/Right` - Move by word
- `Alt + Up/Down` - Move by paragraph

---

## 🚀 Auto-Start on Windows Startup (Optional)

### Method 1: Task Scheduler (Recommended)

1. Open Task Scheduler (`Win + R` → type `taskschd.msc` → press Enter)

2. Click **"Create Task"** (not "Create Basic Task")

3. Configure the task:
   - **General Tab:**
     - Name: `Mac Shortcuts`
     - ✅ Check "Run with highest privileges"
   - **Triggers Tab:**
     - Click "New" → "At log on" → OK
   - **Actions Tab:**
     - Click "New" → "Start a program"
     - Browse to `MacShortcuts.exe` → OK
   - **Conditions Tab:**
     - ❌ Uncheck "Start only if on AC power"

4. Click OK and enter your password if prompted

### Method 2: Startup Folder (Simpler, but may prompt for password)

1. Press `Win + R`, type `shell:startup`, press Enter
2. Create a shortcut to `MacShortcuts.exe` in this folder
3. Right-click shortcut → Properties → Advanced → Check "Run as administrator"

---

## 👨‍💻 For Developers

Want to build from source or customize? See [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md)

### Quick Build

```bash
# Install dependencies
pip install -r requirements.txt

# Build executable
python build.py

# Or use the batch file
build.bat
```

The executable will be in `dist/MacShortcuts.exe`

---

## ❓ Troubleshooting

### The app doesn't start or shortcuts don't work
- ⚠️ **Run as administrator** (this is required for keyboard hooking)
- Check if antivirus is blocking the app (add an exclusion)
- Look for the system tray icon—if it's not there, the app isn't running

### Some shortcuts don't work in certain apps
- Some applications override shortcuts (e.g., IDEs, games)
- Toggle shortcuts off/on via the tray icon to test
- You can customize which shortcuts are active (see Developer section)

### Alt + ` doesn't switch between windows
- This feature works with most apps but some may not be detected
- Make sure you have multiple windows of the same app open

### Windows SmartScreen warning
- This is normal for unsigned executables
- Click "More info" → "Run anyway"
- Or build from source yourself (see BUILD_INSTRUCTIONS.md)

### System tray icon doesn't appear
- Check the hidden icons area (click the ^ icon in system tray)
- Make sure you're running with admin privileges

---

## 🗑️ Uninstalling

**If you used the installer:**
1. Go to Windows Settings → Apps → Installed apps
2. Find "MacKeys" and click Uninstall

**If you're running the standalone .exe:**
1. Right-click the tray icon → **Quit**
2. Remove from Task Scheduler (if you set up auto-start manually)
3. Delete `MacShortcuts.exe`

---

## 🎨 Customization

Want to customize which shortcuts are active or add your own?

1. Download the source code
2. Edit [mac_shortcuts.py](mac_shortcuts.py):
   ```python
   shortcuts = {
       'alt+r': 'ctrl+r',      # Modify existing shortcuts
       'alt+custom': 'ctrl+shift+x',  # Add your own
   }
   ```
3. Build your own .exe with `python build.py`

See [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md) for details.

---

## ⚠️ Important Notes

- **Admin privileges required**: Needed for system-wide keyboard hooking
- **Lightweight**: Runs in background with minimal resource usage (~10-20MB RAM)
- **No telemetry**: No data collection, no internet connection required
- **Open source**: Full source code available for inspection
- **Alt+Tab preserved**: Windows default Alt+Tab is not modified

---

## 📋 Comparison with Alternatives

| Feature | Mac Shortcuts | PowerToys | AutoHotkey |
|---------|--------------|-----------|------------|
| Easy to use | ✅ One-click .exe | ✅ Installer | ❌ Scripting required |
| System tray toggle | ✅ Yes | ❌ No | Depends on script |
| Delete line (Alt+Backspace) | ✅ Yes | ❌ No | Custom script needed |
| App instance switching | ✅ Yes (Alt+`) | ❌ No | Custom script needed |
| Alt→Ctrl remapping | ✅ Comprehensive | ⚠️ Limited | Custom script needed |
| Resource usage | ✅ <20MB | ⚠️ ~100MB+ | ✅ Low |

---

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs or request features via [Issues](../../issues)
- Submit pull requests with improvements
- Share your custom shortcut configurations

---

## 📄 License

Free to use and modify for personal use. See source code for details.

---

## 🙏 Credits

Built with:
- [keyboard](https://github.com/boppreh/keyboard) - Keyboard hooking
- [pystray](https://github.com/moses-palmer/pystray) - System tray icon
- [pywin32](https://github.com/mhammond/pywin32) - Windows API
- [PyInstaller](https://www.pyinstaller.org/) - Executable packaging

---

**Made with ❤️ for Mac users on Windows**
