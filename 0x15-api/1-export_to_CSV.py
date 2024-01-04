#!/usr/bin/python3
"""
Extends your Python script to export data in the CSV format.
"""
import csv
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
            """export to csv"""
            filename = "{}.csv".format(sys.argv[1])
            with open(filename, "w") as file:
                fieldnames = ["USER_ID", "USERNAME",
                              "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                writer = csv.DictWriter(file, fieldnames=fieldnames,
                                        quoting=csv.QUOTE_ALL)
                for item in todo:
                    writer.writerow({"USER_ID": item.get("userId"),
                                     "USERNAME": employee_username,
                                     "TASK_COMPLETED_STATUS": item.get(
                                         "completed"),
                                     "TASK_TITLE": item.get("title")})

    except Exception as value:
        print(value)
