#!/usr/bin/python3
"""
Module documentaion
"""
import requests

headers = {"User-Agent": "My Reddit Subscribers Checker"}


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers (total subscribers) for the subreddit.
        Returns 0 if invalid.
    """
    # URL for the subreddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'My Reddit Subscribers Checker'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract and return number of subscribers
        return data['data']['subscribers']
    else:
        # Invalid subreddit or other error occurred
        return 0
