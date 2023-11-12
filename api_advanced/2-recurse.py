#!/usr/bin/python3
""" module for function to return top 10 hot posts of a given subreddit """
import requests

def recurse(subreddit, hot_list=[], after=None):
    """ Args:
        subreddit: subreddit name
        hot_list: list of hot titles in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid """
    
    headers = {'User-Agent': 'xica369'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after} if after else {}
    
    response = requests.get(url, headers=headers, params=parameters)

    if response.status_code == 200:
        data = response.json().get('data')
        next_after = data.get('after')
        
        if next_after:
            recurse(subreddit, hot_list, after=next_after)
        
        list_titles = data.get('children')
        hot_list.extend(title_['data']['title'] for title_ in list_titles)
        return hot_list
    else:
        return None

