#!/usr/bin/python3

"""
Python script that exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    user_data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    user_data2 = response2.json()

    for k in user_data2:
        if k['id'] == int(argv[1]):
            employee = k['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for k in user_data:

            row = []
            if k['userId'] == int(argv[1]):
                row.append(k['userId'])
                row.append(employee)
                row.append(k['completed'])
                row.append(k['title'])

                writ.writerow(row)
