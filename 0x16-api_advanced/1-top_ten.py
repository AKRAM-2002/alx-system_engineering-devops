#!/usr/bin/python3
""" 
A script to query the reddit api and prints the titles of the first 10 hot posts listed for a given subreddit 
"""
import requests

def top_ten(subreddit):
    """ 
        returns the top ten posts for a given subreddit
    """

    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
