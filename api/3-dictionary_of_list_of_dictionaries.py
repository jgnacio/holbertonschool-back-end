#!/usr/bin/python3
"""
Created on Mon Apr 3 10:29:00 2023.

@authors: jgnacio
@description:
    This script makes a request on jsonplaceholder which returns all
    users with a todo list of tasks that have completed and their
    titles, and wirte this dictionary on a json file.
"""
import json
import requests


COMPLETED = TOTAL_TASK = 0
TODOS_URL = 'https://jsonplaceholder.typicode.com/todos'
EMPLOYEE_URL = 'https://jsonplaceholder.typicode.com/users/'

# Request for the taks
todos_data = requests.get(TODOS_URL, timeout=100)
resp_employee = requests.get(EMPLOYEE_URL, timeout=100)

# Request for the employee info

employee_info = {}
try:
    todos_tasks = todos_data.json()
    employees_info = resp_employee.json()
except json.JSONDecodeError:
    print('Response could not be serialized')

employees_names = []
for employee in employees_info:
    employees_names.append(employee['name'])

employee_tasks = []
all_employee_tasks = {}
for index, name in enumerate(employees_names, 1):
    for todo in todos_tasks:
        if todo['userId'] == index:
            employee_tasks.append({
                "username": name,
                "task": todo['title'],
                "completed": todo['completed']
            })
    all_employee_tasks.update({str(index): employee_tasks})
    employee_tasks = []

with open('todo_all_employees.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(all_employee_tasks, indent=4))
