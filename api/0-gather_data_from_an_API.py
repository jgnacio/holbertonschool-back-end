#!/usr/bin/python3
"""
Created on Sun Apr 2 17:31:00 2023.

@authors: jgnacio
@description:
    This script makes a request on jsonplaceholder which returns a user
    with completed tasks and filter by the id given in the execution.
"""
import json
import sys
import urllib.request

user = sys.argv[1]

todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user)
employee_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user)

# Request for the taks
with urllib.request.urlopen(todos_url) as response:
    todos_data = response.read().decode()

# Request for the employee info
with urllib.request.urlopen(employee_url) as response:
    employee_data = response.read().decode()

employee_info = {}
try:
    employee_taks = json.loads(todos_data)
    employee_info = json.loads(employee_data)
except json.JSONDecodeError:
    print('Response could not be serialized')

completed = total_taks = 0

# Get all the taks name in order and how many are complete.
taks_name_list = ""
for task in employee_taks:
    if task['completed'] is True:
        completed += 1
        taks_name_list += "\t {}\n".format(task['title'])
    total_taks += 1

employee_name = employee_info['name']

# Format the all print for the employee taks
print_employee = """\
Employee {} is done with tasks({}/{}):
{}\
""".format(employee_name, completed, total_taks, taks_name_list[:-1])

print(print_employee)
