#!/usr/bin/python3
"""
Extends your Python script to export data in the json format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    try:
        if int(sys.argv[1]):
            r2 = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                              .format(sys.argv[1]))
            res2 = r2.json()
            employee_username = res2.get("username")

            r = requests.get('https://jsonplaceholder.typicode.com/todos')
            res = r.json()
            todo = []
            for item in res:
                if item.get("userId") == int(sys.argv[1]):
                    todo.append(item)
            """export to json"""
            todo_to_arr = []
            todo_to_json = {}
            for item in todo:
                item_obj = {}
                item_obj["task"] = item.get("title")
                item_obj["completed"] = item.get("completed")
                item_obj["username"] = employee_username

                todo_to_arr.append(item_obj)

            todo_to_json[sys.argv[1]] = todo_to_arr

            filename = "{}.json".format(sys.argv[1])
            with open(filename, "w") as file:
                json.dump(todo_to_json, file)

    except Exception as value:
        print(value)
