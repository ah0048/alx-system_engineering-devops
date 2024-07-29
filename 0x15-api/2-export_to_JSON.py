#!/usr/bin/python3
'''module to returns information about TODO list progress.'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(url)
    name = user.json().get("username")
    url_tasks = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    all_tasks = requests.get(url_tasks)
    all_tasks = all_tasks.json()
    data = {}
    tasks = []
    for task in all_tasks:
        del task['userId']
        del task['id']
        task["task"] = task.pop('title')
        task["completed"] = task.pop('completed')
        task["username"] = name
        tasks.append(task)
    data[user_id] = tasks
    json_file = f'{user_id}.json'
    with open(json_file, 'w') as json_file:
        json.dump(data, json_file)
