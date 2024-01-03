#!/usr/bin/python3
"""
Python script that, using this a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    try:
        if int(sys.argv[1]):
            r2 = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                              .format(sys.argv[1]))
            res2 = r2.json()
            employee_name = res2.get("name")

            r = requests.get('https://jsonplaceholder.typicode.com/todos')
            res = r.json()
            total_number_of_tasks = 0
            number_of_done_tasks = 0
            todo = []
            for item in res:
                if item.get("userId") == int(sys.argv[1]):
                    total_number_of_tasks += 1
                    todo.append(item)

            for item in todo:
                if item.get("completed") is True:
                    number_of_done_tasks += 1

            print(f"Employee {employee_name} is done with tasks(\
                  {number_of_done_tasks}/{total_number_of_tasks})")

            for item in todo:
                if item.get("completed") is True:
                    print(f"\t {item.get('title')}")
    except Exception as value:
        print(value)
