#!/usr/bin/python3
""" 
A script that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
"""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """ 
        a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list

