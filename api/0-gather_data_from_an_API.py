#!/usr/bin/python3
"""
Script that fetches and displays TODO list progress for a given employee ID
using JSONPlaceholder API.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    employee_id = argv[1]
    
    # Fetch employee name
    name_response = requests.get(f"https://jsonplaceholder.typicode.com/users?id={employee_id}")
    name_data = name_response.json()
    
    if not name_data:
        exit(f"Employee with ID {employee_id} not found.")
    
    employee_name = name_data[0]["name"]

    # Fetch all todos for the employee
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Filter completed todos
    completed_todos = [todo for todo in todos_data if todo['completed']]

    # Prepare and print task list
    print(f"Employee {employee_name} is done with tasks ({len(completed_todos)}/{len(todos_data)}):")
    for todo in completed_todos:
        print(f"\t{todo['title']}")


