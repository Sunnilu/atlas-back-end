#!/usr/bin/python3
"""
Script that fetches and displays TODO list progress for a given employee ID
using JSONPlaceholder API.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
    - employee_id (str): The ID of the employee whose TODO list progress is to be fetched.

    Prints:
    - Displays the employee's TODO list progress in the specified format.
    """
    # Fetch employee name
    name_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    name_data = name_response.json()

    if not name_data:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = name_data['name']

    # Fetch all todos for the employee
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Filter completed todos
    completed_todos = [todo for todo in todos_data if todo['completed']]

    # Prepare and print task list
    print(f"Employee {employee_name} is done with tasks ({len(completed_todos)}/{len(todos_data)}):")
    for todo in completed_todos:
        print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)


