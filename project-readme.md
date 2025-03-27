# Python Intern Assignment - ADStack Backend Development

## Project Overview
This project demonstrates a comprehensive backend development solution with Flask API, database management, Android system simulation, and networking capabilities.

## Prerequisites
- Python 3.8+
- pip (Python Package Manager)
- Virtual Environment (recommended)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd python-intern-assignment
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Task-wise Execution

#### Backend API (Task 1 & 2)
```bash
python backend_api.py
# Access API at http://localhost:5000
```

#### Android System Simulation (Task 3)
```bash
python android_simulation.py
```

#### Networking Script (Task 4)
```bash
python networking_script.py
```

## Endpoint Details
- `POST /add-app`: Add app details
- `GET /get-app/<id>`: Retrieve app by ID
- `DELETE /delete-app/<id>`: Delete app by ID

## Note
Ensure all required Android development tools (avdmanager, emulator) are installed for Task 3.

## Submission
ZIP the entire project folder as `YourName_PythonInternAssignment.zip`
