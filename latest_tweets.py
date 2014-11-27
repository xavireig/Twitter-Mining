# Import the necessary methods from tweepy library
import time
import tweepy
from tweepy import OAuthHandler
import sys

# Variables that contains the user credentials to access Twitter API 
CONSUMER_KEY = "type in your key"
CONSUMER_SECRET = "type in your key"
ACCESS_TOKEN = 'type in your key'
ACCESS_SECRET = 'type in your key'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

# screen_name
name = sys.argv[1]

for page in tweepy.Cursor(api.user_timeline, screen_name=name, count=100, since_id=528503683693412352).pages():
    for item in page:
        print item
