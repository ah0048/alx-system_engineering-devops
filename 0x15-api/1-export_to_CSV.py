#!/usr/bin/python3
'''module to returns information about TODO list progress.'''
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(url)
    name = user.json().get("name")
    total_tasks = 0
    completed_tasks = 0
    user_tasks = []
    url_tasks = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    all_tasks = requests.get(url_tasks)
    all_tasks = all_tasks.json()
    csv_file = f'{user_id}.csv'
    with open(csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for task in all_tasks:
            data = {}
            data["user_id"] = user_id
            data["name"] = name
            data["completed"] = task.get('completed')
            data["title"] = task.get('title')
            csv_writer.writerow(data.values())
