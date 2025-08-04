@echo off
title KeyAura Launcher
echo.
echo ========================================
echo           KeyAura Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11 or higher and try again
    echo.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Python version: %PYTHON_VERSION%

REM Run the launcher
echo.
echo Starting KeyAura...
python launcher.py

REM If there was an error, pause to show the message
if errorlevel 1 (
    echo.
    echo Press any key to exit...
    pause >nul
) 