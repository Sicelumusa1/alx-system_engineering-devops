#!/usr/bin/python3

import csv
import requests
import sys

"""Gethers information about the employees' TODO list progress"""


def get_user_name(user_id):
    """
    Fetches the user's name fron the jsonplaceholder api based on the user

    Args:
        user_id (int): Id of the user

    Returns:
        str or None: The name of the user if found, otherwise None.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    user_data = response.json()

    return user_data.get("username", None)

def export_to_csv(employee_id, todos):
    """
    Exports the employee's to do list data to a csv file

    Args:
        employee_id (int): The Id of the employee
        todos (list): A list of dictionaries containing the employee's
                        TODO list data
    Returns:
            None
    """
    filename = f"{employee_id}.csv"
    fieldnames = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]

    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
       #  writer.writerow(fieldnames)

        for todo in todos:
            username = get_user_name(todo["userId"])
            task_completed_status = str(todo["completed"])
            task_title =  todo["title"]

            writer.writerow([todo["userId"], username, task_completed_status,
                            task_title])

def employee_todo_progess(employee_id):
    """
    Gethers information about the employees' TODO list progress

    Args:
        employee_id(int): The ID of an employee

    Returns:
            information about his/her TODO list progress.
    """

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    if todos:
        export_to_csv(employee_id, todos)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_todo_progess(employee_id)
