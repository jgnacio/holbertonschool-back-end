#!/usr/bin/python3
"""
Created on Mon Apr 2 9:44:00 2023.

@authors: jgnacio
@description:
    This script makes a request on jsonplaceholder which returns a user
    with completed tasks and filter by the id given in the execution,
    and returns a list of tasks completed in csv format.
"""
import json
import sys
import urllib.request

USER = sys.argv[1]
TODOS_URL = f'https://jsonplaceholder.typicode.com/todos?userId={USER}'
EMPLOYEE_URL = f'https://jsonplaceholder.typicode.com/users/{USER}'
TASKS_LIST = ""

# Request for the taks
with urllib.request.urlopen(TODOS_URL) as response:
    todos_data = response.read().decode()

# Request for the employee info
with urllib.request.urlopen(EMPLOYEE_URL) as response:
    employee_data = response.read().decode()

employee_info = {}
try:
    employee_tasks = json.loads(todos_data)
    employee_info = json.loads(employee_data)
except json.JSONDecodeError:
    print('Response could not be serialized')


# Get all the taks name in order and how many are complete.
for task in employee_tasks:
    TASKS_LIST += f"\
\"{task['userId']}\",\
\"{employee_info['name']}\",\
\"{task['completed']}\",\
\"{task['title']}\"\n"

with open(f'{USER}.csv', 'w', encoding='utf-8') as f:
    f.write(TASKS_LIST[:-1])
