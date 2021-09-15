#!/usr/bin/python3
"""
script to export data in the CSV format
"""
import json
import csv
import requests
from sys import argv


if __name__ == '__main__':

    sessionReq = requests.Session()

    e_id = argv[1]
    u_todo = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(e_id)
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(e_id)

    emp = sessionReq.get(url_todo)
    emp_name = sessionReq.get(url_user)

    json_req = emp.json()
    user = emp_name.json()['username']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = e_id + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimeter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([emp, user, i.get('completed'), i.get('title')])
