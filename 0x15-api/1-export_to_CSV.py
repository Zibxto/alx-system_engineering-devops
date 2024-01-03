#!/usr/bin/python3
"""
Extends your Python script to export data in the CSV format.
"""
import requests
import sys

if __name__ == "__main__":
    try:
        if int(sys.argv[1]):
            r2 = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                              .format(sys.argv[1]))
            res2 = r2.json()
            employee_username = res2.get("name")

            r = requests.get('https://jsonplaceholder.typicode.com/todos')
            res = r.json()
            todo = []
            for item in res:
                if item.get("userId") == int(sys.argv[1]):
                    todo.append(item)

            for item in todo:
                print('"{}",{},{},{}'. format(item.get("userId"),
                                              employee_username,
                                              item.get("completed"),
                                              item.get("title")))

    except Exception as value:
        print(value)
