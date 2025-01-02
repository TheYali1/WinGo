import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import subprocess
import webbrowser

class WinGoApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("WinGo")
        self.window.geometry("600x530")
        self.window._set_appearance_mode("dark")
        self.window.resizable(False, False)
        self.window.configure(bg="#1f2937")
        
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        
        # Logo container frame
        logo_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        logo_frame.grid(row=0, column=0, columnspan=3, sticky="w", padx=20, pady=(20,0))
        
        try:
            logo_image = self.load_and_resize_image("code\\logo.png", (270, 100))
            logo_label = ctk.CTkLabel(logo_frame, image=logo_image)
            logo_label.grid(row=0, column=0, sticky="w")
        except Exception as e:
            print(f"Failed to load logo image: {e}")

        # Icons section
        icons_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        icons_frame.grid(row=0, column=2, sticky="e", padx=20)
        
        github_label = ctk.CTkLabel(
            icons_frame,
            text="By: The Yali",
            font=("Poppins", 14),
            text_color="white"
        )
        github_label.pack(side="left", padx=5)
        
        try:
            github_icon = ctk.CTkLabel(
                icons_frame,
                text="",
                image=self.load_and_resize_image("code\\github_icon.png", (40, 40)),
                cursor="hand2"
            )
            github_icon.pack(side="left", padx=5)
            github_icon.bind("<Button-1>", self.open_github)  # open link

        except Exception as e:
            print(f"Failed to load images: {e}")
        
        version_label = ctk.CTkLabel(
            self.window,
            text="Choose your Windows version:",
            font=("Poppins", 24)
        )
        version_label.grid(row=2, column=0, columnspan=3, pady=(20,20), padx=20, sticky="w")
        
        buttons_config = [
            ("Pro", 3, 0, "code\\pro_win"),
            ("Education", 3, 1, "code\\edu_win"),
            ("Home Single Language", 3, 2, "code\\home_sl_win"),
            ("Pro N", 4, 0, "code\\pro_n_win"),
            ("Education N", 4, 1, "code\\edu_n_win"),
            ("Home Country Specific", 4, 2, "code\\home_cs_win"),
            ("Home", 5, 0, "code\\home_win"),
            ("Enterprise", 5, 1, "code\\enterprise_win"),
            ("Enterprise N", 5, 2, "code\\enterprise_n_win"),
            ("Home N", 6, 0, "code\\home_n_win")
        ]
        
        for text, row, col, batch_id in buttons_config:
            button = ctk.CTkButton(
                self.window,
                text=text,
                font=("Poppins", 14),
                width=150,
                height=40,
                fg_color="#4287f5",
                hover_color="#3270d8",
                command=lambda id=batch_id: self.run_batch_file(id)
            )
            button.grid(row=row, column=col, pady=10, padx=10)
        
        copyright_label = ctk.CTkLabel(
            self.window,
            text="© 2025",
            font=("Poppins", 12),
            text_color="gray"
        )
        copyright_label.grid(row=7, column=0, columnspan=3, pady=(40,20), sticky="ew")

    def load_and_resize_image(self, filename, size):
        image = Image.open(filename)
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ctk.CTkImage(light_image=image, dark_image=image, size=size)

    def open_github(self, event=None):
        # Github link
        webbrowser.open("https://github.com/TheYali1/WinGo")

    def run_batch_file(self, batch_id):
        # Assuming the batch files are stored in a specific folder (e.g., "code")
        batch_file_path = os.path.join(os.getcwd(), batch_id + ".bat")
        if os.path.exists(batch_file_path):
            subprocess.run(batch_file_path, shell=True)
        else:
            print(f"Batch file {batch_file_path} not found.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = WinGoApp()
    app.run()
