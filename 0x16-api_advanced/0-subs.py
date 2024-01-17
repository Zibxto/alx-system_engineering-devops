#!/usr/bin/python3
"""
Query the Reddit API and returns the number
of subscribers (not active users,
total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API"""
    try:
        res = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={'User-Agent': 'CustomBot/1.0'})

        if res.status_code == requests.codes.ok:
            res = res.json()
            if 'subscribers' in res['data']:
                return res['data']['subscribers']
            else:
                return 0
        else:
            return 0
    except Exception:
        return 0
