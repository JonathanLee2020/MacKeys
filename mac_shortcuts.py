"""
Mac-like Keyboard Shortcuts for Windows
Implements Mac-style keyboard shortcuts on Windows:
- Alt + Backspace: Delete entire line
- Win + Backspace: Delete entire word
- Alt + `: Switch between instances of same app
- Alt + [key]: Replace Ctrl with Alt for common shortcuts
"""

import keyboard
import time
import win32gui
import win32process
import psutil
import pystray
from PIL import Image, ImageDraw
import threading
from collections import defaultdict

# Track active windows by process name
window_tracker = defaultdict(list)

def get_window_process_name(hwnd):
    """Get the process name of a window"""
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        return process.name()
    except:
        return None

def enum_windows_callback(hwnd, _):
    """Callback to enumerate all windows"""
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
        process_name = get_window_process_name(hwnd)
        if process_name:
            window_tracker[process_name].append(hwnd)

def switch_app_instances():
    """Switch between instances of the current application"""
    try:
        # Get current foreground window
        current_hwnd = win32gui.GetForegroundWindow()
        current_process = get_window_process_name(current_hwnd)

        if not current_process:
            return

        # Rebuild window list
        window_tracker.clear()
        win32gui.EnumWindows(enum_windows_callback, None)

        # Get all windows for current process
        windows = window_tracker.get(current_process, [])

        if len(windows) <= 1:
            return

        # Find current window index and switch to next
        try:
            current_index = windows.index(current_hwnd)
            next_index = (current_index + 1) % len(windows)
            next_hwnd = windows[next_index]

            # Bring next window to foreground
            win32gui.ShowWindow(next_hwnd, 9)  # SW_RESTORE
            win32gui.SetForegroundWindow(next_hwnd)
        except ValueError:
            # Current window not in list, just switch to first one
            if windows:
                win32gui.ShowWindow(windows[0], 9)
                win32gui.SetForegroundWindow(windows[0])
    except Exception as e:
        print(f"Error switching windows: {e}")

def delete_line():
    """Delete entire line (Mac: Cmd+Backspace, Windows: Alt+Backspace)"""
    keyboard.send('home')
    keyboard.send('shift+end')
    keyboard.send('backspace')

def delete_word():
    """Delete word backwards (Mac: Option+Backspace, Windows: Win+Backspace)"""
    keyboard.send('ctrl+backspace')

# Global state for shortcuts
shortcuts_enabled = True
registered_hotkeys = []

def clear_shortcuts():
    """Remove all registered shortcuts"""
    global registered_hotkeys
    for hotkey in registered_hotkeys:
        try:
            keyboard.remove_hotkey(hotkey)
        except:
            pass
    registered_hotkeys.clear()

def setup_shortcuts():
    """Set up all keyboard shortcuts"""
    global registered_hotkeys

    if not shortcuts_enabled:
        return

    # Clear any existing shortcuts first
    clear_shortcuts()

    # Alt + Backspace: Delete entire line
    registered_hotkeys.append(keyboard.add_hotkey('alt+backspace', delete_line, suppress=True))

    # Win + Backspace: Delete entire word
    registered_hotkeys.append(keyboard.add_hotkey('win+backspace', delete_word, suppress=True))

    # Alt + `: Switch between app instances
    registered_hotkeys.append(keyboard.add_hotkey('alt+`', switch_app_instances, suppress=True))

    # Common Alt-based shortcuts (replacing Ctrl with Alt)
    shortcuts = {
        # Browser/Tab management
        'alt+r': 'ctrl+r',      # Reload page
        'alt+t': 'ctrl+t',      # New tab
        'alt+w': 'ctrl+w',      # Close tab
        'alt+shift+t': 'ctrl+shift+t',  # Reopen closed tab
        'alt+tab': None,        # Don't override Alt+Tab (Windows default)
        'alt+l': 'ctrl+l',      # Focus address bar

        # Text editing
        'alt+a': 'ctrl+a',      # Select all
        'alt+c': 'ctrl+c',      # Copy
        'alt+x': 'ctrl+x',      # Cut
        'alt+v': 'ctrl+v',      # Paste
        'alt+z': 'ctrl+z',      # Undo
        'alt+shift+z': 'ctrl+y',# Redo
        'alt+f': 'ctrl+f',      # Find
        'alt+s': 'ctrl+s',      # Save
        'alt+n': 'ctrl+n',      # New
        'alt+o': 'ctrl+o',      # Open
        'alt+p': 'ctrl+p',      # Print

        # Text navigation
        'alt+left': 'ctrl+left',    # Move word left
        'alt+right': 'ctrl+right',  # Move word right
        'alt+up': 'ctrl+up',        # Move paragraph up
        'alt+down': 'ctrl+down',    # Move paragraph down

        # Browser navigation
        'alt+[': 'ctrl+shift+tab',  # Previous tab
        'alt+]': 'ctrl+tab',        # Next tab
        'alt+shift+[': 'alt+left',  # Back
        'alt+shift+]': 'alt+right', # Forward

        # General
        'alt+q': 'alt+f4',      # Quit application
        'alt+shift+q': 'alt+f4',# Force quit
        'alt+,': None,          # Settings (app-specific, skip)
    }

    for hotkey, replacement in shortcuts.items():
        if replacement:
            # Suppress the Alt combo and send the Ctrl equivalent
            registered_hotkeys.append(
                keyboard.add_hotkey(
                    hotkey,
                    lambda r=replacement: keyboard.send(r),
                    suppress=True
                )
            )

