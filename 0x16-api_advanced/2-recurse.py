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
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKid/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()["data"]
        hot_list += [post["data"]["title"] for post in data["children"]]
        after = data["after"]
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        print(None)
