import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



api = tweepy.API(auth)

tweets_file = open("tweet.txt", 'a')
tweets = ""
for page in tweepy.Cursor(api.user_timeline,id='kizuthemaid', count=200).pages(16): #go through 16 pages of 200 tweets (3600 tweets)
	    for status in page:
            tweets += status.text + "\n"
            """
            optional extras:
                you could also do some formatting here. 
                    For example, ">" would display as "&gt;"
                remove retweets by checking if the first 2 letters are "RT"
                remove links via regex
                remove @'s
            """
tweets_file.write("\n" + tweets)
tweets_file.close()
