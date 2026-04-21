# DevOps Lab App

A simple Flask web app with a styled UI that shows:
- A welcome message
- Name and registration number
- Current session timestamp
- Application status badge

## Prerequisites

- Python 3.10+
- pip

## Setup

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install -r requirements.txt
```

## Run The App

```powershell
python app.py
```

The app will start at:
- http://127.0.0.1:5000
- http://localhost:5000

## Project Files

- `app.py`: Flask application and styled HTML response
- `requirements.txt`: Python dependencies
- `README.md`: Setup and run documentation