#!/usr/bin/python3
'''a function to return the first 10 hot posts'''
import requests


def top_ten(subreddit):
    '''the function'''
    url = 'https://api.reddit.com/r/{}/hot/'.format(subreddit)
    headers = {'User-agent': 'alx api advanced task'}
    params = {'limit': 10}
    resp = requests.get(url=url, headers=headers,
                        params=params, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        posts = data.get('data', {}).get('children', [])
        if posts is None:
            print('None')
            return
        for post in posts:
            print(post['data']['title'])
    else:
        print('None')
