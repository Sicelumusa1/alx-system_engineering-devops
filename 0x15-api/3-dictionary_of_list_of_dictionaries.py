#!/usr/bin/python3

import json
import requests

def get_users():
    """
    Fetches a list of users from the jsonplaceholder API

    Returns:
            list: A list of dictionarires containing user data
    """
    url = f"https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()

def get_user_name(user_id, users):
    """
    Fetches the name of the user with the given ID from the list of users

    Args:
        user_id (int): The ID of the user
        users (list): A list of dictionaries containing user data

    Returns:
            str or None: The name of the user if found, otherwise None
    """
    for user in users:
        if user["id"] == user_id:
            return user["username"]
    return None

def export_to_json(todo_data):
    """
    Exports the employee's TODO list data to a JSON file

    Args:
        todo_data (dict): A dictionary containing the employee's TODO list

    Returns:
            None
    """
    filename_json = "todo_all_employees.json"

    with open(filename_json, mode='w') as json_file:
        json.dump(todo_data, json_file, separators=(', ',': '))

def gether_todo_data(users):
    """
    Fetches the TODO list data for all employee's

    Args:
        users (list): A list of dictionaries containing user data
    """
    all_todo_data = {}

    for user in users:
        user_id = user["id"]
        url =  f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response = requests.get(url)
        todos = response.json()

        if todos:
            employee_name = user["username"]
            todo_data = [{"username": employee_name, "task": todo["title"],
                          "completed": todo["completed"]} for todo in todos]
            all_todo_data[str(user_id)] = todo_data

        return all_todo_data

if __name__ == "__main__":
    users = get_users()
    if users:
        todo_data = gether_todo_data(users)
        export_to_json(todo_data)
