"""
Build script to create a standalone executable for Mac Shortcuts
Run this script to build the .exe file
"""

import PyInstaller.__main__
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, 'icon.ico') if os.path.exists(os.path.join(script_dir, 'icon.ico')) else None

# PyInstaller arguments
pyinstaller_args = [
    'mac_shortcuts.py',           # Your main script
    '--onefile',                  # Create a single executable
    '--windowed',                 # Don't show console window (runs in background)
    '--name=MacShortcuts',        # Name of the executable
    '--clean',                    # Clean PyInstaller cache
    '--noconfirm',                # Replace output directory without asking
]

# Add icon if it exists
if icon_path:
    pyinstaller_args.append(f'--icon={icon_path}')

# Add hidden imports that PyInstaller might miss
pyinstaller_args.extend([
    '--hidden-import=win32timezone',
    '--hidden-import=pystray._win32',
    '--hidden-import=PIL._tkinter_finder',
])

# Add admin manifest for elevated privileges
pyinstaller_args.append('--uac-admin')

print("Building Mac Shortcuts executable...")
print("=" * 50)

PyInstaller.__main__.run(pyinstaller_args)

print("\n" + "=" * 50)
print("Build complete!")
print("Executable location: dist/MacShortcuts.exe")
print("\nIMPORTANT: Run the .exe with administrator privileges")
print("=" * 50)
