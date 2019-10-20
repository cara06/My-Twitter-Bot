import tweepy
from time import sleep
from credentials import *

# Edit this confif file as you like

# This is hashtag which Twitter bot will search and retweet. You can edit this with any hashtag .For example : '#javascript'

QUERY = '#100Daysofcode'

# Twitter bot setting for liking Tweets
LIKE = True 

# Twitter bot setting for following user who tweeted
FOLLOW = True

# Twitter bot sleep time settings in seconds. For example SLEEP_TIME = 300 means 5 minutes.
# you can decrease it or increase it as you like.Please,use large delay if you are running bot all the time  so that your account does not get banned.

SLEEP_TIME = 10

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Twitter bot which retweets,like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    try:
        print('\n\n >>> Tweet by: @' + tweet.user.screen_name +' <<<')
        print(tweet.text)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        if LIKE:
            tweet.favorite()
            print('Liked the tweet')

        # Follow the user who tweeted
        #check that bot is not already following the user
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')

        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
