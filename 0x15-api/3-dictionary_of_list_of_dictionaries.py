#!/usr/bin/python3
'''Module to return information about TODO list progress.'''
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    # Dictionary to store user data and their tasks
    data = {}

    for user in users:
        id = user.get('id')
        username = user.get('username')

        # Fetch tasks for this user
        url_tasks = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
        all_tasks = requests.get(url_tasks).json()

        tasks = []
        for task in all_tasks:
            # Modify task dictionary
            task_data = {
                'username': username,
                'task': task.get('title'),
                'completed': task.get('completed'),
            }
            tasks.append(task_data)

        # Add tasks to the data dictionary for this user
        data[id] = tasks

    # Write the data to a JSON file
    json_file = 'todo_all_employees.json'
    with open(json_file, 'w') as f:
        json.dump(data, f)
