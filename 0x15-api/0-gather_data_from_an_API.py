#!/usr/bin/python3
"""Gethers information about the employees' TODO list progress"""
import requests
import sys


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

    return user_data.get("name", None)


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
        completed_todos = [todo for todo in todos if todo["completed"]]
        employee_name = get_user_name(employee_id)
        num_completed_todos = len(completed_todos)
        num_total_todos = len(todos)
        print(f"Employee {employee_name} is done with tasks "
              f"({num_completed_todos}/{num_total_todos}):")
        for todo in completed_todos:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_todo_progess(employee_id)
