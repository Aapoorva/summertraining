import tweepy

customer_key = 'XXXXXXXXXXXXXXXXXXXXXX'
customer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'

access_token = 'XXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#authenticating developer account
auth = tweepy.OAuthHandler(customer_key,customer_secret)

#setting api access keys
auth.set_access_token(access_token,access_token_secret)

#connecting to api
api = tweepy.API(auth)

#fetching tweets for a topic
tweets = api.search('#deadpool',count=10000)
