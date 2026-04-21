@echo off
SETLOCAL

REM Default drop folder on Desktop
SET DROP_FOLDER=%USERPROFILE%\Desktop\3D_DROP

ECHO -----------------------------------------
ECHO 3D FILE ORGANIZER - ONE CLICK RUN
ECHO -----------------------------------------

IF NOT EXIST "%DROP_FOLDER%" (
    ECHO Creating drop folder on Desktop...
    mkdir "%DROP_FOLDER%"
    ECHO.
    ECHO Put your files in:
    ECHO %DROP_FOLDER%
    ECHO Then double-click this again.
    pause
    exit
)

ECHO.
ECHO Running DRY RUN (preview only)...
python tools\file_organizer\organizer.py --source "%DROP_FOLDER%" --dry-run

ECHO.
SET /P CONFIRM=Run for real? (Y/N): 

IF /I "%CONFIRM%"=="Y" (
    python tools\file_organizer\organizer.py --source "%DROP_FOLDER%"
    ECHO.
    ECHO Done.
) ELSE (
    ECHO Cancelled.
)

pause
