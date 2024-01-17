#!/usr/bin/python3
"""
Query the Reddit API and returns the number
of subscribers (not active users,
total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API"""
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'CustomBot/1.0'})
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers=headers)
    res = res.json()
    subscribers = res.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    else:
        return subscribers
