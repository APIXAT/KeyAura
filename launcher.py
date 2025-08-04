#!/usr/bin/env python3
"""
KeyAura Launcher
A simple launcher script that checks dependencies and starts the KeyAura application.
"""

import sys
import subprocess
import importlib.util
import os

def check_python_version():
    """Check if Python version is 3.11 or higher."""
    if sys.version_info < (3, 11):
        print("❌ Error: KeyAura requires Python 3.11 or higher.")
        print(f"   Current version: {sys.version}")
        print("   Please upgrade Python and try again.")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_dependency(module_name, package_name=None):
    """Check if a dependency is installed."""
    if package_name is None:
        package_name = module_name
    
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print(f"❌ Missing dependency: {package_name}")
        return False
    else:
        print(f"✅ {package_name} is installed")
        return True

def install_dependencies():
    """Install missing dependencies."""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def main():
    """Main launcher function."""
    print("🎹 KeyAura Launcher")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    print("\n🔍 Checking dependencies...")
    dependencies = [
        ("customtkinter", "CustomTkinter"),
        ("pygame", "Pygame"),
        ("PIL", "Pillow")
    ]
    
    missing_deps = []
    for module, package in dependencies:
        if not check_dependency(module, package):
            missing_deps.append(package)
    
    # Install missing dependencies if any
    if missing_deps:
        print(f"\n⚠️  Missing dependencies: {', '.join(missing_deps)}")
        response = input("Would you like to install them now? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            if not install_dependencies():
                sys.exit(1)
        else:
            print("❌ Cannot start KeyAura without required dependencies.")
            sys.exit(1)
    
    # Check if main.py exists
    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found in current directory.")
        print("   Please run this launcher from the KeyAura directory.")
        sys.exit(1)
    
    # Start the application
    print("\n🚀 Starting KeyAura...")
    try:
        import main
        main.app = main.KeyAura()
        main.app.run()
    except KeyboardInterrupt:
        print("\n👋 KeyAura closed by user.")
    except Exception as e:
        print(f"\n❌ Error starting KeyAura: {e}")
        print("   Please check the error message above and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main() 