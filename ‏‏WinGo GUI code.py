import tkinter as tk
from tkinter import ttk
import subprocess
import os
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO

class BatchLauncherDark(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("WinGo")
        self.geometry("800x600")
        self.configure(bg="#1E1E1E")

        try:
            logo_url = "https://raw.githubusercontent.com/TheYali1/WinGo/refs/heads/main/WinGo%20main%20logo.png"
            response = requests.get(logo_url)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            original_logo = Image.open(img_data)
            logo_width = 300
            ratio = logo_width / original_logo.width
            logo_height = int(original_logo.height * ratio)
            resized_logo = original_logo.resize((logo_width, logo_height))
            self.logo_photo = ImageTk.PhotoImage(resized_logo)
            
            logo_label = tk.Label(self,
                                image=self.logo_photo,
                                bg="#1E1E1E",
                                cursor="hand2")
            logo_label.pack(pady=20)
            logo_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/TheYali1/WinGo"))
        except Exception as e:
            print(f"Could not load logo: {e}")
            logo_label = tk.Label(self,
                                text="WinGo",
                                font=('Segoe UI', 24, 'bold'),
                                bg="#1E1E1E",
                                fg="white")
            logo_label.pack(pady=20)

        main_frame = tk.Frame(self, bg="#2D2D2D", padx=20, pady=20)
        main_frame.pack(pady=20, padx=50, fill="both", expand=True)

        button_frame = tk.Frame(main_frame, bg="#2D2D2D")
        button_frame.pack(pady=20, fill="both", expand=True)

        for i in range(2):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)

        button_names = [
            "Pro",
            "Pro N",
            "Home",
            "Home N",
            "Home Single Language",
            "Home Country Specific",
            "Education",
            "Education N",
            "Enterprise",
            "Enterprise N"
        ]

        icon_urls = [
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true",
            "https://filestore.community.support.microsoft.com/api/images/7c06f078-b027-434d-8a83-4af7d3d64452?upload=true"
        ]

        self.button_icons = []

        for i in range(10):
            row = i // 5
            col = i % 5
            try:
                response = requests.get(icon_urls[i])
                response.raise_for_status()
                img_data = BytesIO(response.content)
                icon_image = Image.open(img_data).resize((32, 32))
                photo = ImageTk.PhotoImage(icon_image)
                self.button_icons.append(photo)
            except Exception as e:
                print(f"Could not load icon {i+1}: {e}")
                self.button_icons.append(None)

            btn = tk.Button(button_frame,
                            text=button_names[i],
                            font=('Segoe UI', 11),
                            bg="#0078D4",
                            fg="white",
                            relief="flat",
                            compound="top",
                            padx=20,
                            pady=10,
                            cursor="hand2",
                            command=lambda x=i: self.run_batch(x),
                            image=self.button_icons[i] if self.button_icons[i] else None)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            btn.bind("<Enter>", lambda e, btn=btn: btn.configure(bg="#006CBC"))
            btn.bind("<Leave>", lambda e, btn=btn: btn.configure(bg="#0078D4"))

        self.progress = ttk.Progressbar(main_frame,
                                        orient="horizontal",
                                        length=700,
                                        mode='determinate')
        self.progress.pack(pady=20)

        self.log_text = tk.Text(main_frame,
                                height=6,
                                bg="#2D2D2D",
                                fg="#808080",
                                font=('Consolas', 10),
                                relief="flat")
        self.log_text.pack(fill="both", expand=True)

        clear_logs_btn = tk.Button(main_frame,
                                text="Clear Logs",
                                font=('Segoe UI', 10),
                                bg="#FF3B30",
                                fg="white",
                                relief="flat",
                                cursor="hand2",
                                command=self.clear_logs)
        clear_logs_btn.pack(pady=10)

        try:
            github_url = "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/github-white-icon.png"
            response = requests.get(github_url)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            github_logo = Image.open(img_data).resize((32, 32))
            self.github_photo = ImageTk.PhotoImage(github_logo)
            
            github_label = tk.Label(self,
                                    image=self.github_photo,
                                    bg="#1E1E1E",
                                    cursor="hand2")
            github_label.pack(side="bottom", pady=20)
            github_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/TheYali1/WinGo"))
        except Exception as e:
            print(f"Could not load GitHub logo: {e}")

    def run_batch(self, index):
        """Running a batch file by index"""
        script_dir = os.path.dirname(os.path.realpath(__file__))
        batch_path = os.path.join(script_dir, "batch_files", f"batch{index+1}.bat")
        
        print(f"Looking for batch file: {batch_path}")
        if os.path.exists(batch_path):
            self.log_text.insert("end", "Running The Code...")
            subprocess.Popen([batch_path], shell=True)
        else:
            self.log_text.insert("end", f"\nError: {batch_path} not found!\n")
        self.log_text.see("end")



    def clear_logs(self):
        """Clearing the log area"""
        self.log_text.delete("1.0", "end")


if __name__ == "__main__":
    app = BatchLauncherDark()
    app.mainloop()
