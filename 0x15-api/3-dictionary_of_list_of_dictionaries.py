#!/usr/bin/python3
"""
Extends your Python script to export data in the json format.
"""
import json
import requests

if __name__ == "__main__":
    # try:
    r2 = requests.get('https://jsonplaceholder.typicode.com/users')
    employees = r2.json()

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    res = r.json()
    todo_obj = {}
    todo_arr = []
    for employee in employees:
        for item in res:
            if item.get("userId") == employee.get("id"):
                todo_arr.append(item)
        todo_obj[item.get("userId")] = todo_arr

    """export to json"""
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(todo_obj, file)

    # except Exception as value:
    #     print(value)
