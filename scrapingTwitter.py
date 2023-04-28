# scrapingTwitter.py
import tweepy
import csv

# Twitter API credentials
consumer_key = "<your consumer key>"
consumer_secret = "<your consumer secret>"
access_key = "<your access key>"
access_secret = "<your access secret>"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Define search query and parameters
query = "cybersecurity OR infosec OR data breach"
max_tweets = 100
searched_tweets = [tweet for tweet in tweepy.Cursor(api.search_tweets, q=query).items(max_tweets)]

# Write tweets to a CSV file
with open('cybersecurity_news.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Tweet ID', 'Username', 'Tweet Text', 'Location', 'Retweet Count', 'Favorite Count'])

    for tweet in searched_tweets:
        writer.writerow([tweet.id_str, tweet.user.screen_name, tweet.text, tweet.user.location, tweet.retweet_count, tweet.favorite_count])

