import tweepy
import pandas as pd

def scrape_twitter(api_keys, query, count=100):
    # Authenticate using Tweepy
    auth = tweepy.OAuth1UserHandler(api_keys['consumer_key'], api_keys['consumer_secret'],
                                    api_keys['access_token'], api_keys['access_token_secret'])
    api = tweepy.API(auth)
    
    # Fetch tweets
    tweets = api.search_tweets(query, count=count, lang='en')
    tweet_data = [
        {
            'tweet': tweet.text,
            'created_at': tweet.created_at,
            'user': tweet.user.screen_name
        } for tweet in tweets
    ]
    
    # Save to CSV
    df = pd.DataFrame(tweet_data)
    df.to_csv('../data/twitter_data.csv', index=False)
    print("Twitter data saved to `data/twitter_data.csv`")

# Replace with your API keys
api_keys = {
    'consumer_key': 'YOUR_CONSUMER_KEY',
    'consumer_secret': 'YOUR_CONSUMER_SECRET',
    'access_token': 'YOUR_ACCESS_TOKEN',
    'access_token_secret': 'YOUR_ACCESS_TOKEN_SECRET'
}

scrape_twitter(api_keys, query="stock market prediction", count=100)
