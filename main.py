import customtkinter as ctk
import pygame
import json
import os
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
        self.root.title("KeyAura - Interactive Keyboard Sound Customizer")
        self.root.geometry("1600x1000")
        self.root.minsize(1400, 900)
        
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
        
        # Multi-key selection state
        self.selected_keys = set()
        self.ctrl_pressed = False
        
        # Create directories if they don't exist
        os.makedirs(self.template_dir, exist_ok=True)
        os.makedirs(self.sounds_dir, exist_ok=True)
        
        # Load existing templates
        self.load_templates()
        
        # Bind keyboard events for Ctrl key detection
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.bind('<KeyRelease>', self.on_key_release)
        
        # Create UI
        self.create_ui()
        
    def create_ui(self):
        # Configure grid weights for responsive layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Main container
        main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Top Bar
        self.create_top_bar(main_frame)
        
        # Content Area with responsive layout
        content_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        content_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))
        content_frame.grid_columnconfigure(0, weight=2)  # Left panel gets more space
        content_frame.grid_columnconfigure(1, weight=1)  # Right panel
        content_frame.grid_rowconfigure(0, weight=1)
        
        # Left Panel - Keyboard and Sound Customization
        left_panel = ctk.CTkFrame(content_frame, fg_color="transparent")
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        left_panel.grid_columnconfigure(0, weight=1)
        left_panel.grid_rowconfigure(1, weight=1)
        
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
        top_frame = ctk.CTkFrame(parent, height=80, fg_color="#1a1a1a", corner_radius=15)
        top_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        top_frame.grid_columnconfigure(1, weight=1)
        top_frame.grid_propagate(False)
        
        # Title with icon
        title_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        title_frame.grid(row=0, column=0, padx=20, pady=15)
        
        title_label = ctk.CTkLabel(
            title_frame, 
            text="🎹 KeyAura", 
            font=ctk.CTkFont(family="Arial", size=36, weight="bold"),
            text_color="#00ff88"
        )
        title_label.pack()
        
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text="Interactive Keyboard Sound Customizer",
            font=ctk.CTkFont(size=14),
            text_color="#888888"
        )
        subtitle_label.pack()
        
        # Control buttons frame
        controls_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
        controls_frame.grid(row=0, column=2, padx=20, pady=15)
        
        # Volume control
        volume_frame = ctk.CTkFrame(controls_frame, fg_color="transparent")
        volume_frame.pack(side="left", padx=(0, 15))
        
        volume_label = ctk.CTkLabel(volume_frame, text="🔊", font=ctk.CTkFont(size=18))
        volume_label.pack(side="left", padx=(0, 5))
        
        self.volume_slider = ctk.CTkSlider(
            volume_frame,
            from_=0,
            to=1,
            number_of_steps=100,
            command=self.set_volume,
            width=120
        )
        self.volume_slider.set(self.volume)
        self.volume_slider.pack(side="left")
        
        # Sound Toggle Button
        self.sound_button = ctk.CTkButton(
            controls_frame,
            text="🔊",
            width=60,
            height=45,
            command=self.toggle_sound,
            fg_color="#2d2d2d",
            hover_color="#3d3d3d",
            corner_radius=12
        )
        self.sound_button.pack(side="left", padx=(15, 10))
        
        # Add Template Button
        add_template_btn = ctk.CTkButton(
            controls_frame,
            text="🎧 Add Template",
            width=140,
            height=45,
            command=self.add_template,
            fg_color="#4a90e2",
            hover_color="#357abd",
            corner_radius=12
        )
        add_template_btn.pack(side="left", padx=10)
        
        # Templates Button
        templates_btn = ctk.CTkButton(
            controls_frame,
            text="🧩 Templates",
            width=120,
            height=45,
            command=self.show_templates,
            fg_color="#9b59b6",
            hover_color="#8e44ad",
            corner_radius=12
        )
        templates_btn.pack(side="left", padx=10)
        
    def create_keyboard_layout(self, parent):
        keyboard_frame = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        keyboard_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        keyboard_frame.grid_columnconfigure(0, weight=1)
        
        # Keyboard Layout Title
        layout_title = ctk.CTkLabel(
            keyboard_frame,
            text="⌨️ Interactive Virtual Keyboard",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#ffffff"
        )
        layout_title.grid(row=0, column=0, pady=(20, 10))
        
        # Instructions for multi-key selection
        instructions_label = ctk.CTkLabel(
            keyboard_frame,
            text="💡 Hold Ctrl and click multiple keys to select them as a group",
            font=ctk.CTkFont(size=13),
            text_color="#00ff88"
        )
        instructions_label.grid(row=1, column=0, pady=(0, 15))
        
        # Layout Type Selector
        layout_frame = ctk.CTkFrame(keyboard_frame, fg_color="transparent")
        layout_frame.grid(row=2, column=0, pady=(0, 20))
        
        layout_label = ctk.CTkLabel(layout_frame, text="Layout:", text_color="#cccccc", font=ctk.CTkFont(size=15))
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
            width=120,
            height=35
        )
        layout_menu.pack(side="left")
        
        # Keyboard Keys Container
        keys_container = ctk.CTkFrame(keyboard_frame, fg_color="transparent")
        keys_container.grid(row=3, column=0, pady=(0, 25), sticky="ew")
        keys_container.grid_columnconfigure(0, weight=1)
        
        # Keyboard Keys
        self.create_keyboard_keys(keys_container)
        
    def create_keyboard_keys(self, parent):
        # Define key rows with proper spacing and additional keys
        key_rows = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Shift", "Z", "X", "C", "V", "B", "N", "M", "Shift"],
            ["Ctrl", "Space", "Enter", "Ctrl"]
        ]
        
        # Create main keys frame
        keys_frame = ctk.CTkFrame(parent, fg_color="transparent")
        keys_frame.pack(pady=10, fill="x")
        
        self.key_buttons = {}
        
        for row_idx, row in enumerate(key_rows):
            row_frame = ctk.CTkFrame(keys_frame, fg_color="transparent")
            row_frame.pack(pady=8, fill="x")
            
            # Add offset for second and third rows
            if row_idx == 1:
                offset_frame = ctk.CTkFrame(row_frame, fg_color="transparent", width=30)
                offset_frame.pack(side="left")
            elif row_idx == 2:
                offset_frame = ctk.CTkFrame(row_frame, fg_color="transparent", width=60)
                offset_frame.pack(side="left")
            elif row_idx == 3:
                offset_frame = ctk.CTkFrame(row_frame, fg_color="transparent", width=90)
                offset_frame.pack(side="left")
            
            for key in row:
                # Determine button size based on key type
                if key in ["Space", "Enter"]:
                    width, height = 120, 55
                elif key in ["Shift", "Ctrl"]:
                    width, height = 80, 55
                else:
                    width, height = 55, 55
                
                key_btn = ctk.CTkButton(
                    row_frame,
                    text=key,
                    width=width,
                    height=height,
                    command=lambda k=key: self.on_key_click(k),
                    fg_color="#2d2d2d",
                    hover_color="#4a90e2",
                    corner_radius=12,
                    font=ctk.CTkFont(size=16, weight="bold"),
                    border_width=2,
                    border_color="#3d3d3d"
                )
                key_btn.pack(side="left", padx=4)
                self.key_buttons[key] = key_btn
                
    def create_sound_customization(self, parent):
        sound_frame = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        sound_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 20))
        sound_frame.grid_columnconfigure(0, weight=1)
        sound_frame.grid_rowconfigure(3, weight=1)
        
        # Section Title
        sound_title = ctk.CTkLabel(
            sound_frame,
            text="🔊 Sound Customization",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#ffffff"
        )
        sound_title.grid(row=0, column=0, pady=(20, 15), sticky="w", padx=20)
        
        # Selected Keys Display
        self.selected_keys_label = ctk.CTkLabel(
            sound_frame,
            text="No keys selected",
            font=ctk.CTkFont(size=15),
            text_color="#888888"
        )
        self.selected_keys_label.grid(row=1, column=0, pady=(0, 15), sticky="w", padx=20)
        
        # Sound Controls
        controls_frame = ctk.CTkFrame(sound_frame, fg_color="transparent")
        controls_frame.grid(row=2, column=0, pady=(0, 20), padx=20, sticky="ew")
        controls_frame.grid_columnconfigure(1, weight=1)
        
        # Sound File Selection
        self.sound_path_var = ctk.StringVar()
        sound_entry = ctk.CTkEntry(
            controls_frame,
            textvariable=self.sound_path_var,
            placeholder_text="Select sound file...",
            fg_color="#2d2d2d",
            border_color="#4a90e2",
            height=40,
            font=ctk.CTkFont(size=14)
        )
        sound_entry.grid(row=0, column=0, columnspan=2, sticky="ew", padx=(0, 10))
        
        browse_btn = ctk.CTkButton(
            controls_frame,
            text="Browse",
            width=90,
            command=self.browse_sound_file,
            fg_color="#4a90e2",
            hover_color="#357abd",
            corner_radius=10,
            height=40
        )
        browse_btn.grid(row=0, column=2, padx=(0, 10))
        
        preview_btn = ctk.CTkButton(
            controls_frame,
            text="Preview",
            width=90,
            command=self.preview_sound,
            fg_color="#27ae60",
            hover_color="#229954",
            corner_radius=10,
            height=40
        )
        preview_btn.grid(row=0, column=3)
        
        # Apply buttons frame
        apply_frame = ctk.CTkFrame(sound_frame, fg_color="transparent")
        apply_frame.grid(row=3, column=0, pady=(0, 20), padx=20, sticky="ew")
        
        # Apply to selected keys button
        apply_selected_btn = ctk.CTkButton(
            apply_frame,
            text="Apply to Selected Keys",
            width=160,
            command=self.apply_sound_to_selected,
            fg_color="#27ae60",
            hover_color="#229954",
            corner_radius=10,
            height=40
        )
        apply_selected_btn.pack(side="left", padx=(0, 10))
        
        # Apply to all keys button
        apply_all_btn = ctk.CTkButton(
            apply_frame,
            text="Apply to All Keys",
            width=130,
            command=self.apply_sound_to_all,
            fg_color="#f39c12",
            hover_color="#e67e22",
            corner_radius=10,
            height=40
        )
        apply_all_btn.pack(side="left", padx=(0, 10))
        
        # Clear selected button
        clear_selected_btn = ctk.CTkButton(
            apply_frame,
            text="Clear Selected",
            width=130,
            command=self.clear_selected_sounds,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            corner_radius=10,
            height=40
        )
        clear_selected_btn.pack(side="left")
        
    def create_template_management(self, parent):
        template_frame = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        template_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 20))
        template_frame.grid_columnconfigure(0, weight=1)
        template_frame.grid_rowconfigure(1, weight=1)
        
        # Section Title
        template_title = ctk.CTkLabel(
            template_frame,
            text="📁 Template Management",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#ffffff"
        )
        template_title.grid(row=0, column=0, pady=(20, 15), sticky="w", padx=20)
        
        # Templates List
        self.templates_list_frame = ctk.CTkScrollableFrame(
            template_frame,
            fg_color="transparent",
            height=500
        )
        self.templates_list_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 20))
        
        self.refresh_templates_list()
        
    def on_key_press(self, event):
        """Handle key press events for Ctrl detection."""
        if event.keysym == 'Control_L' or event.keysym == 'Control_R':
            self.ctrl_pressed = True
            
    def on_key_release(self, event):
        """Handle key release events for Ctrl detection."""
        if event.keysym == 'Control_L' or event.keysym == 'Control_R':
            self.ctrl_pressed = False
            
    def on_key_click(self, key):
        """Handle key button clicks with Ctrl+Click multi-selection."""
        if self.ctrl_pressed:
            # Multi-key selection mode
            if key in self.selected_keys:
                self.selected_keys.remove(key)
                self.key_buttons[key].configure(
                    fg_color="#2d2d2d",
                    border_color="#3d3d3d"
                )
            else:
                self.selected_keys.add(key)
                self.key_buttons[key].configure(
                    fg_color="#00ff88",
                    border_color="#00ff88"
                )
        else:
            # Single key mode - clear selection and select only this key
            self.clear_key_selection()
            self.selected_keys.add(key)
            self.key_buttons[key].configure(
                fg_color="#00ff88",
                border_color="#00ff88"
            )
            
        # Update selected keys display
        self.update_selected_keys_display()
        
        # Play sound if available
        self.play_key_sound(key)
        
    def clear_key_selection(self):
        """Clear all key selections."""
        for key in self.selected_keys:
            if key in self.key_buttons:
                self.key_buttons[key].configure(
                    fg_color="#2d2d2d",
                    border_color="#3d3d3d"
                )
        self.selected_keys.clear()
        
    def update_selected_keys_display(self):
        """Update the display of selected keys."""
        if self.selected_keys:
            keys_text = ", ".join(sorted(self.selected_keys))
            self.selected_keys_label.configure(
                text=f"Selected keys: {keys_text}",
                text_color="#00ff88"
            )
        else:
            self.selected_keys_label.configure(
                text="No keys selected",
                text_color="#888888"
            )
            
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
                original_color = self.key_buttons[key].cget("fg_color")
                self.key_buttons[key].configure(fg_color="#4a90e2")
                self.root.after(100, lambda: self.key_buttons[key].configure(fg_color=original_color))
                
            except Exception as e:
                print(f"Error playing sound for key {key}: {e}")
                messagebox.showerror("Error", f"Could not play sound for key {key}: {e}")
                
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
            
    def apply_sound_to_selected(self):
        """Apply sound to selected keys."""
        if not self.selected_keys:
            messagebox.showwarning("Warning", "Please select keys first using Ctrl+Click.")
            return
            
        sound_path = self.sound_path_var.get()
        if not sound_path or not os.path.exists(sound_path):
            messagebox.showwarning("Warning", "Please select a valid sound file first.")
            return
            
        # Apply sound to all selected keys
        for key in self.selected_keys:
            self.key_sounds[key] = sound_path
            
        messagebox.showinfo("Success", f"Sound applied to {len(self.selected_keys)} selected keys!")
        
    def apply_sound_to_all(self):
        """Apply sound to all keys."""
        sound_path = self.sound_path_var.get()
        if not sound_path or not os.path.exists(sound_path):
            messagebox.showwarning("Warning", "Please select a valid sound file first.")
            return
            
        # Apply sound to all keys
        for key in self.key_buttons.keys():
            self.key_sounds[key] = sound_path
            
        messagebox.showinfo("Success", "Sound applied to all keys!")
        
    def clear_selected_sounds(self):
        """Clear sounds from selected keys."""
        if not self.selected_keys:
            messagebox.showwarning("Warning", "Please select keys first using Ctrl+Click.")
            return
            
        # Clear sounds from selected keys
        for key in self.selected_keys:
            if key in self.key_sounds:
                del self.key_sounds[key]
                
        messagebox.showinfo("Success", f"Cleared sounds from {len(self.selected_keys)} selected keys!")
            
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
            self.clear_key_selection()
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