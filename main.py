import customtkinter as ctk
from PIL import Image
import os
import webbrowser
import subprocess
from tkinter import font as tkfont
from PIL import ImageFont 

ctk.set_appearance_mode("Dark")

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(CURRENT_DIR, "Font.ttf")
LOGO_PATH = os.path.join(CURRENT_DIR, "Logo.png")
GITHUB_ICON_PATH = os.path.join(CURRENT_DIR, "Github.png") 

COLOR_BACKGROUND_DARK = "#242424"
COLOR_CONTAINER_GRAY = "#1F1F1F"
COLOR_BLUE_PRIMARY = "#0c6cd5"
COLOR_BUTTON_BLUE = "#0c6cd5"
COLOR_BUTTON_HOVER = "#0a5ab3"
COLOR_GRAY_TEXT = "#FFFFFF"
COLOR_CONTAINER_HOVER = "#1F1F1F" 

SCALE_FACTOR = 1.1 
LOGO_SIZE = (300, 120)
GITHUB_ICON_SIZE = (45, 45)
BUTTON_WIDTH_SMALL = 250 

PADDING_NORMAL = 15 
PADDING_HOVER = 8  

FONT_SIZE_NORMAL = 22
FONT_SIZE_HOVER = 24  

ANIMATION_STEPS = 10
ANIMATION_INTERVAL_MS = 15

BUTTON_FILES = {
    "Pro": "1.png",
    "Home Single Language": "2.png",
    "Education": "3.png",
    "Education N": "4.png",
    "Enterprise N": "5.png",
    "Home Country Specific": "6.png",
    "Home": "7.png",
    "Home N": "8.png",
    "Enterprise": "9.png",
    "Pro N": "10.png",
}

BUTTON_BAT_FILES = {
    "Pro": "Pro.bat",
    "Pro N": "ProN.bat",
    "Education": "Education.bat",
    "Education N": "EducationN.bat",
    "Home Single Language": "HomeSingleLanguage.bat",
    "Home Country Specific": "HomeCountrySpecific.bat",
    "Home": "Home.bat",
    "Home N": "HomeN.bat",
    "Enterprise": "Enterprise.bat",
    "Enterprise N": "EnterpriseN.bat",
}

def load_app_font(size, weight="normal"):
    try:
        pil_font = ImageFont.truetype(FONT_PATH, size=size)
        font_name_tuple = pil_font.getname()
        font_family = font_name_tuple[0]
        tk_weight = "bold" if weight == "bold" else "normal"
        try:
            return ctk.CTkFont(family=font_family, size=size, weight=tk_weight)
        except:
            return ctk.CTkFont(family=font_family, size=size, weight=tk_weight)
    except Exception as e:
        try:
            if os.path.exists(FONT_PATH):
                font_obj = tkfont.Font(file=FONT_PATH, size=size)
                if weight == "bold":
                    font_obj.configure(weight="bold")
                font_family = font_obj.actual()["family"]
                return ctk.CTkFont(family=font_family, size=size, weight=weight)
        except:
            pass
        
        return ctk.CTkFont(family="Arial", size=size, weight=weight)

class WinGoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.font_wingu_title = load_app_font(56, "bold") 
        self.font_subtitle = load_app_font(20, "normal") 
        self.font_by_line = load_app_font(22, "normal")
        self.font_button = load_app_font(FONT_SIZE_NORMAL, "bold")

        self.title("WinGo - Here For You!")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.configure(fg_color=COLOR_BACKGROUND_DARK)

        self._load_assets()
        
        self.top_section_frame = ctk.CTkFrame(self, fg_color="transparent", height=120)
        self.top_section_frame.pack(fill="x", padx=40, pady=(40, 20)) 
        self.top_section_frame.pack_propagate(False)
        
        self.top_section_frame.grid_columnconfigure(0, weight=1) 
        self.top_section_frame.grid_columnconfigure(1, weight=0)
        self.top_section_frame.grid_rowconfigure(0, weight=1)

        self.left_header_frame = ctk.CTkFrame(self.top_section_frame, fg_color="transparent")
        self.left_header_frame.grid(row=0, column=0, sticky="wns")
        self.left_header_frame.grid_rowconfigure(0, weight=1)
        
        if self.logo_image:
            self.logo_label = ctk.CTkLabel(self.left_header_frame, image=self.logo_image, text="")
            self.logo_label.grid(row=0, column=0, sticky="w")
            self._animate_logo() 

        self.right_header_frame = ctk.CTkFrame(self.top_section_frame, fg_color="transparent")
        self.right_header_frame.grid(row=0, column=1, sticky="ens")
        self.right_header_frame.grid_rowconfigure(0, weight=1)
        
        self.right_content_frame = ctk.CTkFrame(self.right_header_frame, fg_color="transparent")
        self.right_content_frame.grid(row=0, column=0, sticky="e")
        
        self.by_label = ctk.CTkLabel(self.right_content_frame, text="By: TheYali1", 
                                     font=self.font_by_line, 
                                     text_color="#FFFFFF")
        self.by_label.pack(side="left", padx=(0, 15))
        self._animate_by_text()

        if self.github_image:
            self.github_icon_button = ctk.CTkButton(self.right_content_frame, text="", image=self.github_image, 
                                                    fg_color="transparent", hover_color=COLOR_BACKGROUND_DARK, 
                                                    width=GITHUB_ICON_SIZE[0], height=GITHUB_ICON_SIZE[1],
                                                    command=self._open_github)
            self.github_icon_button.pack(side="left", padx=(0, 0))
            self._animate_github_icon()
        
        self.buttons_container_outer = ctk.CTkFrame(self, fg_color=COLOR_CONTAINER_GRAY, corner_radius=20) 
        self.buttons_container_outer.pack(fill="both", expand=True, padx=40, pady=(0, 40))

        self.buttons_grid_frame = ctk.CTkFrame(self.buttons_container_outer, fg_color="transparent")
        self.buttons_grid_frame.pack(fill="both", expand=True, padx=20, pady=20) 

        self.buttons_grid_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="button_col")
        self.buttons_grid_frame.grid_rowconfigure((0, 1, 2, 3), weight=1, uniform="button_row")

        self._create_buttons()

    def _open_github(self):
        webbrowser.open("https://github.com/TheYali1")

    def _load_assets(self):
        self.logo_image = None
        try:
            logo_image_data = Image.open(LOGO_PATH).convert("RGBA")
            original_size = logo_image_data.size
            ratio = min(LOGO_SIZE[0] / original_size[0], LOGO_SIZE[1] / original_size[1])
            new_size = (int(original_size[0] * ratio), int(original_size[1] * ratio))
            logo_image_data = logo_image_data.resize(new_size, Image.Resampling.LANCZOS)
            self.logo_image = ctk.CTkImage(logo_image_data, size=new_size)
            self.logo_actual_size = new_size
        except FileNotFoundError:
            print(f"Error: File {LOGO_PATH} not found.")
        
        self.github_image = None
        try:
            github_image_data = Image.open(GITHUB_ICON_PATH).convert("RGBA")
            self.github_image = ctk.CTkImage(github_image_data, size=GITHUB_ICON_SIZE)
        except FileNotFoundError:
            print(f"Error: File {GITHUB_ICON_PATH} not found.")
            
        self.button_images = {}
        for name, filename in BUTTON_FILES.items():
            path = os.path.join(CURRENT_DIR, filename)
            try:
                img_data = Image.open(path).convert("RGBA")
                new_size = (int(img_data.width * SCALE_FACTOR), int(img_data.height * SCALE_FACTOR))
                self.button_images[name] = ctk.CTkImage(img_data, size=new_size)
            except FileNotFoundError:
                self.button_images[name] = None 

    def _ease_out_cubic(self, t):
        return 1 - (1 - t) ** 3
    
    def _ease_out_expo(self, t):
        if t >= 1.0:
            return 1.0
        return 1 - (2 ** (-10 * t))
    
    def _ease_out_back(self, t):
        c1 = 1.70158
        c3 = c1 + 1
        return 1 + c3 * ((t - 1) ** 3) + c1 * ((t - 1) ** 2)
    
    def _create_buttons(self):
        
        def create_wintype_button(name, row, col, columnspan=1):
            button_text = name
            button_font = self.font_button
            button_fg_color = COLOR_BUTTON_BLUE
            button_hover_color = COLOR_BUTTON_HOVER
            button_height = 50
            button_width = -1
            
            def run_bat_file(button_name):
                bat_file = BUTTON_BAT_FILES.get(button_name)
                if not bat_file:
                    bat_file = f"{button_name}.bat"
                bat_path = os.path.join(CURRENT_DIR, bat_file)
                if os.path.exists(bat_path):
                    try:
                        subprocess.Popen([bat_path], shell=True, cwd=CURRENT_DIR)
                    except Exception as e:
                        print(f"Error executing {bat_file}: {e}")
                else:
                    print(f"File not found: {bat_path}")
            
            button = ctk.CTkButton(self.buttons_grid_frame, 
                                 text=button_text, 
                                 font=button_font,
                                 text_color="#FFFFFF",
                                 fg_color=button_fg_color, 
                                 hover_color=button_hover_color,
                                 height=button_height,
                                 width=button_width, 
                                 corner_radius=12, 
                                 border_width=0, 
                                 command=lambda n=name: run_bat_file(n))
            
            button._original_padx = PADDING_NORMAL
            button._original_pady = PADDING_NORMAL
            button._original_font_size = FONT_SIZE_NORMAL
            
            button.grid(row=row, column=col, columnspan=columnspan, 
                        padx=PADDING_NORMAL, pady=PADDING_NORMAL, sticky="nsew")
            
            button.bind("<Enter>", self._on_button_enter)
            button.bind("<Leave>", self._on_button_leave)
            
            return button

        create_wintype_button("Pro", 0, 0)
        create_wintype_button("Pro N", 0, 1)
        create_wintype_button("Education", 0, 2)
        create_wintype_button("Education N", 0, 3)

        create_wintype_button("Home Single Language", 1, 0, columnspan=4)
        
        create_wintype_button("Home Country Specific", 2, 0, columnspan=4)

        create_wintype_button("Home", 3, 0)
        create_wintype_button("Home N", 3, 1)
        create_wintype_button("Enterprise", 3, 2)
        create_wintype_button("Enterprise N", 3, 3)

    def _on_button_enter(self, event):
        button = event.widget
        self._animate_padding(button, PADDING_HOVER, ANIMATION_STEPS, self._ease_out_back) 
        self._animate_font_size(button, FONT_SIZE_HOVER, ANIMATION_STEPS, self._ease_out_back) 

    def _on_button_leave(self, event):
        button = event.widget
        self._animate_padding(button, PADDING_NORMAL, ANIMATION_STEPS, self._ease_out_back) 
        self._animate_font_size(button, FONT_SIZE_NORMAL, ANIMATION_STEPS, self._ease_out_back) 

    def _resolve_button_widget(self, widget):
        if not hasattr(widget, '_original_padx') and hasattr(widget, 'master'):
            return widget.master
        return widget
        
    def _animate_padding(self, button, target_padx, steps, easing_func):
        button = self._resolve_button_widget(button)

        if not isinstance(button, ctk.CTkButton) or not hasattr(button, '_original_padx'):
            return 

        if hasattr(button, '_anim_job_padding'):
            self.after_cancel(button._anim_job_padding)
        
        start_padx = button.grid_info().get('padx', button._original_padx)
        start_pady = button.grid_info().get('pady', button._original_pady)
        target_pady = target_padx 

        if start_padx == target_padx:
            return

        def step_animation(step=0):
            t = step / steps
            eased_t = easing_func(t)
            
            current_padx = int(start_padx + (target_padx - start_padx) * eased_t)
            current_pady = int(start_pady + (target_pady - start_pady) * eased_t)
            
            button.grid(padx=current_padx, pady=current_pady, sticky="nsew")
            
            if step < steps:
                button._anim_job_padding = self.after(ANIMATION_INTERVAL_MS, lambda s=step+1: step_animation(s))
            else:
                if hasattr(button, '_anim_job_padding'):
                    del button._anim_job_padding
            
        step_animation(0)
    
    def _animate_font_size(self, button, target_size, steps, easing_func):
        button = self._resolve_button_widget(button)

        if not isinstance(button, ctk.CTkButton) or not hasattr(button, '_original_font_size'):
            return

        if hasattr(button, '_anim_job_font'):
            self.after_cancel(button._anim_job_font)

        current_font_obj = button.cget("font")
        
        if not isinstance(current_font_obj, ctk.CTkFont):
            return 
            
        base_family = current_font_obj.cget("family")
        base_weight = current_font_obj.cget("weight")
        start_size = current_font_obj.cget("size")
        
        if start_size == target_size:
            return

        def step_animation(step=0):
            t = step / steps
            eased_t = easing_func(t)
            
            current_size = int(start_size + (target_size - start_size) * eased_t)
            
            new_font = ctk.CTkFont(family=base_family, size=current_size, weight=base_weight)
            button.configure(font=new_font)
            
            if step < steps:
                button._anim_job_font = self.after(ANIMATION_INTERVAL_MS, lambda s=step+1: step_animation(s))
            else:
                final_font = ctk.CTkFont(family=base_family, size=target_size, weight=base_weight)
                button.configure(font=final_font)
                
                if hasattr(button, '_anim_job_font'):
                    del button._anim_job_font
            
        step_animation(0)
    
    def _animate_logo(self):
        pass
    
    def _animate_by_text(self):
        original_color = self.by_label.cget("text_color")
        
        def animate_step(step=0, total_steps=6):
            if step <= total_steps:
                t = step / total_steps
                eased = self._ease_out_expo(t)
                
                if step == 0:
                    self.by_label.configure(text_color="#303030")
                elif step < total_steps:
                    r, g, b = int(original_color[1:3], 16), int(original_color[3:5], 16), int(original_color[5:7], 16)
                    start_r, start_g, start_b = 48, 48, 48
                    current_r = int(start_r + (r - start_r) * eased)
                    current_g = int(start_g + (g - start_g) * eased)
                    current_b = int(start_b + (b - start_b) * eased)
                    self.by_label.configure(text_color=f"#{current_r:02x}{current_g:02x}{current_b:02x}")
                
                if step < total_steps:
                    self.after(15, lambda s=step+1: animate_step(s, total_steps))
                else:
                    self.by_label.configure(text_color=original_color)
        
        self.after(100, lambda: animate_step(0, 6))
    
    def _animate_github_icon(self):
        pass


if __name__ == "__main__":
    app = WinGoApp()
    app.mainloop()
