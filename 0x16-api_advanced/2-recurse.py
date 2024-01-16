#!/usr/bin/python3

"""
Queries the Reddit API recursively and returns a list containing the
titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API recursively and returns a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list of hot articles to append to.
        after (str): the ID of the last post in the previous page
        of results

    Returns:
        list: The list of hot articles for the given subreddit. Returns None
        it the subreddit is invald or the request fails.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Codig in Python"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        hot_list += [post["data"]["title"] for post in data["children"]]
        after = data.get["after"]
        if after:
            recurse(subreddit, hot_list)
        return hot_list
    else:
        print(None)
