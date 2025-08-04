# KeyAura 🎹

A modern, dark-themed interactive desktop application for customizing keyboard sound effects and managing sound templates with advanced multi-key selection capabilities and a complete virtual keyboard.

## Features ✨

### 🎨 Modern Dark Theme
- Sleek, dark interface with neon accents
- Smooth animations and hover effects
- Responsive design that adapts to different screen sizes

### ⌨️ Complete Interactive Virtual Keyboard
- **Full QWERTY Layout**: Complete keyboard with Q-Z, A-L, Z-M keys
- **NEW: Additional Keys**: Space, Enter, Shift, and Ctrl keys
- **Multiple Layout Options**: 67%, 75%, and 100% keyboard layouts
- **Rounded, Modern Design**: Buttons with shadow effects and smooth animations
- **NEW: Ctrl+Click Multi-Key Selection** with real-time visual feedback
- **Responsive Layout**: Buttons maintain size and position when resizing window
- **Dynamic Sizing**: Different button sizes for different key types (Space/Enter are wider)

### 🎯 Advanced Key Selection System
- **Single Key Selection**: Click any key to select it individually
- **Ctrl+Click Multi-Selection**: Hold Ctrl and click multiple keys to select them as a group
- **Mixed Key Types**: Select combinations of letters, Space, Enter, Shift, and Ctrl
- **Visual Feedback**: Selected keys highlight in green (#00ff88) with glowing borders
- **Real-time Display**: Selected keys are shown in the customization panel
- **Toggle Selection**: Ctrl+click again to deselect individual keys
- **Dynamic Updates**: Selection display updates instantly as you select/deselect keys

### 🔊 Enhanced Sound Customization
- **Individual Key Assignment**: Assign unique sounds to specific keys
- **Group Sound Assignment**: Apply the same sound to multiple selected keys
- **Mixed Key Types**: Assign sounds to combinations of letters and special keys
- **Bulk Operations**: Apply sounds to all keys or clear selected keys
- **Sound Preview**: Test sounds before applying them
- **Multiple Formats**: Support for MP3, WAV, and OGG audio files
- **Volume Control**: Real-time volume adjustment with slider
- **Global Toggle**: Enable/disable all sounds with one click

### 📁 Template Management System
- **Save Configurations**: Save current key sounds and layout as templates
- **Load Templates**: Quickly switch between different sound configurations
- **Template Cards**: Visual cards showing template name, creation date, and layout
- **CRUD Operations**: Create, Read, Update, and Delete templates
- **JSON Storage**: Templates stored as human-readable JSON files
- **Auto-loading**: Templates automatically load on application startup

### 🎧 Template Features
- **Customizable Template Names**: Create descriptive template names
- **Keyboard Layout Preservation**: Layout settings saved with templates
- **Easy Template Switching**: Instant template loading and application
- **Template Preview and Management**: Visual template organization

## Installation 🚀

### Prerequisites
- Python 3.11 or higher
- Windows 10/11 (tested on Windows 10.0.26100)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd KeyAura
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage Guide 📖

### Getting Started
1. Launch KeyAura
2. The application will create `templates/` and `sounds/` directories automatically
3. Start customizing your keyboard sounds!

### 🎯 Multi-Key Selection (NEW!)

#### Single Key Selection
1. **Click any key** on the virtual keyboard (letters, Space, Enter, Shift, Ctrl)
2. The key will **highlight in green** to show it's selected
3. The selected key appears in the customization panel

#### Multi-Key Selection
1. **Hold Ctrl** and click multiple keys (mix different key types)
2. **Selected keys highlight in green** with glowing borders
3. **Real-time display** shows all selected keys
4. **Ctrl+click again** to deselect individual keys

### 🔊 Enhanced Sound Customization

#### Individual Key Assignment
1. **Select a key** (single click or Ctrl+click)
2. **Browse** for an audio file (MP3, WAV, or OGG)
3. **Preview** the sound to ensure it's correct
4. **Click "Apply to Selected Keys"**

#### Multi-Key Sound Assignment
1. **Use Ctrl+Click** to select multiple keys (including Space, Enter, Shift, Ctrl)
2. **Browse** for a sound file
3. **Click "Apply to Selected Keys"** to assign the same sound to all selected keys

#### Bulk Operations
- **"Apply to All Keys"**: Assign the same sound to every key (including new keys)
- **"Clear Selected"**: Remove sounds from selected keys only
- **"Preview"**: Test sounds before applying them

### Creating Templates
1. Customize your key sounds using the enhanced selection features
2. Click **"🎧 Add Template"** in the top bar
3. Enter a template name (e.g., "Mechanical Vibes", "Hacker Mode")
4. Your current sound configuration will be saved

### Managing Templates
- **Use**: Load a template's sound configuration
- **Edit**: Modify template settings (coming soon)
- **Delete**: Remove templates from your collection

### Keyboard Layouts
- Choose between 67%, 75%, and 100% layouts
- Layout changes are saved with templates

## File Structure 📁

```
KeyAura/
├── main.py                 # Main application with complete features
├── enhanced_main.py        # Alternative enhanced version
├── demo_complete.py        # Complete demo showcasing all features
├── demo_enhanced.py        # Demo for enhanced features
├── launcher.py            # Dependency checker and launcher
├── demo.py                # Basic demo script
├── requirements.txt       # Python dependencies
├── config.json           # Application configuration
├── run_keyaura.bat       # Windows launcher
├── README.md             # This file
├── INSTALL.md            # Installation guide
├── QUICK_START.md        # Quick start guide
├── FEATURES.md           # Complete features overview
├── sample_template.json  # Example template
├── templates/            # Template storage (auto-created)
└── sounds/              # Sound file storage (auto-created)
```

## Dependencies 📦

- **customtkinter**: Modern UI framework
- **pygame**: Audio playback and mixing
- **Pillow**: Image processing (for future features)

## Technical Details 🔧

### Audio Support
- **Formats**: MP3, WAV, OGG
- **Engine**: pygame.mixer
- **Features**: Real-time playback, volume control

### Data Storage
- **Templates**: JSON files in `templates/` directory
- **Structure**: Template name, key sounds, layout, creation date
- **Persistence**: Automatic loading on startup

### UI Framework
- **Framework**: CustomTkinter
- **Theme**: Dark mode with custom color palette
- **Responsive**: Adapts to window resizing with grid layout

### 🎯 New Multi-Key Selection System
- **Ctrl Key Detection**: Real-time keyboard event monitoring
- **Visual Feedback**: Dynamic color changes and borders
- **State Management**: Efficient tracking of selected keys
- **Smooth Animations**: Fluid transitions and hover effects

### 📐 Enhanced Layout System
- **Grid-based Layout**: Responsive design using CustomTkinter grid
- **Dynamic Resizing**: Buttons maintain size and position when window is resized
- **Proportional Panels**: Left panel (2/3 width), Right panel (1/3 width)
- **Improved Spacing**: Better padding, margins, and visual hierarchy

## Color Palette 🎨

- **Primary Background**: #1a1a1a (Dark Gray)
- **Secondary Background**: #2d2d2d (Medium Gray)
- **Accent Blue**: #4a90e2 (Primary Action)
- **Accent Green**: #27ae60 (Success Actions)
- **Accent Orange**: #f39c12 (Warning Actions)
- **Accent Red**: #e74c3c (Delete Actions)
- **Accent Purple**: #9b59b6 (Template Actions)
- **Text Primary**: #ffffff (White)
- **Text Secondary**: #cccccc (Light Gray)
- **Brand Color**: #00ff88 (Neon Green)
- **Selection Color**: #00ff88 (Green for selected keys)

## 🆕 New Features in This Version

### ⌨️ Complete Virtual Keyboard
- **30 Total Keys**: 26 letters + Space, Enter, Shift, Ctrl
- **Dynamic Button Sizing**: Space/Enter are wider, Shift/Ctrl are medium-sized
- **Professional Layout**: Proper keyboard spacing and alignment
- **Mixed Key Types**: Support for letters and special keys

### 🎯 Enhanced Multi-Key Selection
- **Mixed Key Selection**: Select combinations of letters and special keys
- **Real-time Visual Feedback** with green highlighting
- **Dynamic Selection Display** in the customization panel
- **Toggle Selection** by Ctrl+clicking again

### 🔊 Complete Sound Management
- **All Key Types**: Assign sounds to letters, Space, Enter, Shift, Ctrl
- **Apply to Selected Keys** button for group operations
- **Apply to All Keys** for bulk assignment (including new keys)
- **Clear Selected** for removing sounds from specific keys
- **Improved Preview** functionality with volume control

### ✨ Enhanced Visual Design
- **Larger Window**: 1600x1000 default size for better usability
- **Improved Proportions**: 2:1 left/right panel ratio
- **Better Typography**: Larger fonts and improved readability
- **Enhanced Spacing**: More professional padding and margins
- **Responsive Layout**: Maintains button sizes during window resizing

### 📁 Advanced Template Management
- **Complete Key Support**: Templates include all 30 keys
- **Enhanced Template Cards** with more information
- **Improved Layout** for better organization
- **Better Visual Feedback** for template operations

## Future Enhancements 🚀

- [ ] Template editing interface
- [ ] Sound volume control per key
- [ ] Keyboard layout customization
- [ ] Sound effect categories
- [ ] Import/export template collections
- [ ] Real-time keyboard input detection
- [ ] Sound visualization
- [ ] Multiple sound profiles per template
- [ ] **NEW: Drag and drop key selection**
- [ ] **NEW: Keyboard shortcuts for common actions**
- [ ] **NEW: Additional special keys (Backspace, Tab, etc.)**

## Troubleshooting 🔧

### Common Issues

**Audio not playing:**
- Ensure audio files are in supported formats (MP3, WAV, OGG)
- Check system audio settings
- Verify pygame installation

**Template not loading:**
- Check file permissions in `templates/` directory
- Ensure JSON files are not corrupted
- Restart the application

**UI not displaying correctly:**
- Update CustomTkinter: `pip install --upgrade customtkinter`
- Check Python version (requires 3.11+)
- Verify all dependencies are installed

**Multi-key selection not working:**
- Ensure you're holding Ctrl while clicking
- Check that the application window has focus
- Try clicking the keys in sequence

**Window resizing issues:**
- Ensure minimum window size (1400x900)
- Check that all UI elements are properly configured
- Restart the application if layout becomes corrupted

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License 📄

This project is open source and available under the MIT License.

## Support 💬

For issues, questions, or feature requests, please open an issue on the repository.

---


**KeyAura** - Transform your typing experience with custom keyboard sounds and a complete virtual keyboard! ✨ 
