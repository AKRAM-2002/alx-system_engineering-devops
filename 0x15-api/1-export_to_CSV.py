#!/usr/bin/python3
'''
gather employee data from API and export it in CSV format
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
'''

import re
import urllib.request
import json
import sys
import csv

REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            
            
            with urllib.request.urlopen(f'{REST_API}/users/{id}') as response:
                req = json.loads(response.read().decode())

            
            with urllib.request.urlopen(f'{REST_API}/todos') as response:
                task_req = json.loads(response.read().decode())


            # field names
            fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            
            username = req.get('username')
            filename = '{}.csv'.format(id)
            
            with open(filename, 'w', ) as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                for task in task_req:
                    if task.get('userId') == id:
                        writer.writerow([id, username, task.get('completed'), task.get('title')])



            
        
