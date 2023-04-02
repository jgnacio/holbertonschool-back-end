#!/usr/bin/python3
"""
Created on Sun Apr 2 17:31:00 2023.

@authors: jgnacio
@description:
    This script makes a request on jsonplaceholder which returns a user
    with completed tasks and filter by the id given in the execution.
"""
from json import JSONDecodeError
import requests
import sys

resp = requests.get(
    f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[-1]}')
employee_resp = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{sys.argv[-1]}'
)

employee_list = {}
emplyee_info = {}
try:
    employee_taks = resp.json()
    employee_info = employee_resp.json()
except JSONDecodeError:
    print('Response could not be serialized')

user_id = sys.argv[-1]
completed = total_taks = 0

# Get all the taks name in order and how many are complete.
taks_name_list = ""
for task in employee_taks:
    if task['completed'] == True:
        completed += 1
        taks_name_list += "     " + f"{task['title']}\n"
    total_taks += 1

employee_name = employee_info['name']

# Format the all print for the employee taks
print_employee = f"""\
Employee {employee_name} is done with tasks({completed}/{total_taks}):
{taks_name_list[:-1]}\
"""

print(print_employee)
