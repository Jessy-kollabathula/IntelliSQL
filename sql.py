import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
    NAME TEXT,
    CLASS TEXT,
    MARKS INTEGER,
    COMPANY TEXT
)
""")

# Insert sample data
students_data = [
    ('Sijo', 'BTech', 75, 'JSW'),
    ('Anu', 'MCom', 85, 'Infosys'),
    ('Rahul', 'BTech', 92, 'TCS'),
    ('Meera', 'MCom', 67, 'Wipro'),
    ('John', 'MBA', 88, 'Infosys')
]

cursor.executemany("INSERT INTO STUDENTS VALUES(?,?,?,?)", students_data)

connection.commit()
connection.close()

print("Database created successfully!")