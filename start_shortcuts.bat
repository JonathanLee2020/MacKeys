@echo off
REM Batch script to start Mac-like shortcuts for Windows
REM Run this with administrator privileges

cd /d "%~dp0"
python mac_shortcuts.py
pause
