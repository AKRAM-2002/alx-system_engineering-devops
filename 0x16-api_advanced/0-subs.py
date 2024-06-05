#!/usr/bin/python3
"""
A Python script to query the Reddit API and returns the number of subscribers
"""
import requests
import sys

def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
