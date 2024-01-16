#!/usr/bin/python3

"""
Queries the Reddit API and prints the titles of the first 10 hot
posts
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Codig in Python"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        for post in response.json()["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
