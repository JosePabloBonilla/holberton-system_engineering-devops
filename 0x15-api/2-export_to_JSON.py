#!/usr/bin/python3
"""
script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    emp_id = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(emp_id)
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)

    emp = sessionReq.get(url_todo)
    emp_name = sessionReq.get(url_user)

    json_req = emp.json()
    user = emp_name.json()['username']

    totalTasks = []
    updateUser = {}

    for all_emp in json_req:
        totalTasks.append(
                {
                    "task": all_emp.get('title'),
                    "completed": all_emp.get('completed'),
                    "username": user,
                })
    updateUser[emp_id] = totalTasks

    file_Json = emp_id + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
