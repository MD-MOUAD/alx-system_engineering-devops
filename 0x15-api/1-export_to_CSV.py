#!/usr/bin/python3
""" module doc """
import requests
import sys


def json_response(url, data=None):
    """get response using get request"""
    if data:
        if isinstance(requests.get(url).json(), list):
            return [result.get(data) for result in requests.get(url).json()]
        else:
            return requests.get(url).json().get(data)
    else:
        return requests.get(url).json()


def main():
    """main function"""

    url = "https://jsonplaceholder.typicode.com"
    EmployeeID = sys.argv[1]
    # urls:
    user_data = f"{url}/users/{EmployeeID}"
    user_tasks = f"{url}/todos?userId={EmployeeID}"

    # data:
    USER_NAME = json_response(user_data, "username")
    TOTAL_TASKS = json_response(user_tasks)

    # export to CSV
    with open(f'{EmployeeID}.csv', 'w') as f:
        for task in TOTAL_TASKS:
            TASK_STATUS = task.get("completed")
            TASK_TITLE = task.get("title")
            f.write('\"{}\",\"{}\",\"{}\",\"{}\"\n'.format(
                EmployeeID, USER_NAME, TASK_STATUS, TASK_TITLE
            ))


if __name__ == "__main__":
    main()
