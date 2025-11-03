#!/usr/bin/env python3
"""
Virtual Stress Ball - Rage Delete Edition
A therapeutic application for deleting fake files when you need to vent!
"""

import os
import random
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import atexit
import shutil


class VirtualStressBall:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Stress Ball - RAGE DELETE!")
        self.root.geometry("600x700")
        self.root.configure(bg="#1a1a1a")

        # Setup paths
        self.base_dir = Path(__file__).parent
        self.fake_files_dir = self.base_dir / "fake_files"
        self.fake_files_dir.mkdir(exist_ok=True)

        # Register cleanup on exit
        atexit.register(self.cleanup_fake_files)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Annoying file names for stress relief
        self.file_templates = [
            "URGENT_READ_NOW_{}.txt",
            "FINAL_FINAL_v{}.docx",
            "Meeting_Notes_Copy_{}.txt",
            "Untitled_{}.txt",
            "New_Document_{}.doc",
            "Screenshot_{}.png",
            "DO_NOT_DELETE_{}.txt",
            "IMPORTANT_{}.pdf",
            "backup_backup_{}.zip",
            "tmp_file_{}.tmp",
            "draft_{}.txt",
            "revised_FINAL_{}.docx",
            "TO_BE_REVIEWED_{}.xlsx",
            "old_version_{}.bak",
            "random_thoughts_{}.txt"
        ]

        # Create initial fake files
        self.generate_fake_files(25)

        # Setup GUI
        self.setup_ui()
        self.refresh_file_list()

        # Bind keyboard shortcuts
        self.root.bind('<Return>', lambda event: self.rage_delete())
        self.root.bind('<Delete>', lambda event: self.rage_delete())
        self.root.bind('<BackSpace>', lambda event: self.rage_delete())

    def generate_fake_files(self, count=10):
        """Generate fake files with random annoying names"""
        for i in range(count):
            template = random.choice(self.file_templates)
            filename = template.format(random.randint(1, 999))
            filepath = self.fake_files_dir / filename

            # Create empty file with some fake content
            with open(filepath, 'w') as f:
                f.write(f"This is a fake file for stress relief.\n")
                f.write(f"File ID: {random.randint(10000, 99999)}\n")
                f.write("Feel free to DELETE me!\n")

    def setup_ui(self):
        """Setup the user interface"""
        # Title
        title_label = tk.Label(
            self.root,
            text="🔥 VIRTUAL STRESS BALL 🔥",
            font=("Arial", 24, "bold"),
            bg="#1a1a1a",
            fg="#ff4444"
        )
        title_label.pack(pady=20)

        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Delete fake files to release your stress!",
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="#ffffff"
        )
        subtitle.pack(pady=5)

        # Keyboard hint
        hint_label = tk.Label(
            self.root,
            text="Press Enter, Delete, or Backspace to rage delete!",
            font=("Arial", 10, "italic"),
            bg="#1a1a1a",
            fg="#888888"
        )
        hint_label.pack(pady=2)

        # File count label
        self.count_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#1a1a1a",
            fg="#00ff00"
        )
        self.count_label.pack(pady=10)

        # File list frame
        list_frame = tk.Frame(self.root, bg="#2a2a2a")
        list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox for files
        self.file_listbox = tk.Listbox(
            list_frame,
            font=("Courier", 11),
            bg="#2a2a2a",
            fg="#00ff00",
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set,
            highlightthickness=0,
            borderwidth=0
        )
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)

        # Status label for feedback
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            bg="#1a1a1a",
            fg="#ffaa00"
        )
        self.status_label.pack(pady=10)

        # Big DELETE button
        self.delete_button = tk.Button(
            self.root,
            text="💥 SMASH DELETE 💥",
            font=("Arial", 20, "bold"),
            bg="#ff0000",
            fg="#ffffff",
            activebackground="#cc0000",
            activeforeground="#ffffff",
            command=self.rage_delete,
            height=2,
            cursor="hand2"
        )
        self.delete_button.pack(pady=20, padx=40, fill=tk.X)

        # Add more files button
        add_button = tk.Button(
            self.root,
            text="Add More Annoying Files",
            font=("Arial", 10),
            bg="#444444",
            fg="#ffffff",
            activebackground="#555555",
            command=lambda: self.add_more_files(10),
            cursor="hand2"
        )
        add_button.pack(pady=5)

    def refresh_file_list(self):
        """Refresh the file list display"""
        self.file_listbox.delete(0, tk.END)

        files = sorted(self.fake_files_dir.glob("*"))
        for file in files:
            if file.is_file():
                self.file_listbox.insert(tk.END, f"  📄 {file.name}")

        # Update count
        file_count = len(files)
        self.count_label.config(text=f"Files remaining: {file_count}")

        # Update button state
        if file_count == 0:
            self.delete_button.config(state=tk.DISABLED)
            self.status_label.config(
                text="All files deleted! Add more to continue.",
                fg="#00ff00"
            )
        else:
            self.delete_button.config(state=tk.NORMAL)

    def rage_delete(self):
        """Delete a random file with dramatic effect!"""
        files = list(self.fake_files_dir.glob("*"))
        files = [f for f in files if f.is_file()]

        if not files:
            self.status_label.config(text="No files to delete!", fg="#ffaa00")
            return

        # Pick a random file
        target_file = random.choice(files)

        # Visual feedback
        self.delete_button.config(bg="#ff6600")
        self.status_label.config(
            text=f"💥 DELETED: {target_file.name} 💥",
            fg="#ff0000"
        )

        # Delete the file
        target_file.unlink()

        # Refresh UI
        self.refresh_file_list()

        # Reset button color after delay
        self.root.after(200, lambda: self.delete_button.config(bg="#ff0000"))

        # Clear status after delay
        self.root.after(2000, lambda: self.status_label.config(text=""))

    def add_more_files(self, count):
        """Add more fake files"""
        self.generate_fake_files(count)
        self.refresh_file_list()
        self.status_label.config(
            text=f"Added {count} more annoying files!",
            fg="#00aaff"
        )
        self.root.after(2000, lambda: self.status_label.config(text=""))

    def cleanup_fake_files(self):
        """Remove all fake files on exit"""
        if self.fake_files_dir.exists():
            shutil.rmtree(self.fake_files_dir)
            print("Cleaned up all fake files!")

    def on_closing(self):
        """Handle window close event"""
        self.cleanup_fake_files()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = VirtualStressBall(root)
    root.mainloop()


if __name__ == "__main__":
    main()
