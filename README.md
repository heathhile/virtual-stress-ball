# Virtual Stress Ball - Rage Delete Edition

A therapeutic Python application that lets you rage delete fake files to release stress!

## Features

- **Fake File Generation**: Creates 25 annoying fake files on startup with names like "FINAL_FINAL_v3.docx" and "DO_NOT_DELETE_42.txt"
- **Rage Delete Button**: A big, satisfying button to smash and delete random files
- **Keyboard Shortcuts**: Press Enter, Delete, or Backspace to rage delete!
- **Visual Feedback**: Color changes and status messages for that satisfying deletion feeling
- **Safe**: Only deletes fake files in the isolated `fake_files/` directory
- **Auto Cleanup**: All fake files are removed when you close the application
- **Add More Files**: Button to generate more files when you need to keep venting
- **Standalone Executable**: Can be packaged as a Windows .exe with no Python required!

## Requirements

### For Running the Python Script
- Python 3.6 or higher
- tkinter (usually comes with Python)

### For Windows Users (No Python Required)
- Just download the pre-built `.exe` file and double-click to run!

## Usage

### Option 1: Run with Python

```bash
python stress_ball.py
```

or make it executable:

```bash
chmod +x stress_ball.py
./stress_ball.py
```

### Option 2: Use Windows Standalone Executable

Double-click `VirtualStressBall.exe` - no installation needed!

## Building Windows Executable

Want to create a standalone `.exe` that runs on Windows without Python? Follow these steps:

### On Windows:

1. Make sure Python is installed
2. Run the build script:
   ```cmd
   build_windows.bat
   ```
3. Find your executable in `dist/VirtualStressBall.exe`
4. Copy it anywhere - it runs without Python!

### On Mac/Linux (Cross-platform build):

```bash
python build.py
```

### Manual Build:

```bash
pip install pyinstaller
pyinstaller --clean stress_ball.spec
```

Your standalone executable will be in the `dist/` folder. You can copy this file to any Windows computer and run it without installing Python!

## How It Works

1. **On Startup**: Creates a `fake_files/` directory and generates 25 fake files
2. **During Use**: Click the "SMASH DELETE" button to randomly delete files with visual feedback
3. **Add More**: Click "Add More Annoying Files" to generate 10 more files when you run out
4. **On Close**: Automatically cleans up all fake files and the directory

## Safety

- All files are created in an isolated `fake_files/` directory
- Only these fake files can be deleted by the application
- Complete cleanup happens automatically when you close the app
- No real files are ever touched

## Perfect For

- Stressful work days
- Post-meeting frustration
- General rage venting
- Therapeutic file deletion without consequences

Enjoy your stress-free rage deleting!
