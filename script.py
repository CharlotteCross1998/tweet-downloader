import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



api = tweepy.API(auth)

public_tweets = api.user_timeline('kizuthemaid')
for tweet in public_tweets:
    print(tweet.text)
    tweets = open("tweet.txt", 'a')
    tweets.write(tweet.text)
    tweets.write('\n')
