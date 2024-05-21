#!/usr/bin/python3
'''
gather employee data from API and export data in the JSON format
'''

import re
import urllib.request
import json
import sys

REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':

    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            
            
            with urllib.request.urlopen(f'{REST_API}/users/{id}') as response:
                req = json.loads(response.read().decode())

            
            with urllib.request.urlopen(f'{REST_API}/todos') as response:
                task_req = json.loads(response.read().decode())

            
            username = req.get('username')
            tasks = []
            for task in task_req:
                if task.get('userId') == id:
                    task_data = {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": username
                    }
                    tasks.append(task_data)

            print(tasks)

            
            output = { str(id): tasks }
            
            
            filename = '{}.json'.format(id)
            with open(filename, 'w') as jsonfile:
                json.dump(output, jsonfile, indent=4)
                


            
        
