#!/usr/bin/python3
'''a function to return  the number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''the function'''
    url = 'https://api.reddit.com/r/{}/about'.format(subreddit)
    headers = {'User-agent': 'alx api advanced task'}
    resp = requests.get(url=url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        return (data['data']['subscribers'])
    else:
        return 0
