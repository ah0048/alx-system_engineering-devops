#!/usr/bin/python3
'''a function to return a list'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''function'''
    url = 'https://api.reddit.com/r/{}/hot/'.format(subreddit)
    headers = {'User-agent': 'alx api advanced task'}
    params = {'after': after}
    resp = requests.get(url=url, headers=headers,
                        params=params, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data.get('data').get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
