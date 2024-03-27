#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    user_data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    user_data2 = response2.json()

    new_dict1 = {}

    for l in user_data2:

        row = []
        for k in user_data:

            new_dict2 = {}

            if l['id'] == k['userId']:

                new_dict2['username'] = l['username']
                new_dict2['task'] = k['title']
                new_dict2['completed'] = k['completed']
                row.append(new_dict2)

        new_dict1[l['id']] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict1)
        f.write(json_obj)
