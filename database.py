
import sqlite3


# Connect to the database
def connect_db():
    connection = sqlite3.connect("tasks.db")
    return connection


# Create tasks table
def create_table():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    connection.commit()

    connection.close()


# Add a task
def add_task_db(task):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (task) VALUES (?)",
        (task,)
    )

    connection.commit()

    connection.close()


# View all tasks
def get_tasks():

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    connection.close()

    return tasks


# Delete a task
def delete_task_db(task_id):

    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    connection.close()
