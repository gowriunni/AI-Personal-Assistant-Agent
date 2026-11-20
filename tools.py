

from langchain.tools import tool

from database import (
    create_table,
    add_task_db,
    get_tasks,
    delete_task_db
)


# Make sure the database table exists
create_table()


# Tool 1: Add a task
@tool
def add_task(task: str) -> str:
    """Add a new task to the user's task list."""

    add_task_db(task)

    return f"Task added successfully: {task}"


# Tool 2: View all tasks
@tool
def view_tasks() -> str:
    """Show all tasks saved in the user's task list."""

    tasks = get_tasks()

    if not tasks:
        return "Your task list is empty."

    result = "Your saved tasks:\n"

    for task in tasks:
        task_id, task_name, status = task

        result += f"\nID: {task_id} | Task: {task_name} | Status: {status}"

    return result


# Tool 3: Delete a task
@tool
def delete_task(task_id: int) -> str:
    """Delete a task using its unique task ID."""

    tasks = get_tasks()

    matching_task = [
        task for task in tasks if task[0] == task_id
    ]

    if not matching_task:
        return f"No task found with ID {task_id}."

    delete_task_db(task_id)

    return f"Task deleted successfully. ID: {task_id}"
