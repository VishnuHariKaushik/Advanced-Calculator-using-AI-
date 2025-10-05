# Advanced Calculator — Flask

Simple Flask web app (app.py) that evaluates advanced math expressions.

## Contents
- app.py — Flask app
- README.md — this file
- (optional) requirements.txt

## Prerequisites
- Python 3.8+
- pip

## Setup (Windows)
1. Open PowerShell or CMD and change to project folder:
   cd "c:\Python practice"

2. (Optional) Create and activate a virtual environment:
   PowerShell:
     python -m venv venv
     .\venv\Scripts\Activate.ps1
   CMD:
     python -m venv venv
     .\venv\Scripts\activate.bat

3. Install dependencies:
   pip install flask

4. (Optional) Capture dependencies:
   pip freeze > requirements.txt

## Run (development)
- Option A (direct):
  python app.py

- Option B (Flask CLI):
  set FLASK_APP=app.py
  flask run

Open the local URL shown in the terminal (example: http://127.0.0.1:5000).

## Usage
Enter expressions like:
- 2+2
- sin(90)
- log(100, 10)
- sqrt(16)
- 2**8

## Local App URL (from terminal)
Replace the placeholder below with the URL printed by the Flask run output:
LOCAL_APP_URL_PLACEHOLDER

## Notes & Security
- The app uses a restricted evaluation context but only run it for trusted users.
- For production, use a WSGI server (Waitress on Windows or Gunicorn on Linux) and enable TLS.

## Deploy to GitHub (quick steps)
1. Initialize local repo and commit:
   git init
   git add .
   git commit -m "Initial commit"

2a. Using GitHub CLI (recommended):
   gh repo create REPO_NAME --public --source=. --remote=origin --push
   (replace REPO_NAME)

2b. Or create repo on GitHub, then:
   git branch -M main
   git remote add origin https://github.com/USERNAME/REPO_NAME.git
   git push -u origin main

(Replace USERNAME and REPO_NAME accordingly.)

## Troubleshooting
- If pip install fails: ensure Python and pip are on PATH.
- If port already used: use `flask run --port 5001` or change app.run() port.

License: MIT
# From Advanced Calculator using AI
# 1) Run app
python app.py
# OR using Flask CLI
set FLASK_APP=app.py
flask run

# The terminal will show the URL, e.g.:
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
