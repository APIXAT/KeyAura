import customtkinter as ctk
import pygame
import json
import os
import shutil
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import threading
import time

# Configure CustomTkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class KeyAura:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("KeyAura - Keyboard Sound Customizer")
        self.root.geometry("1400x900")
        self.root.minsize(1200, 800)
        
        # Initialize pygame mixer
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        
        # Application state
        self.sound_enabled = True
        self.current_template = None
        self.templates = {}
        self.key_sounds = {}
        self.template_dir = "templates"
        self.sounds_dir = "sounds"
        self.volume = 0.7
        
        # Create directories if they don't exist
        os.makedirs(self.template_dir, exist_ok=True)
        os.makedirs(self.sounds_dir, exist_ok=True)
        
        # Load existing templates
        self.load_templates()
        
        # Create UI
        self.create_ui()
        
    def create_ui(self):
        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Main container
        main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Top Bar
        self.create_top_bar(main_frame)
        
        # Content Area
        content_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        content_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        
        # Left Panel - Keyboard and Sound Customization
        left_panel = ctk.CTkFrame(content_frame, fg_color="transparent")
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        left_panel.grid_columnconfigure(0, weight=1)
        
        # Right Panel - Template Management
        right_panel = ctk.CTkFrame(content_frame, fg_color="transparent")
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        right_panel.grid_columnconfigure(0, weight=1)
        right_panel.grid_rowconfigure(1, weight=1)
        
        # Create sections
        self.create_keyboard_layout(left_panel)
        self.create_sound_customization(left_panel)
        self.create_template_management(right_panel)
        
    def create_top_bar(self, parent):
        top_frame = ctk.CTkFrame(parent, height=70, fg_color="#1a1a1a", corner_radius=15)
        top_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        top_frame.grid_columnconfigure(1, weight=1)
        top_frame.grid_propagate(False)
        
        # Title with icon
        title_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        title_frame.grid(row=0, column=0, padx=20, pady=15)
        
        title_label = ctk.CTkLabel(
            title_frame, 
            text="🎹 KeyAura", 
            font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
            text_color="#00ff88"
        )
        title_label.pack()
        
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text="Keyboard Sound Customizer",
            font=ctk.CTkFont(size=12),
            text_color="#888888"
        )
        subtitle_label.pack()
        
        # Control buttons frame
        controls_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        controls_frame.grid(row=0, column=2, padx=20, pady=15)
        
        # Volume control
        volume_frame = ctk.CTkFrame(controls_frame, fg_color="transparent")
        volume_frame.pack(side="left", padx=(0, 15))
        
        volume_label = ctk.CTkLabel(volume_frame, text="🔊", font=ctk.CTkFont(size=16))
        volume_label.pack(side="left", padx=(0, 5))
        
        self.volume_slider = ctk.CTkSlider(
            volume_frame,
            from_=0,
            to=1,
            number_of_steps=100,
            command=self.set_volume,
            width=100
        )
        self.volume_slider.set(self.volume)
        self.volume_slider.pack(side="left")
        
        # Sound Toggle Button
        self.sound_button = ctk.CTkButton(
            controls_frame,
            text="🔊",
            width=50,
            height=40,
            command=self.toggle_sound,
            fg_color="#2d2d2d",
            hover_color="#3d3d3d",
            corner_radius=10
        )
        self.sound_button.pack(side="left", padx=(15, 10))
        
        # Add Template Button
        add_template_btn = ctk.CTkButton(
            controls_frame,
            text="🎧 Add Template",
            width=130,
            height=40,
            command=self.add_template,
            fg_color="#4a90e2",
            hover_color="#357abd",
            corner_radius=10
        )
        add_template_btn.pack(side="left", padx=10)
        
        # Templates Button
        templates_btn = ctk.CTkButton(
            controls_frame,
            text="🧩 Templates",
            width=110,
            height=40,
            command=self.show_templates,
            fg_color="#9b59b6",
            hover_color="#8e44ad",
            corner_radius=10
        )
        templates_btn.pack(side="left", padx=10)
        
    def create_keyboard_layout(self, parent):
        keyboard_frame = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        keyboard_frame.pack(fill="x", pady=(0, 20))
        
        # Keyboard Layout Title
        layout_title = ctk.CTkLabel(
            keyboard_frame,
            text="⌨️ Virtual Keyboard",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#ffffff"
        )
        layout_title.pack(pady=(20, 15))
        
        # Layout Type Selector
        layout_frame = ctk.CTkFrame(keyboard_frame, fg_color="transparent")
        layout_frame.pack(pady=(0, 20))
        
        layout_label = ctk.CTkLabel(layout_frame, text="Layout:", text_color="#cccccc", font=ctk.CTkFont(size=14))
        layout_label.pack(side="left", padx=(0, 10))
        
        self.layout_var = ctk.StringVar(value="100%")
        layout_menu = ctk.CTkOptionMenu(
            layout_frame,
            values=["67%", "75%", "100%"],
            variable=self.layout_var,
            command=self.change_layout,
            fg_color="#2d2d2d",
            button_color="#4a90e2",
            button_hover_color="#357abd",
            width=100
        )
        layout_menu.pack(side="left")
        
        # Keyboard Keys
        self.create_keyboard_keys(keyboard_frame)
        
    def create_keyboard_keys(self, parent):
        # Define key rows with proper spacing
        key_rows = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"]
        ]
        
        keys_frame = ctk.CTkFrame(parent, fg_color="transparent")
        keys_frame.pack(pady=(0, 25))
        
        self.key_buttons = {}
        
        for row_idx, row in enumerate(key_rows):
            row_frame = ctk.CTkFrame(keys_frame, fg_color="transparent")
            row_frame.pack(pady=8)
            
            # Add offset for second and third rows
            if row_idx == 1:
                offset_frame = ctk.CTkFrame(row_frame, fg_color="transparent", width=25)
                offset_frame.pack(side="left")
            elif row_idx == 2:
                offset_frame = ctk.CTkFrame(row_frame, fg_color="transparent", width=50)
                offset_frame.pack(side="left")
            
            for key in row:
                key_btn = ctk.CTkButton(
                    row_frame,
                    text=key,
                    width=55,
                    height=55,
                    command=lambda k=key: self.play_key_sound(k),
                    fg_color="#2d2d2d",
                    hover_color="#4a90e2",
                    corner_radius=12,
                    font=ctk.CTkFont(size=18, weight="bold"),
                    border_width=2,
                    border_color="#3d3d3d"
                )
                key_btn.pack(side="left", padx=4)
                self.key_buttons[key] = key_btn
                
    def create_sound_customization(self, parent):
        sound_frame = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        sound_frame.pack(fill="x")
        
        # Section Title
        sound_title = ctk.CTkLabel(
            sound_frame,
            text="🔊 Sound Customization",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#ffffff"
        )
        sound_title.pack(pady=(20, 15))
        
        # Sound Controls
        controls_frame = ctk.CTkFrame(sound_frame, fg_color="transparent")
        controls_frame.pack(pady=(0, 20), padx=20, fill="x")
        
        # Key Selection
        key_label = ctk.CTkLabel(controls_frame, text="Select Key:", text_color="#cccccc", font=ctk.CTkFont(size=14))
        key_label.pack(side="left", padx=(0, 10))
        
        self.key_var = ctk.StringVar(value="A")
        key_menu = ctk.CTkOptionMenu(
            controls_frame,
            values=list(self.key_buttons.keys()),
            variable=self.key_var,
            command=self.on_key_selected,
            fg_color="#2d2d2d",
            button_color="#4a90e2",
            button_hover_color="#357abd",
            width=80
        )
        key_menu.pack(side="left", padx=(0, 20))
        
        # Sound File Selection
        self.sound_path_var = ctk.StringVar()
        sound_entry = ctk.CTkEntry(
            controls_frame,
            textvariable=self.sound_path_var,
            placeholder_text="Select sound file...",
            width=350,
            fg_color="#2d2d2d",
            border_color="#4a90e2",
            height=35
        )
        sound_entry.pack(side="left", padx=(0, 10))
        
        browse_btn = ctk.CTkButton(
            controls_frame,
            text="Browse",
            width=80,
            command=self.browse_sound_file,
            fg_color="#4a90e2",
            hover_color="#357abd",
            corner_radius=8,
            height=35
        )
        browse_btn.pack(side="left", padx=(0, 10))
        
        preview_btn = ctk.CTkButton(
            controls_frame,
            text="Preview",
            width=80,
            command=self.preview_sound,
            fg_color="#27ae60",
            hover_color="#229954",
            corner_radius=8,
            height=35
        )
        preview_btn.pack(side="left")
        
        # Apply buttons frame
        apply_frame = ctk.CTkFrame(sound_frame, fg_color="transparent")
        apply_frame.pack(pady=(0, 20), padx=20, fill="x")
        
        # Apply to all keys checkbox
        self.apply_all_var = ctk.BooleanVar()
        apply_all_check = ctk.CTkCheckBox(
            apply_frame,
            text="Apply to all keys (A-Z)",
            variable=self.apply_all_var,
            fg_color="#4a90e2",
            hover_color="#357abd",
            text_color="#cccccc",
            font=ctk.CTkFont(size=14)
        )
        apply_all_check.pack(side="left", padx=(0, 20))
        
        # Apply button
        apply_btn = ctk.CTkButton(
            apply_frame,
            text="Apply Sound",
            width=120,
            command=self.apply_sound,
            fg_color="#27ae60",
            hover_color="#229954",
            corner_radius=8,
            height=35
        )
        apply_btn.pack(side="left")
        
        # Clear button
        clear_btn = ctk.CTkButton(
            apply_frame,
            text="Clear Sound",
            width=120,
            command=self.clear_sound,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            corner_radius=8,
            height=35
        )
        clear_btn.pack(side="left", padx=(10, 0))
        
    def create_template_management(self, parent):
        template_frame = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        template_frame.pack(fill="both", expand=True)
        template_frame.grid_columnconfigure(0, weight=1)
        template_frame.grid_rowconfigure(1, weight=1)
        
        # Section Title
        template_title = ctk.CTkLabel(
            template_frame,
            text="📁 Template Management",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#ffffff"
        )
        template_title.grid(row=0, column=0, pady=(20, 15))
        
        # Templates List
        self.templates_list_frame = ctk.CTkScrollableFrame(
            template_frame,
            fg_color="transparent",
            height=400
        )
        self.templates_list_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 20))
        
        self.refresh_templates_list()
        
    def set_volume(self, value):
        self.volume = float(value)
        pygame.mixer.music.set_volume(self.volume)
        
    def toggle_sound(self):
        self.sound_enabled = not self.sound_enabled
        if self.sound_enabled:
            self.sound_button.configure(text="🔊")
        else:
            self.sound_button.configure(text="🔇")
            
    def change_layout(self, layout_type):
        # This would implement different keyboard layouts
        print(f"Layout changed to: {layout_type}")
        
    def play_key_sound(self, key):
        if not self.sound_enabled:
            return
            
        if key in self.key_sounds and self.key_sounds[key]:
            try:
                # Stop any currently playing sound
                pygame.mixer.music.stop()
                pygame.mixer.music.load(self.key_sounds[key])
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play()
                
                # Visual feedback
                self.key_buttons[key].configure(fg_color="#4a90e2")
                self.root.after(100, lambda: self.key_buttons[key].configure(fg_color="#2d2d2d"))
                
            except Exception as e:
                print(f"Error playing sound for key {key}: {e}")
                messagebox.showerror("Error", f"Could not play sound for key {key}: {e}")
                
    def on_key_selected(self, key):
        if key in self.key_sounds:
            self.sound_path_var.set(self.key_sounds[key])
        else:
            self.sound_path_var.set("")
            
    def browse_sound_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Sound File",
            filetypes=[("Audio files", "*.mp3 *.wav *.ogg"), ("All files", "*.*")]
        )
        if file_path:
            self.sound_path_var.set(file_path)
            
    def preview_sound(self):
        sound_path = self.sound_path_var.get()
        if sound_path and os.path.exists(sound_path):
            try:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(sound_path)
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play()
            except Exception as e:
                messagebox.showerror("Error", f"Could not play sound: {e}")
        else:
            messagebox.showwarning("Warning", "Please select a valid sound file first.")
            
    def apply_sound(self):
        sound_path = self.sound_path_var.get()
        selected_key = self.key_var.get()
        
        if not sound_path or not os.path.exists(sound_path):
            messagebox.showwarning("Warning", "Please select a valid sound file first.")
            return
            
        if self.apply_all_var.get():
            # Apply to all A-Z keys
            for key in self.key_buttons.keys():
                self.key_sounds[key] = sound_path
        else:
            # Apply to selected key only
            self.key_sounds[selected_key] = sound_path
            
        messagebox.showinfo("Success", "Sound applied successfully!")
        
    def clear_sound(self):
        selected_key = self.key_var.get()
        
        if self.apply_all_var.get():
            # Clear all A-Z keys
            for key in self.key_buttons.keys():
                if key in self.key_sounds:
                    del self.key_sounds[key]
        else:
            # Clear selected key only
            if selected_key in self.key_sounds:
                del self.key_sounds[selected_key]
                
        self.sound_path_var.set("")
        messagebox.showinfo("Success", "Sound cleared successfully!")
            
    def add_template(self):
        template_name = ctk.CTkInputDialog(
            text="Enter template name:",
            title="Add Template"
        ).get_input()
        
        if template_name:
            # Save current key sounds as template
            template_data = {
                "name": template_name,
                "key_sounds": self.key_sounds.copy(),
                "layout": self.layout_var.get(),
                "created": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            template_file = os.path.join(self.template_dir, f"{template_name}.json")
            with open(template_file, 'w') as f:
                json.dump(template_data, f, indent=2)
                
            self.templates[template_name] = template_data
            self.refresh_templates_list()
            messagebox.showinfo("Success", f"Template '{template_name}' saved successfully!")
            
    def show_templates(self):
        # This would show a detailed template view
        pass
        
    def load_templates(self):
        if os.path.exists(self.template_dir):
            for filename in os.listdir(self.template_dir):
                if filename.endswith('.json'):
                    template_path = os.path.join(self.template_dir, filename)
                    try:
                        with open(template_path, 'r') as f:
                            template_data = json.load(f)
                            self.templates[template_data['name']] = template_data
                    except Exception as e:
                        print(f"Error loading template {filename}: {e}")
                        
    def refresh_templates_list(self):
        # Clear existing widgets
        for widget in self.templates_list_frame.winfo_children():
            widget.destroy()
            
        # Add template cards
        for template_name, template_data in self.templates.items():
            self.create_template_card(template_name, template_data)
            
    def create_template_card(self, template_name, template_data):
        card_frame = ctk.CTkFrame(
            self.templates_list_frame,
            fg_color="#2d2d2d",
            corner_radius=12,
            border_width=2,
            border_color="#3d3d3d"
        )
        card_frame.pack(fill="x", pady=8, padx=10)
        
        # Template info
        info_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=15, pady=12)
        
        name_label = ctk.CTkLabel(
            info_frame,
            text=template_name,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#ffffff"
        )
        name_label.pack(anchor="w")
        
        created_label = ctk.CTkLabel(
            info_frame,
            text=f"Created: {template_data.get('created', 'Unknown')}",
            font=ctk.CTkFont(size=12),
            text_color="#cccccc"
        )
        created_label.pack(anchor="w")
        
        layout_label = ctk.CTkLabel(
            info_frame,
            text=f"Layout: {template_data.get('layout', '100%')}",
            font=ctk.CTkFont(size=12),
            text_color="#888888"
        )
        layout_label.pack(anchor="w")
        
        # Action buttons
        buttons_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
        buttons_frame.pack(side="right", padx=15, pady=12)
        
        use_btn = ctk.CTkButton(
            buttons_frame,
            text="Use",
            width=60,
            command=lambda: self.use_template(template_name),
            fg_color="#27ae60",
            hover_color="#229954",
            corner_radius=8,
            height=30
        )
        use_btn.pack(side="left", padx=2)
        
        edit_btn = ctk.CTkButton(
            buttons_frame,
            text="Edit",
            width=60,
            command=lambda: self.edit_template(template_name),
            fg_color="#f39c12",
            hover_color="#e67e22",
            corner_radius=8,
            height=30
        )
        edit_btn.pack(side="left", padx=2)
        
        delete_btn = ctk.CTkButton(
            buttons_frame,
            text="Delete",
            width=60,
            command=lambda: self.delete_template(template_name),
            fg_color="#e74c3c",
            hover_color="#c0392b",
            corner_radius=8,
            height=30
        )
        delete_btn.pack(side="left", padx=2)
        
    def use_template(self, template_name):
        if template_name in self.templates:
            template_data = self.templates[template_name]
            self.key_sounds = template_data['key_sounds'].copy()
            self.layout_var.set(template_data.get('layout', '100%'))
            self.current_template = template_name
            messagebox.showinfo("Success", f"Template '{template_name}' loaded successfully!")
            
    def edit_template(self, template_name):
        # This would open an edit dialog
        messagebox.showinfo("Info", f"Edit functionality for '{template_name}' would be implemented here.")
        
    def delete_template(self, template_name):
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete template '{template_name}'?"):
            template_file = os.path.join(self.template_dir, f"{template_name}.json")
            if os.path.exists(template_file):
                os.remove(template_file)
            if template_name in self.templates:
                del self.templates[template_name]
            self.refresh_templates_list()
            messagebox.showinfo("Success", f"Template '{template_name}' deleted successfully!")
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = KeyAura()
    app.run() 