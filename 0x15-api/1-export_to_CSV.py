#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + "users/{}".format(sys.argv[1])
    todo_url = url + "todos"
    params = {"userId": sys.argv[1]}
    user = requests.get(url=user_url).json()
    todos = requests.get(url=todo_url, params=params).json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo)

    # Set the filename for the CSV file
    filename = "{}.csv".format(sys.argv[1])

    # Write the CSV data to the file
    with open(filename, mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for todo in completed:
            writer.writerow({
                'USER_ID': user.get('id'),
                'USERNAME': user.get('username'),
                'TASK_COMPLETED_STATUS': 'true',
                'TASK_TITLE': todo.get('title')
            })

        for todo in todos:
            if todo not in completed:
                writer.writerow({
                    'USER_ID': user.get('id'),
                    'USERNAME': user.get('username'),
                    'TASK_COMPLETED_STATUS': 'false',
                    'TASK_TITLE': todo.get('title')
                })

    print("CSV file created: {}".format(filename))
