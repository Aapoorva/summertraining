import tweepy
from textblob import TextBlob
import string
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

customer_key = 'CaIAxeFfXhO6mQnKaX44X9u77'
customer_secret = 'zUNYkmJO4e2YxXie38KW5h37yIEJ65oBwehSf3O5J2LzHPFaSF'

access_token = '828271353451204608-aOWCTeKZ5acwuU1POyUH4Fp6MvtHJ1Z'
access_token_secret = '6LN3CB7nkpyRJjwkfiKCbKpe4QmglV4VCqJCf1mC8pfrN'

#authenticating developer account
auth = tweepy.OAuthHandler(customer_key,customer_secret)

#setting api access keys
auth.set_access_token(access_token,access_token_secret)

#connecting to api
api = tweepy.API(auth)

#fetching tweets for a topic
tweets = api.search('@realDonaldTrump',count=20)

tweet_polarity = []
#parsing fetched tweets
for tweet in tweets :
	#reading tweet text
	tweet_text = tweet.text
	
	#cleaning tweet text
	#removing punctuations
	tweet_text_non_punc = [i for i in tweet_text if i not in string.punctuation]
	tweet_text_non_punc = ''.join(tweet_text_non_punc)

	#removing stopwords
	tweet_text_cleaned = [i for i in tweet_text_non_punc.strip().split() if i not in stopwords.words('english')]
	tweet_text_cleaned = ' '.join(tweet_text_cleaned)

	#analysing sentiments
	tweet_sentiment = TextBlob(tweet_text_cleaned).sentiment
	#storing polarity
	if tweet_sentiment.polarity > 0 :
		tweet_polarity.append('positive')
	elif tweet_sentiment.polarity == 0 :
		tweet_polarity.append('neutral')
	else :
		tweet_polarity.append('negative')

#calculating percentages
total_tweets = len(tweet_polarity)
positive_count = tweet_polarity.count('positive')
neutral_count = tweet_polarity.count('neutral')
negative_count = tweet_polarity.count('negative')

# positive_percent = (positive_count/total_tweets)*100
# neutral_percent = (neutral_count/total_tweets)*100
# negative_percent = (negative_count/total_tweets)*100

#ploting data
# create data
lables=['positive','neutral','negative']
# data=[positive_percent,neutral_percent,negative_percent]
data=[positive_count,neutral_count,negative_count]
# autopct=
explode=[0.05,0.05,0.05]
color=['g','b','r']

plt.title('Sentiment Analysis') 

# Create a pieplot
plt.pie(data,labels=lables,explode=explode,colors=color,autopct='%1.1f%%',pctdistance=0.5)
#plt.show()
 
# add a circle at the center - to show white portion
my_circle=plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
 
plt.show()