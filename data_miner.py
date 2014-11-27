import json
import pandas as pd
import matplotlib.pyplot as plt
import codecs
from csv import writer

tweets_data_path = './twitter_data.txt'
csv_data_path = './twitter_data.csv'

tweets_data = []
tweets_file = open(tweets_data_path).read()

with codecs.open(tweets_data_path, 'r', encoding='utf-8') as in_file, open(csv_data_path, 'w') as out_file:
	
    print >> out_file, 'tweet_id, tweet_time, tweet_author, tweet_author_id,    tweet_language, tweet_geo, tweet_text'
    csv = writer(out_file)
	
    for line in in_file:
        try:
            tweet = json.loads(line, encoding='utf-8')
            tweets_data.append(tweet)
            # Pull out various data from the tweets
	    row = (
                tweet['id'],                    # tweet_id
                tweet['created_at'],            # tweet_time
                tweet['user']['screen_name'],   # tweet_author
                tweet['user']['id_str'],        # tweet_authod_id
                tweet['lang'],                  # tweet_language
                tweet['geo'],                   # tweet_geo
                tweet['text']                   # tweet_text
            )
	    values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
            csv.writerow(values)

        except:
            continue

print json.dumps(tweets_data, indent=4)
print "Total tweets: " + str(len(tweets_data))

