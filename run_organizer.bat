@echo off
SETLOCAL
cd /d "%~dp0"
SET "DROP_FOLDER=%~dp03D_DROP"
IF NOT "%~1"=="" SET "DROP_FOLDER=%~1"
IF NOT EXIST "%DROP_FOLDER%" (
    ECHO Drop folder not found: "%DROP_FOLDER%"
    EXIT /B 1
)
python tools\file_organizer\organizer.py --source "%DROP_FOLDER%" --dry-run
IF ERRORLEVEL 1 EXIT /B 1
SET /P "CONFIRM=Move reviewed files into Needs_Review? (Y/N): "
IF /I "%CONFIRM%"=="Y" python tools\file_organizer\organizer.py --source "%DROP_FOLDER%" --apply
