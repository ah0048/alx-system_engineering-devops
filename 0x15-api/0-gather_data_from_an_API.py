#!/usr/bin/python3
'''module to returns information about TODO list progress.'''
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
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    all_tasks = requests.get(url_tasks)
    all_tasks = all_tasks.json()
    for task in all_tasks:
        if int(user_id) == task.get("userId"):
            total_tasks += 1
            if task.get("completed"):
                completed_tasks += 1
                user_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        name, completed_tasks, total_tasks))
    for task in user_tasks:
        print("\t {}".format(task))
