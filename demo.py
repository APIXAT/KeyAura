#!/usr/bin/env python3
"""
KeyAura Demo Script
This script demonstrates how to use the KeyAura application programmatically.
"""

import json
import os
import time
from main import KeyAura

def create_demo_template():
    """Create a demo template with sample data."""
    demo_template = {
        "name": "Demo Template",
        "key_sounds": {
            "A": "sounds/demo_key_1.mp3",
            "S": "sounds/demo_key_2.mp3",
            "D": "sounds/demo_key_3.mp3",
            "F": "sounds/demo_key_1.mp3",
            "G": "sounds/demo_key_2.mp3",
            "H": "sounds/demo_key_3.mp3",
            "J": "sounds/demo_key_1.mp3",
            "K": "sounds/demo_key_2.mp3",
            "L": "sounds/demo_key_3.mp3"
        },
        "layout": "100%",
        "created": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Save demo template
    os.makedirs("templates", exist_ok=True)
    with open("templates/Demo Template.json", 'w') as f:
        json.dump(demo_template, f, indent=2)
    
    print("✅ Demo template created successfully!")

def demo_keyboard_interaction(app):
    """Demonstrate keyboard interaction."""
    print("\n🎹 Demo: Keyboard Interaction")
    print("=" * 40)
    
    # Simulate key presses
    demo_keys = ["A", "S", "D", "F", "G"]
    for key in demo_keys:
        print(f"Playing sound for key: {key}")
        app.play_key_sound(key)
        time.sleep(0.5)  # Wait between key presses

def demo_template_management(app):
    """Demonstrate template management."""
    print("\n📁 Demo: Template Management")
    print("=" * 40)
    
    # Create a demo template
    create_demo_template()
    
    # Load templates
    app.load_templates()
    print(f"Loaded {len(app.templates)} templates")
    
    # List available templates
    for template_name in app.templates.keys():
        print(f"  - {template_name}")

def demo_sound_customization(app):
    """Demonstrate sound customization."""
    print("\n🔊 Demo: Sound Customization")
    print("=" * 40)
    
    # Set a demo sound for key 'A'
    demo_sound_path = "sounds/demo_sound.mp3"
    app.key_sounds["A"] = demo_sound_path
    print(f"Set sound for key 'A': {demo_sound_path}")
    
    # Apply sound to all keys
    for key in app.key_buttons.keys():
        app.key_sounds[key] = demo_sound_path
    print("Applied demo sound to all keys")

def main():
    """Main demo function."""
    print("🎹 KeyAura Demo")
    print("=" * 50)
    
    # Create and configure the application
    print("Initializing KeyAura...")
    app = KeyAura()
    
    # Demo different features
    demo_sound_customization(app)
    demo_template_management(app)
    demo_keyboard_interaction(app)
    
    print("\n✅ Demo completed!")
    print("\nTo run the full application:")
    print("  python main.py")
    print("  or")
    print("  python launcher.py")

if __name__ == "__main__":
    main() 