def create_icon_image():
    """Create a simple icon for the system tray"""
    # Create a 64x64 image with a Mac-style command symbol
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Draw a stylized "M" for Mac
    draw.rectangle([10, 10, 54, 54], fill=(0, 122, 255))
    draw.text((16, 18), "M", fill=(255, 255, 255))

    return image

def toggle_shortcuts(icon, item):
    """Toggle shortcuts on/off"""
    global shortcuts_enabled
    shortcuts_enabled = not shortcuts_enabled

    if shortcuts_enabled:
        setup_shortcuts()
        icon.notify("Mac Shortcuts Enabled", "Shortcuts are now active")
    else:
        clear_shortcuts()
        icon.notify("Mac Shortcuts Disabled", "Shortcuts are now inactive")

def quit_app(icon, item):
    """Quit the application"""
    global shortcuts_enabled
    shortcuts_enabled = False
    clear_shortcuts()
    icon.stop()

def show_help(icon, item):
    """Show help notification"""
    icon.notify(
        "Mac Shortcuts for Windows",
        "Alt+Backspace: Delete line\n"
        "Win+Backspace: Delete word\n"
        "Alt+`: Switch app instances\n"
        "Alt+C/V/X/Z/S: Copy/Paste/Cut/Undo/Save\n"
        "Right-click icon for options"
    )

def run_tray_icon():
    """Run the system tray icon"""
    icon_image = create_icon_image()

    menu = pystray.Menu(
        pystray.MenuItem(
            "Enabled",
            toggle_shortcuts,
            checked=lambda item: shortcuts_enabled
        ),
        pystray.MenuItem("Help", show_help),
        pystray.MenuItem("Quit", quit_app)
    )

    icon = pystray.Icon(
        "mac_shortcuts",
        icon_image,
        "Mac Shortcuts for Windows",
        menu
    )

    icon.run()

def main():
    """Main function to start the shortcut listener"""
    print("Mac-like Shortcuts for Windows")
    print("=" * 50)
    print("\nSystem tray icon starting...")
    print("Look for the Mac Shortcuts icon in your system tray")
    print("\nActive Shortcuts:")
    print("  Alt + Backspace     : Delete entire line")
    print("  Win + Backspace     : Delete entire word")
    print("  Alt + `             : Switch app instances")
    print("  Alt + R             : Reload page")
    print("  Alt + W             : Close tab")
    print("  Alt + T             : New tab")
    print("  Alt + C/V/X/A       : Copy/Paste/Cut/Select All")
    print("  Alt + Z             : Undo")
    print("  Alt + S             : Save")
    print("  Alt + F             : Find")
    print("  Alt + Q             : Quit application")
    print("  ... and more!")
    print("\nRight-click the tray icon to:")
    print("  - Enable/Disable shortcuts")
    print("  - View help")
    print("  - Quit the app")
    print("=" * 50)

    # Set up shortcuts
    setup_shortcuts()

    # Start system tray icon in a separate thread
    tray_thread = threading.Thread(target=run_tray_icon, daemon=True)
    tray_thread.start()

    try:
        # Keep the script running
        keyboard.wait()
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        clear_shortcuts()

if __name__ == "__main__":
    # Note: This script requires administrator privileges on Windows
    main()
