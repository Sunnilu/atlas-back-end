#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import requests
import sys
import csv

def fetch_employee_todo_progress(employee_id):
    """
    Fetches and exports the TODO list progress for a given employee ID into a CSV file.

    Args:
    - employee_id (int): The ID of the employee whose TODO list progress is to be fetched and exported.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'

    try:
        """ Fetching user information """
        response = requests.get(user_url)
        response.raise_for_status()
        user_data = response.json()
        employee_name = user_data['username']  # Use 'username' instead of 'name' as per JSONPlaceholder API

        """ Fetching todo list for the employee """
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Prepare CSV file name
        csv_filename = f"{USER_ID}.csv"

        """ Writing to CSV file """
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

            for task in todos_data:
                task_completed = "Completed" if task['completed'] else "Not Completed"
                csv_writer.writerow([employee_id, employee_name, task_completed, task['title']])

        print(f"Exported TODO list for Employee ID {employee_id} to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
