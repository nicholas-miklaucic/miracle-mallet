"""This file creates a Reddit bot to invert the gender of posts in the MRP subreddit."""

import configparser
from datetime import datetime

import praw

from gender_invert import change_text as invert

config = configparser.ConfigParser()

config.read("credentials.conf")

reddit = praw.Reddit(
    **config['Account']
)

mrp = reddit.subreddit('MarriedRedPill')
mbp = reddit.subreddit('TheMarriedBluePill')

def make_inverted_post(submission):
    if not submission.is_self:
        return
    
    new_post = mbp.submit(
        title=invert(submission.title),
        selftext=invert(submission.selftext),
        nsfw=submission.over_18,
        send_replies=False,
    )


def update():
    with open('last-updated', 'r') as infile:
        last_updated = int(infile.read())

    now = int(datetime.utcnow().timestamp())
        
    for sub in mrp.new(limit=1024):
        if last_updated < sub.created_utc:
            print(sub.title)
            make_inverted_post(sub)

    with open('last-updated', 'w') as outfile:
        outfile.write(str(now))
