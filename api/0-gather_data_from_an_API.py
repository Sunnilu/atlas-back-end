#!/usr/bin/python3
"""
Script that fetches and displays TODO list progress for a given employee ID
using JSONPlaceholder API.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    # Fetch employee name
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users?id={argv[1]}")
    user_data = user_response.json()
    if not user_data:
        print(f"Employee with ID {argv[1]} not found.")
        exit(1)
    employee_name = user_data[0]['name']

    # Fetch completed todos
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}&completed=true")
    todos_data = todos_response.json()
    total_tasks = len(todos_data)

    # Prepare and print task list
    task_list = []
    for todo in todos_data:
        task_list.append(f"\t{todo['title']}")

    # Print output
    print(f"Employee {employee_name} is done with tasks ({len(todos_data)}/{total_tasks}):")
    for task in task_list:
        print(task)
