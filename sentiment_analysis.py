from alchemyapi import AlchemyAPI
import sys

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

# read from file
tweets_file = open(sys.argv[1], 'rb')
en = 0
es = 0
fr = 0
cat = 0
other = 0

for line in tweets_file:
    response = alchemyapi.sentiment("text", line)
    lang = response["language"]
    if lang == 'catalan':
        cat = cat + 1
    elif lang == 'spanish':
        es = es + 1
    elif lang == 'english':
        en = en + 1
    elif lang == 'french':
        fr = fr + 1
    else :
        other = other + 1
        
print "Total = " + str(en + es + fr + cat + other)