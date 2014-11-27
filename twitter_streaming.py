# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import sys

# Variables that contains the user credentials to access Twitter API 
CONSUMER_KEY = "type in your key"
CONSUMER_SECRET = "type in your key"
ACCESS_TOKEN = 'type in your key'
ACCESS_SECRET = 'type in your key'

# Tag to capture via parameter
tag = sys.argv[1]

# global counters
tweets_per_file = 0
max_tweets_per_file = 1000
file_number = 0
start_time = datetime.datetime.now()

# data files details
data_folder = './data/'
data_file_name = 'data0'
f = open(data_folder + data_file_name, 'w')
    
# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        
        global f, data_path, tweets_per_file, file_number        
        
        f.write(data)
        tweets_per_file = tweets_per_file + 1

        # check if we need to create a new data file
        if (tweets_per_file == max_tweets_per_file):
            f.close()
            file_number = file_number + 1
            data_file_name = 'data' + str(file_number)
            f = open(data_folder + data_file_name, 'w')
            tweets_per_file = 0
            print "# data files: " + str(file_number + 1)

        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':   

    print "Starting the capture of tweets with '" + tag +"' at " + str(start_time)
    print "# data files: 1"

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=[tag])
