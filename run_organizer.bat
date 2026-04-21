@echo off
SETLOCAL

REM Preferred drop folder names on Desktop
SET DROP_FOLDER=%USERPROFILE%\Desktop\3D_DROP
SET ALT_DROP_FOLDER=%USERPROFILE%\Desktop\3-D_DROP
SET ALT_DROP_FOLDER2=%USERPROFILE%\Desktop\3-D drop
SET ALT_DROP_FOLDER3=%USERPROFILE%\Desktop\3D drop

IF EXIST "%ALT_DROP_FOLDER%" SET DROP_FOLDER=%ALT_DROP_FOLDER%
IF EXIST "%ALT_DROP_FOLDER2%" SET DROP_FOLDER=%ALT_DROP_FOLDER2%
IF EXIST "%ALT_DROP_FOLDER3%" SET DROP_FOLDER=%ALT_DROP_FOLDER3%

ECHO -----------------------------------------
ECHO 3D FILE ORGANIZER - ONE CLICK RUN
ECHO -----------------------------------------
ECHO Using drop folder:
ECHO %DROP_FOLDER%

IF NOT EXIST "%DROP_FOLDER%" (
    ECHO.
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
