#!/usr/bin/python3
"""
Recursive function that queries the Reddit
API and returns a list containing the titles
of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursive function to retrieve titles
    of hot articles from Reddit API.
    """
    if hot_list is None:
        hot_list = []

    # Base case: if subreddit is not valid, return None
    if subreddit is None:
        return None

    try:
        # Construct the URL for the Reddit API request
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        params = {'limit': 100, 'after': after}
        headers = {'User-Agent': 'CustomBot/1.0'}

        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # Check if the response contains posts
        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']

            # Extract titles from the current page and add them to the hot_list
            titles = [child['data']['title'] for child in children]
            hot_list.extend(titles)

            # Recursive call with the next 'after' parameter
            next_after = data['data']['after']
            if next_after:
                recurse(subreddit, hot_list, next_after)

        # If no results are found, return None
        elif not hot_list:
            return None

        return hot_list

    except Exception as e:
        print(f"Error: {e}")
        return None
