#!/usr/bin/python3
"""Gethers information about the employees' TODO list progress"""

import json
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


def export_to_json(employee_id, todos):
    """
    Exports the employee's TODO list data to a JSON file

    Args:
        employee_id (int): The ID of the employee
        todo (list): A list of dictionaries with employee's TODO
                    list data
    Returns:
            None
    """
    employee_name = get_user_name(employee_id)
    filename_json = f"{employee_id}.json"

    tasks_json = [{"task": todo["title"], "completed": todo["completed"],
                   "username": employee_name} for todo in todos]
    user_tasks = {str(employee_id): tasks_json}

    with open(filename_json, mode='w') as json_file:
        json.dump(user_tasks, json_file, separators=(', ', ': '))


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
        export_to_json(employee_id, todos)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_todo_progess(employee_id)
