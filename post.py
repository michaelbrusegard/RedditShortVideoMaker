import praw
import random

def retrieve_post(subreddit, client_id, client_secret, user_agent):
    print('Retrieving reddit post...')
    # Create a Reddit instance
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    subreddit_obj = reddit.subreddit(subreddit)

    # Retrieve the top posts of the month
    top_posts = list(subreddit_obj.hot(limit=25))
    
    # Pick a random post from the top 10 posts and return its URL
    random_post = random.choice(top_posts)
    return random_post