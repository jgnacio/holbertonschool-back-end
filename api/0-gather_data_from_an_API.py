#!/usr/bin/python3
"""
Created on Sun Apr 2 17:31:00 2023.

@authors: jgnacio
@description:
"""
from json import JSONDecodeError
import requests
import sys

resp = requests.get('https://jsonplaceholder.typicode.com/todos')
todos_list = {}
try:
    todos_list = resp.json()
except JSONDecodeError:
    print('Response could not be serialized')

user_id = sys.argv[-1]

completed = 0
for todo in todos_list:
    if int(user_id) == todo["userId"]:
        if todo['completed'] == True:
            completed += 1
print(completed)
