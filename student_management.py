
import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    course TEXT)''')

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    print("Student added successfully!\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    print()

def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, student_id))
    conn.commit()
    print("Student updated successfully!\n")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Student deleted successfully!\n")

while True:
    print("1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")
