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

api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

print api.rate_limit_status()['resources']['users']['/users/lookup']['remaining']

# file with user IDs
users_file = open(sys.argv[1], 'rb')
data_file = open(sys.argv[2], 'w')

data_file.write("location; statuses_count; friends_count; followers_count; lang; created at \n")

i = 0
users = range(100)

for line in users_file:
    current_line = line.replace('\n', '').replace('\r', '')
    users[i] = current_line
    i = i + 1
    if i == 100:
        i = 0;
        print "API remaining calls: " + str(api.rate_limit_status()['resources']['users']['/users/lookup']['remaining'])
        if (api.rate_limit_status()['resources']['users']['/users/lookup']['remaining'] == 115):
            print ("Number of calls exceeded, sleeping for 15 min")
            time.sleep(60*15)
        try:
            for user in api.lookup_users(users):           
                text = user['location'] + "; " + str(user['statuses_count']) + "; " + str(user['friends_count']) + "; " + str(user['followers_count']) + "; " + user['lang']+ "; " + user['created_at'] + "\n"
                text2 = text.encode('utf-8')
                data_file.write(text2)
        except tweepy.TweepError as e:
            print e
            
data_file.close()
