#!/usr/bin/python3
"""
Query the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API"""
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'CustomBot/1.0'})
    params = {"limit": 9}
    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers=headers, params=params)
    res = res.json()
    children = res.get('data', {}).get('children')
    if not children:
        print(None)
    else:
        for child in children:
            print(child.get('data', None).get('title', None))
