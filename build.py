#!/usr/bin/env python3
"""
Build script for creating standalone executables
"""

import subprocess
import sys
import shutil
from pathlib import Path


def run_command(cmd, description):
    """Run a command and print status"""
    print(f"\n{'='*50}")
    print(f"{description}")
    print(f"{'='*50}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\nERROR: {description} failed!")
        sys.exit(1)
    return result


def main():
    print("""
    ╔════════════════════════════════════════╗
    ║  Virtual Stress Ball - Build Script   ║
    ╚════════════════════════════════════════╝
    """)

    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller is installed")
    except ImportError:
        print("✗ PyInstaller not found. Installing...")
        run_command(
            f"{sys.executable} -m pip install pyinstaller",
            "Installing PyInstaller"
        )

    # Clean previous builds
    print("\n[1/3] Cleaning previous builds...")
    for dir_name in ['build', 'dist']:
        if Path(dir_name).exists():
            shutil.rmtree(dir_name)
            print(f"  ✓ Removed {dir_name}/")

    # Build executable
    print("\n[2/3] Building executable...")
    run_command(
        f"{sys.executable} -m PyInstaller --clean stress_ball.spec",
        "Building with PyInstaller"
    )

    # Success message
    print("\n[3/3] Build complete!")
    print(f"""
    ╔════════════════════════════════════════╗
    ║            BUILD SUCCESS!              ║
    ╚════════════════════════════════════════╝

    Your executable is located at:
      📁 dist/VirtualStressBall{'.exe' if sys.platform == 'win32' else ''}

    You can distribute this file to run on any
    compatible system without Python installed!

    File size: {Path('dist').stat().st_size / (1024*1024):.1f} MB (approx)
    """)


if __name__ == "__main__":
    main()
