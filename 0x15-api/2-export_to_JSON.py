#!/usr/bin/python3
""" module doc """
import json
import requests
import sys


def main():
    """main doc"""
    url = "https://jsonplaceholder.typicode.com"
    EmployeeID = sys.argv[1]

    # urls:
    user_data = f"{url}/users/{EmployeeID}"
    user_tasks = f"{url}/todos?userId={EmployeeID}"
    # data
    userName = requests.get(user_data).json().get("username")
    # export to json
    with open(f"{EmployeeID}.json", "w") as f:
        data = {
            EmployeeID: [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": userName,
                }
                for task in requests.get(user_tasks).json()
            ]
        }
        json.dump(data, f)


if __name__ == "__main__":
    main()
