# Windows Build Guide

This guide will help you create a standalone Windows executable that runs without Python installed.

## Quick Start (Easiest Method)

1. **Get the Code**
   - Download the repository as ZIP from GitHub: https://github.com/heathhile/virtual-stress-ball
   - Click the green "Code" button → "Download ZIP"
   - Extract the ZIP file to a folder

   OR if you have Git installed:
   ```cmd
   git clone https://github.com/heathhile/virtual-stress-ball.git
   cd virtual-stress-ball
   ```

2. **Install Python** (if not already installed)
   - Download from https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

3. **Build the Executable**
   - Open the `virtual-stress-ball` folder you downloaded/cloned
   - Double-click `build_windows.bat`
   - Wait for the build process to complete (1-2 minutes)

4. **Done!**
   - Find `VirtualStressBall.exe` in the `dist/` folder
   - Copy this file anywhere you want
   - Share it with friends - no Python needed to run it!

## What You Get

- **File**: `dist/VirtualStressBall.exe`
- **Size**: ~15-25 MB (includes Python runtime)
- **Requirements**: None! It's completely standalone
- **Portable**: Copy to USB drives, email it, share it anywhere

## Distributing Your App

You can share `VirtualStressBall.exe` with anyone who has Windows:

1. Copy `VirtualStressBall.exe` from the `dist/` folder
2. Send it via email, USB drive, or cloud storage
3. Recipients just double-click to run - no installation needed!

## Troubleshooting

### "Python is not recognized"
- Reinstall Python and check "Add Python to PATH" during installation
- Or open Command Prompt as Administrator and run: `setx PATH "%PATH%;C:\Python3x"` (replace with your Python path)

### "pyinstaller is not recognized as a command"
- This is a common Windows PATH issue
- The build script has been updated to fix this automatically
- If you still see this error, run manually: `python -m PyInstaller --clean stress_ball.spec`

### Build fails
- Make sure you have internet connection (needed to download PyInstaller)
- Try running Command Prompt as Administrator
- Manually install PyInstaller: `python -m pip install pyinstaller`
- Then build with: `python -m PyInstaller --clean stress_ball.spec`

### Antivirus flags the .exe
- This is normal for PyInstaller executables
- Add an exception in your antivirus
- The code is open source - you can verify it's safe

## Advanced: Manual Build

If you prefer manual control:

```cmd
REM Install PyInstaller
python -m pip install pyinstaller

REM Clean previous builds
rmdir /s /q build dist

REM Build executable
python -m PyInstaller --clean stress_ball.spec

REM Your .exe is now in dist/VirtualStressBall.exe
```

## File Structure After Build

```
virtual_stress_ball/
├── stress_ball.py          # Source code
├── build/                  # Temporary build files (can delete)
├── dist/
│   └── VirtualStressBall.exe  # 👈 YOUR STANDALONE EXECUTABLE
├── build_windows.bat       # Build script
└── stress_ball.spec        # PyInstaller configuration
```

## Notes

- The executable is self-contained with Python runtime
- Creates `fake_files/` folder next to the .exe when running
- All fake files are cleaned up when you close the app
- The .exe is portable - runs from any location

Happy rage deleting! 🔥
