@echo off
echo ========================================
echo Virtual Stress Ball - Windows Builder
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Installing PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo ERROR: Failed to install PyInstaller
    pause
    exit /b 1
)

echo.
echo [2/4] Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo.
echo [3/4] Building Windows executable...
pyinstaller --clean stress_ball.spec
if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo [4/4] Build complete!
echo.
echo ========================================
echo SUCCESS!
echo ========================================
echo Your executable is located at:
echo   dist\VirtualStressBall.exe
echo.
echo You can copy this .exe file to any Windows computer
echo and run it without installing Python!
echo ========================================
echo.
pause
