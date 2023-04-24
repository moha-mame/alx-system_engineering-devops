#!/usr/bin/python3

import requests
import sys

# Function to get the TODO list progress for an employee
def get_employee_todo_progress(employee_id):
    # API endpoint URL
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Make a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        # If not, display an error message and exit the script
        print(f"Error: {response.status_code} - {response.reason}")
        sys.exit()

    # Parse the response JSON data
    todos = response.json()

    # Count the number of completed tasks and total number of tasks
    num_completed_tasks = sum(1 for todo in todos if todo['completed'])
    total_num_tasks = len(todos)

    # Get the name of the employee
    employee_name = todos[0]['name']

    # Display the progress report
    print(f"Employee {employee_name} is done with {num_completed_tasks}/{total_num_tasks} tasks:")

    # Display the titles of completed tasks
    for todo in todos:
        if todo['completed']:
            print(f"\t- {todo['title']}")

# Get the employee ID from the command line argument
employee_id = int(sys.argv[1])

# Call the function to get the employee's TODO list progress
get_employee_todo_progress(employee_id)
