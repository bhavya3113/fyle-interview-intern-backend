@echo off
REM to stop on first error
set -e

REM Delete older .pyc files
REM for /d %%i in (env venv) do if exist "%%i" rmdir /s /q "%%i"
for /r %%i in (*.pyc) do del "%%i"

REM Run required migrations
set FLASK_APP=core/server.py

REM flask db init -d core/migrations/
REM flask db migrate -m "Initial migration." -d core/migrations/
REM flask db upgrade -d core/migrations/

REM Run server
waitress-serve --listen=0.0.0.0:5000 --call "core.server:app"
