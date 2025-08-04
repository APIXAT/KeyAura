#!/usr/bin/env python3
"""
KeyAura Enhanced Demo Script
This script demonstrates the new Ctrl+Click multi-key selection and advanced features.
"""

import json
import os
import time
from main import KeyAura

def demo_multi_key_selection(app):
    """Demonstrate the new Ctrl+Click multi-key selection feature."""
    print("\n🎯 Demo: Multi-Key Selection (Ctrl+Click)")
    print("=" * 50)
    
    print("1. Single key selection:")
    print("   - Click any key to select it")
    print("   - The key will highlight in green")
    
    print("\n2. Multi-key selection:")
    print("   - Hold Ctrl and click multiple keys")
    print("   - Selected keys will be highlighted")
    print("   - You can deselect by Ctrl+clicking again")
    
    print("\n3. Sound assignment to selected keys:")
    print("   - Select multiple keys using Ctrl+Click")
    print("   - Choose a sound file")
    print("   - Click 'Apply to Selected Keys'")
    
    # Simulate some key selections
    demo_keys = ["A", "S", "D"]
    print(f"\n📝 Demo: Selecting keys {', '.join(demo_keys)}")
    
    for key in demo_keys:
        app.selected_keys.add(key)
        if key in app.key_buttons:
            app.key_buttons[key].configure(
                fg_color="#00ff88",
                border_color="#00ff88"
            )
    
    app.update_selected_keys_display()
    print(f"✅ Selected keys: {', '.join(sorted(app.selected_keys))}")

def demo_enhanced_sound_customization(app):
    """Demonstrate enhanced sound customization features."""
    print("\n🔊 Demo: Enhanced Sound Customization")
    print("=" * 50)
    
    print("1. Individual key sound assignment:")
    print("   - Select a single key")
    print("   - Browse for a sound file")
    print("   - Click 'Apply to Selected Keys'")
    
    print("\n2. Multi-key sound assignment:")
    print("   - Use Ctrl+Click to select multiple keys")
    print("   - Apply the same sound to all selected keys")
    
    print("\n3. Bulk operations:")
    print("   - 'Apply to All Keys': Assign sound to every key")
    print("   - 'Clear Selected': Remove sounds from selected keys")
    
    # Set demo sounds for different keys
    demo_sounds = {
        "A": "sounds/mechanical_click.mp3",
        "S": "sounds/electronic_beep.mp3",
        "D": "sounds/nature_drop.mp3"
    }
    
    for key, sound_path in demo_sounds.items():
        app.key_sounds[key] = sound_path
        print(f"   - Key '{key}': {sound_path}")

def demo_visual_feedback(app):
    """Demonstrate visual feedback and animations."""
    print("\n✨ Demo: Visual Feedback & Animations")
    print("=" * 50)
    
    print("1. Key highlighting:")
    print("   - Selected keys: Green border and background")
    print("   - Hover effects: Blue glow on mouse over")
    print("   - Click feedback: Brief blue flash when pressed")
    
    print("\n2. Smooth animations:")
    print("   - Button hover transitions")
    print("   - Color changes with smooth transitions")
    print("   - Visual feedback for all interactions")
    
    print("\n3. Status indicators:")
    print("   - Selected keys display updates in real-time")
    print("   - Sound toggle button changes icon")
    print("   - Volume slider provides immediate feedback")

def demo_template_management_enhanced(app):
    """Demonstrate enhanced template management."""
    print("\n📁 Demo: Enhanced Template Management")
    print("=" * 50)
    
    # Create enhanced demo templates
    templates = [
        {
            "name": "Mechanical Vibes",
            "description": "Classic mechanical keyboard sounds",
            "key_sounds": {key: "sounds/mechanical_click.mp3" for key in app.key_buttons.keys()}
        },
        {
            "name": "Electronic Beeps",
            "description": "Digital electronic sound effects",
            "key_sounds": {key: "sounds/electronic_beep.mp3" for key in app.key_buttons.keys()}
        },
        {
            "name": "Nature Sounds",
            "description": "Relaxing nature-inspired sounds",
            "key_sounds": {key: "sounds/nature_drop.mp3" for key in app.key_buttons.keys()}
        }
    ]
    
    for template in templates:
        template_data = {
            "name": template["name"],
            "key_sounds": template["key_sounds"],
            "layout": "100%",
            "created": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        template_file = os.path.join(app.template_dir, f"{template['name']}.json")
        with open(template_file, 'w') as f:
            json.dump(template_data, f, indent=2)
        
        print(f"✅ Created template: {template['name']}")
        print(f"   Description: {template['description']}")

def demo_workflow_example(app):
    """Demonstrate a complete workflow example."""
    print("\n🎹 Demo: Complete Workflow Example")
    print("=" * 50)
    
    print("1. Start with a clean keyboard")
    print("2. Select multiple keys using Ctrl+Click:")
    print("   - Hold Ctrl and click: A, S, D, F")
    print("3. Browse and select a sound file")
    print("4. Click 'Apply to Selected Keys'")
    print("5. Test the sounds by clicking the keys")
    print("6. Create a template with 'Add Template'")
    print("7. Load different templates to switch sounds")
    
    # Simulate the workflow
    workflow_keys = ["A", "S", "D", "F"]
    print(f"\n📝 Simulating workflow with keys: {', '.join(workflow_keys)}")
    
    # Select the keys
    for key in workflow_keys:
        app.selected_keys.add(key)
        if key in app.key_buttons:
            app.key_buttons[key].configure(
                fg_color="#00ff88",
                border_color="#00ff88"
            )
    
    app.update_selected_keys_display()
    print(f"✅ Selected keys: {', '.join(sorted(app.selected_keys))}")
    
    # Apply a demo sound
    demo_sound = "sounds/workflow_demo.mp3"
    for key in workflow_keys:
        app.key_sounds[key] = demo_sound
    
    print(f"✅ Applied sound '{demo_sound}' to selected keys")

def main():
    """Main enhanced demo function."""
    print("🎹 KeyAura Enhanced Demo")
    print("=" * 60)
    print("This demo showcases the new Ctrl+Click multi-key selection")
    print("and enhanced sound customization features.")
    print("=" * 60)
    
    # Create and configure the application
    print("\n🚀 Initializing KeyAura with enhanced features...")
    app = KeyAura()
    
    # Demo different enhanced features
    demo_multi_key_selection(app)
    demo_enhanced_sound_customization(app)
    demo_visual_feedback(app)
    demo_template_management_enhanced(app)
    demo_workflow_example(app)
    
    print("\n" + "=" * 60)
    print("✅ Enhanced Demo completed!")
    print("\n🎯 Key New Features Demonstrated:")
    print("   • Ctrl+Click multi-key selection")
    print("   • Real-time selected keys display")
    print("   • Enhanced sound customization")
    print("   • Visual feedback and animations")
    print("   • Improved template management")
    print("   • Complete workflow examples")
    
    print("\n🚀 To run the full enhanced application:")
    print("   python main.py")
    print("   or")
    print("   python launcher.py")
    
    print("\n💡 Tips for using the enhanced features:")
    print("   • Hold Ctrl and click multiple keys to select them")
    print("   • Use 'Apply to Selected Keys' for group operations")
    print("   • Watch the selected keys display for real-time feedback")
    print("   • Experiment with different sound combinations")

if __name__ == "__main__":
    main() 