import praw
import pandas as pd

def scrape_reddit(api_keys, subreddit_name, limit=100):
    # Authenticate using PRAW
    reddit = praw.Reddit(client_id=api_keys['client_id'],
                         client_secret=api_keys['client_secret'],
                         user_agent=api_keys['user_agent'])
    
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.new(limit=limit)
    
    post_data = [
        {
            'title': post.title,
            'selftext': post.selftext,
            'created_at': post.created_utc,
            'author': post.author.name if post.author else None
        } for post in posts
    ]
    
    # Save to CSV
    df = pd.DataFrame(post_data)
    df.to_csv('../data/reddit_data.csv', index=False)
    print("Reddit data saved to `data/reddit_data.csv`")

# Replace with your API keys
api_keys = {
    'client_id': 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET',
    'user_agent': 'YOUR_USER_AGENT'
}

scrape_reddit(api_keys, subreddit_name="stocks", limit=100)
