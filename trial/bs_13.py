import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import codecs 
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'IHOLgbAUmqxiTLG3w1zxuFS27'
        consumer_secret = 'gt21ZTTgA2lotgzvvX6YAJGMQzzmkEQHa60O06U96qZ7Ico0kc'
        access_token = '923586299642003456-FhcN1etzIBTAruen8mVbB4SPg3RJtCJ'
        access_token_secret = 'kKEetDdyd9FjfFd0b2S0fO5eUXPiFuFi135BHaTxrtyvf'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        
        
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
	print analysis
        fs3=str(analysis)
	gfile3=open('anchors3.txt','w')
	gfile3.write(fs3)
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
	    #print 'postive',analysis
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
	    #print 'neut',analysis
        else:
            return 'negative'
	    #print 'neg',analysis
 
    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)
	    fs=str(fetched_tweets)
	    gfile2=open('anchors.txt','w')
	    gfile2.write(fs)
	    #print 'one', fetched_tweets[0]
	    #print 'second',fetched_tweets
            i =0
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
                print i
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
		#print parsed_tweet
		exam=tweet.text
		#print "exammm",exam
		#fs2=str(exam)
		
		#exam2=codecs.encode(exam, 'translit/one').encode('ascii', 'replace')
		#exam2= u"{}".format(exam2)
	        gfile22=open('anchors2.txt','w')
	        gfile22.write(exam.encode('utf-8'))
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
		checksen=self.get_tweet_sentiment(tweet.text)
		print checksen
                i +=1
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 
def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = 'Donald Trump', count = 20)
    #print tweets
    print '\n'
    #print tweets[0]
    print 'tweets(len)',len(tweets)
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    
    # percentage of neutral tweets
    #print("Neutral tweets percentage: {} % \
      #  ".format(100*len(tweets - ntweets - ptweets)/len(tweets)))
    print("Neutral tweets percentage: {} % \
	".format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets)))


 
    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
 
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
 
if __name__ == "__main__":
    # calling main function
    main()
