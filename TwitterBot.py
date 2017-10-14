from random  import randint
from time    import sleep
from tweepy  import OAuthHandler, API

infile = open('Facts.txt', 'r')
Facts = []
for line in infile:
    Facts.append(line.strip('\n'))
infile.close()

Hashtags = ['#Quote', '#QuoteOfDDay', '#TamilQuote']

# Credentials to access Twitter API 
ACCESS_TOKEN    = ''
ACCESS_SECRET   = ''
CONSUMER_KEY    = ''
CONSUMER_SECRET = ''

# Initiate the connection to Twitter API
Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)

outfile = open('Log.txt', 'a')
i = 0
while i < len(Facts):
    TwitterBot.update_status(Facts[i]+' '+Hashtags[randint(0,len(Hashtags)-1)]) # Tweet a fact as well as a random hashtag
    outfile.write(str(i)+': '+Facts[i]+'\n') # Keep a log of tweeted facts in case server shuts off
    outfile.flush()
    sleep(randint(3000, 3600)*5) # Tweet every 4-5 hours to prevent bot recognition
    i += 1
