import sqlite3

# Database Connection and Schema Creation
def create_database():
    conn = sqlite3.connect('apps.db')
    cursor = conn.cursor()
    
    # Create Apps Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        app_name TEXT NOT NULL,
        version TEXT NOT NULL,
        description TEXT
    )
    ''')
    
    # Sample Data Insertion
    sample_apps = [
        ('MyFirstApp', '1.0.0', 'A sample mobile application'),
        ('NetworkTool', '2.1.5', 'Network connectivity analyzer'),
        ('GameZone', '3.2.1', 'Mobile gaming platform')
    ]
    
    cursor.executemany('''
    INSERT INTO apps (app_name, version, description) 
    VALUES (?, ?, ?)
    ''', sample_apps)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Database and sample data created successfully!")
