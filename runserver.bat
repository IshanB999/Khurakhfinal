@echo off
REM Check if Python is in PATH or set its path manually
SET PYTHON_PATH=python

REM Run the Django server with network binding
%PYTHON_PATH% manage.py runserver localhost:8000

REM Keep the terminal window open (optional)
pause
