#!/usr/bin/python3
"""
Script that fetches and displays TODO list progress for a given employee ID
using JSONPlaceholder API.
"""

import requests
import sys
import json


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

    if name_response.status_code != 200:
        print(f"Error fetching employee with ID {employee_id}. Status code: {name_response.status_code}")
        sys.exit(1)

    name_data = name_response.json()

    if not name_data:
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)

    employee_name = name_data['name']

    # Fetch all todos for the employee
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    if todos_response.status_code != 200:
        print(f"Error fetching TODO list for employee with ID {employee_id}. Status code: {todos_response.status_code}")
        sys.exit(1)

    todos_data = todos_response.json()

    # Filter completed todos
    completed_todos = [{'task': todo['title'], 'completed': todo['completed'], 'username': employee_name} for todo in todos_data]

    # Prepare and print task list
    print(f"Employee {employee_name} is done with tasks ({len(completed_todos)}/{len(todos_data)}):")
    for todo in completed_todos:
        print(f"\t{todo['task']} - Completed: {todo['completed']}")

    # Export data in JSON format
    json_file_name = f"{employee_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump({employee_id: completed_todos}, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)

    # Export data for all employees in JSON format
    all_employees_data = {}
    for emp_id in range(1, 11):  # Assuming employee IDs range from 1 to 10
        all_employees_data[emp_id] = fetch_all_employee_todos(emp_id)

    all_employees_json_file_name = "todo_all_employees.json"
    with open(all_employees_json_file_name, 'w') as all_employees_json_file:
        json.dump(all_employees_data, all_employees_json_file, indent=4)
