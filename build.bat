@echo off
REM Build script for Mac Shortcuts Windows executable

echo Building Mac Shortcuts for Windows...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run the build script
echo.
echo Building executable...
python build.py

echo.
echo ========================================
echo Build complete!
echo.
echo The executable is located at:
echo   dist\MacShortcuts.exe
echo.
echo To distribute:
echo 1. Copy MacShortcuts.exe to any location
echo 2. Run it with administrator privileges
echo 3. Look for the icon in system tray
echo ========================================
pause
