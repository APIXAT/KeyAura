# KeyAura Installation Guide

This guide will help you install and set up KeyAura on your Windows system.

## Prerequisites

### System Requirements
- **Operating System**: Windows 10/11 (64-bit)
- **Python**: Version 3.11 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 100MB free space
- **Audio**: Working audio output device

### Required Software
1. **Python 3.11+**: Download from [python.org](https://www.python.org/downloads/)
2. **Git** (optional): For cloning the repository

## Installation Methods

### Method 1: Quick Start (Recommended)

1. **Download the project**
   - Download the KeyAura ZIP file
   - Extract it to a folder of your choice

2. **Run the launcher**
   - Double-click `run_keyaura.bat`
   - The launcher will automatically check dependencies and install them if needed

3. **Start using KeyAura**
   - The application will start automatically after dependencies are installed

### Method 2: Manual Installation

1. **Install Python**
   ```bash
   # Download and install Python 3.11+ from python.org
   # Make sure to check "Add Python to PATH" during installation
   ```

2. **Verify Python installation**
   ```bash
   python --version
   # Should show Python 3.11.x or higher
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   # or
   python launcher.py
   ```

### Method 3: Using the Launcher Script

1. **Open Command Prompt**
   - Press `Win + R`, type `cmd`, and press Enter

2. **Navigate to KeyAura directory**
   ```bash
   cd path\to\KeyAura
   ```

3. **Run the launcher**
   ```bash
   python launcher.py
   ```

## Troubleshooting

### Common Issues

#### Python Not Found
**Error**: `'python' is not recognized as an internal or external command`

**Solution**:
1. Reinstall Python and check "Add Python to PATH"
2. Or add Python manually to PATH:
   - Find Python installation path (usually `C:\Users\Username\AppData\Local\Programs\Python\Python311\`)
   - Add to PATH environment variable

#### Dependencies Installation Failed
**Error**: `Failed to install dependencies`

**Solution**:
1. Update pip: `python -m pip install --upgrade pip`
2. Install dependencies manually:
   ```bash
   pip install customtkinter==5.2.0
   pip install pygame==2.5.2
   pip install Pillow==10.0.1
   ```

#### Audio Issues
**Error**: `Could not play sound`

**Solution**:
1. Check system audio settings
2. Ensure audio files are in supported formats (MP3, WAV, OGG)
3. Try different audio files
4. Restart the application

#### Permission Errors
**Error**: `Permission denied` or `Access denied`

**Solution**:
1. Run Command Prompt as Administrator
2. Check folder permissions
3. Ensure antivirus isn't blocking the application

### Advanced Troubleshooting

#### Check Python Version
```bash
python --version
```

#### Check Installed Packages
```bash
pip list
```

#### Verify Audio System
```bash
python -c "import pygame; pygame.mixer.init(); print('Audio system OK')"
```

#### Test CustomTkinter
```bash
python -c "import customtkinter; print('CustomTkinter OK')"
```

## First Run Setup

1. **Launch KeyAura**
   - The application will create necessary directories automatically

2. **Add Sound Files**
   - Place your audio files in the `sounds/` directory
   - Supported formats: MP3, WAV, OGG

3. **Create Your First Template**
   - Customize key sounds
   - Click "🎧 Add Template" to save your configuration

4. **Test the Keyboard**
   - Click on virtual keyboard keys to test sounds
   - Use the volume slider to adjust audio levels

## File Structure

After installation, your KeyAura directory should look like this:

```
KeyAura/
├── main.py                 # Main application
├── enhanced_main.py        # Enhanced version
├── launcher.py            # Dependency checker and launcher
├── demo.py                # Demo script
├── requirements.txt       # Python dependencies
├── config.json           # Application configuration
├── run_keyaura.bat       # Windows launcher
├── README.md             # Documentation
├── INSTALL.md            # This file
├── templates/            # Template storage (auto-created)
└── sounds/              # Sound file storage (auto-created)
```

## Updating KeyAura

1. **Backup your templates**
   - Copy the `templates/` folder to a safe location

2. **Download new version**
   - Replace old files with new ones

3. **Restore templates**
   - Copy your templates back to the `templates/` folder

## Uninstalling

1. **Remove the KeyAura folder**
   - Delete the entire KeyAura directory

2. **Remove dependencies (optional)**
   ```bash
   pip uninstall customtkinter pygame Pillow
   ```

## Support

If you encounter issues not covered in this guide:

1. Check the [README.md](README.md) for more information
2. Look for error messages in the console output
3. Ensure all prerequisites are met
4. Try running the demo script: `python demo.py`

## System Compatibility

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python    | 3.11    | 3.11+       |
| Windows   | 10      | 11          |
| RAM       | 4GB     | 8GB         |
| Storage   | 100MB   | 500MB       |

---

**Need Help?** Check the troubleshooting section above or refer to the main README file. 