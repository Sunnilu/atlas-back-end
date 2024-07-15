#!/usr/bin/python3
"""
Script that fetches and displays TODO list progress for a given employee ID
using JSONPlaceholder API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    try:
        # Fetch user information
        user_response = requests.get(f"{base_url}users/{employee_id}")
        user = user_response.json()
        employee_name = user['name']

        # Fetch TODO list for the employee
        todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id})
        todos = todos_response.json()

        # Filter completed tasks
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]

        # Print TODO list progress
        print(f"Employee {employee_name} is done with tasks "
              f"({len(completed_tasks)}/{len(todos)}):")

        for task in completed_tasks:
            print(f"\t{task}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
