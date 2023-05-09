#!/usr/bin/python3
"number of subscribers"

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
