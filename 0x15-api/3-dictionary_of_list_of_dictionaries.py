#!/usr/bin/python3
"""Python script to fetch REST API for todo lists of employees using urllib"""

import json
import urllib.request
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    with urllib.request.urlopen(url) as response:
        Users = json.loads(response.read().decode())

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(USER_ID)

        with urllib.request.urlopen(todo_url) as response:
            tasks = json.loads(response.read().decode())

        users_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            users_dict[USER_ID].append({
                "username": USERNAME,
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f, indent=4)
