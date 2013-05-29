from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from pymongo import Connection

consumer_key = "#####"
consumer_secret = "#####"

access_token = "#####"
access_token_secret = "#####"


connection = Connection('localhost', 27017)
db = connection.tweets
tweets = db.tweets


class MongoListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        print "[%20s] %s" % (tweet['user']['name'], tweet['text'])
        tweets.insert(tweet)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    connection = Connection('localhost', 27017)
    db = connection.tweets
    tweets = db.tweets

    l = MongoListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['audi', 'bmw', 'subaru', 'jeep', 'nissan', 'accura', 'porsche', 'ferarri', 'lamborghini', 'mercedes', 'ford', 'honda'])
