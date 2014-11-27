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

print api.rate_limit_status()['resources']['followers']['/followers/ids']['remaining']
print api.rate_limit_status()['resources']['friends']['/friends/ids']['remaining']

# file with user IDs
users_file = open(sys.argv[1], 'rb')
nodes_file = open(sys.argv[2], 'w')

followers = 0
friends = 0

# for each user ID
for line in users_file:
    # delete any carriage return
    current_user = line.replace('\n', '').replace('\r', '')
    print ("Current user: " + current_user)
    if (api.rate_limit_status()['resources']['followers']['/followers/ids']['remaining'] == 0):
        print ("Followers limit exceeded, sleeping for 15 min")
        time.sleep(60*15)
    
    # pages of followers of current_user
    try:
        for page in tweepy.Cursor(api.followers_ids, id=current_user).pages():
            if (api.rate_limit_status()['resources']['followers']['/followers/ids']['remaining'] == 0):
                print ("Followers limit exceeded, sleeping for 15 min")
                time.sleep(60*15)
            else :
                # print each ID
                for item in page:
                    followers = followers + 1
                    text = current_user + ';' + str(item) + '\n'
                    nodes_file.write(text)
                if len(page) == 5000: time.sleep(60)
    except tweepy.TweepError as e:
        print "Error - Skipping" + current_user
        
    if (api.rate_limit_status()['resources']['friends']['/friends/ids']['remaining'] == 0):
        print ("Friends limit exceeded, sleeping for 15 min")
        time.sleep(60*15)
           
    try:
        # pages of followers of current_user
        for page in tweepy.Cursor(api.friends_ids, id=current_user).pages():
            if (api.rate_limit_status()['resources']['friends']['/friends/ids']['remaining'] == 0):
                print ("Followers limit exceeded, sleeping for 15 min")
                time.sleep(60*15)
            else :
                # print each ID
                for item in page:
                    friends = friends + 1
                    text = current_user + ';' + str(item) + '\n'
                    nodes_file.write(text)
                if len(page) == 5000: time.sleep(60)
    except tweepy.TweepError as e:
        print "Error - Skipping" + current_user

file.close()

