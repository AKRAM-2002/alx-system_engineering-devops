#!/usr/bin/python3
""" 
A script to query the reddit api and prints the titles of the first 10 hot posts listed for a given subreddit 
"""
import requests

def top_ten(subreddit):
    """ 
        returns the top ten posts for a given subreddit
    """
    
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))        
        
    else:
        return 0
