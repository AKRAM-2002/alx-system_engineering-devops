#!/usr/bin/python3
'''
gather employee data from API
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

            emp_name = req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
