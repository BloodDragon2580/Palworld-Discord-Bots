::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSjk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGmF+GEfBlZwRReBM3m+OqEZ+/y16vKCwg==
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
:: This script creates a virtual environment, installs dependencies, and
:: allows the user to choose between global and virtual python environment for running the program
:: @author KOOKIIE
:: Turn ECHO off
@echo off
if not exist venv\ (
    echo No venv folder found
    echo Setting up virtual environment...
    :: Generate VENV in project dir
    python -m venv %~dp0venv

    echo Installing dependencies...
    :: Activate the VENV
    call venv\scripts\activate.bat
    :: Install requirements
    pip install wheel
    pip install -r requirements.txt
)

:: function to run from global environment
:global
echo PalworldBot wird gestartet
python main.py
:: uncomment to auto-restart:
echo "The program crashed, restarting..."
goto global
exit \b
