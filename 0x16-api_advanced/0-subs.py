#!/usr/bin/python3

"""
A Method that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit

    Returns:
        number of subscribers or 0 for inalid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Codig in Python"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["data"]["subsribers"]
    else:
        return 0
