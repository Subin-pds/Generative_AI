@echo off
cd /d "C:\Users\subin\OneDrive\Desktop\GenAI"
call ".venv\Scripts\activate"
if %ERRORLEVEL% neq 0 (
    echo Error: Could not activate the virtual environment.
    pause
    exit /b
)
streamlit run App.py
pause