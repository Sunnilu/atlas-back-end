#!/usr/bin/python3

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
    - employee_id (int): The ID of the employee whose TODO list progress is to be fetched.

    Prints:
    - Displays the employee's TODO list progress in the specified format.

    Example output format:
    Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        TASK_TITLE
        TASK_TITLE
        ...

    Note:
    - Uses the JSONPlaceholder API (https://jsonplaceholder.typicode.com/) to fetch data.
    - Requires the 'requests' module to be installed (`pip install requests`).
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'

    try:
        # Fetching user information
        response = requests.get(user_url)
        if response.status_code != 200:
            print(f"Failed to fetch user information for ID {employee_id}.")
            return

        user_data = response.json()
        employee_name = user_data['name']

        # Fetching todo list for the employee
        response = requests.get(todos_url)
        if response.status_code != 200:
            print(f"Failed to fetch TODO list for ID {employee_id}.")
            return

        todos_data = response.json()
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task['completed']]
        total_done_tasks = len(done_tasks)

        # Printing the output in the required format
        print(f"Employee {employee_name} is done with tasks ({total_done_tasks}/{total_tasks}):")

        for task in done_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)

