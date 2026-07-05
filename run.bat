@echo off
:: bob_AI — one-command setup + environment check (Windows)
:: Usage:  run.bat            (setup + verify)
::         run.bat check      (just re-run the environment check)

setlocal

if "%1"=="check" goto check

echo ============================================
echo   bob_AI :: AI Foundations Course setup
echo ============================================

echo.
echo [1/3] Creating virtual environment (.venv) ...
if not exist ".venv" (
    py -m venv .venv
) else (
    echo      .venv already exists, reusing it.
)

echo.
echo [2/3] Installing requirements ...
call .venv\Scripts\activate
py -m pip install --upgrade pip >nul
py -m pip install -r requirements.txt

:check
echo.
echo [3/3] Verifying environment ...
call .venv\Scripts\activate 2>nul
py module_01_setup\setup_check.py

echo.
echo Done. Next: open module_01_setup\headfirst.md
endlocal
