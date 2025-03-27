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

# Python Backend Development Assignment Documentation


## Task 1: Backend Development (Backend API)
### File: `backend_api.py`
#### Approach
The backend API was developed using Flask and SQLAlchemy to create a robust, scalable application management system.

#### Key Components
1. **Database Model**
```python
class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
```
- Defines the structure for storing app information
- Uses SQLAlchemy ORM for database interactions

2. **API Endpoints**
- `POST /add-app`: Adds new app details to the database
- `GET /get-app/{id}`: Retrieves app details by ID
- `DELETE /delete-app/{id}`: Removes an app by ID

#### Key Challenges and Solutions
- Implemented error handling for database operations
- Used Flask-SQLAlchemy for seamless database integration
- Provided JSON serialization for API responses

## Task 2: Database Management
### File: `database_manager.py`
#### Approach
Created a SQLite database management script to handle app information storage and initialization.

#### Key Features
1. **Database Creation**
```python
def create_database():
    conn = sqlite3.connect('apps.db')
    cursor = conn.cursor()
    
    # Create apps table with required schema
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_name TEXT NOT NULL,
        version TEXT NOT NULL,
        description TEXT
    )
    ''')
```

2. **Sample Data Insertion**
- Included sample apps for initial testing
- Demonstrates database population technique

#### Challenges Addressed
- Ensured database schema matches API requirements
- Provided mechanism for easy database initialization

## Task 3: Virtual Android System Simulation
### File: `android_simulator.py`
#### Approach
Developed a Python script to simulate a virtual Android environment with system information retrieval.

#### Key Functionalities
1. **Virtual System Creation**
```python
def create_virtual_system(self):
    try:
        create_cmd = [
            'avdmanager', 'create', 'avd', 
            '-n', self.avd_name, 
            '-k', 'system-images;android-30;google_apis;x86_64'
        ]
        subprocess.run(create_cmd, check=True)
    except Exception as e:
        self.logger.error(f"Error creating virtual system: {e}")
```

2. **System Information Retrieval**
```python
def get_system_info(self):
    system_info = {
        'os_version': platform.system(),
        'os_release': platform.release(),
        'device_model': platform.machine(),
        'total_memory': f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
        'available_memory': f"{psutil.virtual_memory().available / (1024**3):.2f} GB"
    }
```

#### Challenges and Solutions
- Implemented robust error handling
- Used logging for tracking system operations
- Provided flexibility in virtual system management

## Task 4: Basic Networking
### File: `network_manager.py`
#### Approach
Created a networking script to establish communication between the virtual Android system and backend server.

#### Key Networking Features
1. **Device Information Generation**
```python
def get_device_info(self):
    return {
        'device_id': self.device_id,
        'os_version': platform.system() + " " + platform.release(),
        'device_model': platform.machine(),
        'total_memory': f"{platform.processor()} processor"
    }
```

2. **Server Communication**
```python
def send_device_info(self):
    try:
        response = requests.post(
            f'{self.server_url}/add-app', 
            json={
                'app_name': 'DeviceInfoApp',
                'version': '1.0.0',
                'description': json.dumps(device_info)
            }
        )
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
```

#### Challenges Addressed
- Implemented secure device information transmission
- Provided TCP and HTTP communication methods
- Added error handling for network operations

## Project Dependencies
### File: `requirements.txt`
```
flask==2.3.2
flask-sqlalchemy==3.0.3
requests==2.31.0
psutil==5.9.5
uuid==1.30.0
pytest==7.3.1
```
- Carefully selected compatible library versions
- Covered all project requirements

## Additional Considerations
1. **Error Handling**: Implemented comprehensive error management
2. **Logging**: Added detailed logging for tracking operations
3. **Modularity**: Designed code with separation of concerns
4. **Scalability**: Created flexible, extensible components

## Deployment Recommendations
1. Use virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Configure Android development tools
4. Set up appropriate environment variables

## Future Improvements
- Enhance security mechanisms
- Add more comprehensive logging
- Implement advanced error handling
- Create more robust networking protocols

## Conclusion
The solution provides a comprehensive approach to the Python Intern Assignment, addressing all specified requirements with robust, scalable, and modular code.
