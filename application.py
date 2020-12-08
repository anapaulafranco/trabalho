# coding=utf-8
import sys
from flask import Flask
import tweepy
import time
import json

application = Flask(__name__)


# print(phrase_to_search);

consumer_key = 'j6NjkfP4PxZxR81tBsCKd8jEF'
consumer_secret = 'GhPHxnDnTLzeY6ejbMwhxrTd0A7a019Pc7nxRC2azUtdLckuBK'
access_token = '344908066-3gb7pZfLeXkz1LH9djEaACrqoshzkOd9k9uBpvd3'
access_token_secret = '4gcw6dL1H3fM0p0L7bqyP9xYtIXNwUgL5YJzFbnhG330o'

g = []
 

@application.route("/")
def hello():
    return "<h1>TRABALHO DE CLOUD 44BDT</h1><h3>AWS CODE PIPELINE - ELASTIC BEANSTALK</h3><p>Esta aplicacao lista os Trending Topics do Twitter a cada clique no botão abaixo</p><p><a href='getTrendingTopics'>Ver Trending Topics</a></p>"


@application.route("/getTrendingTopics")
def gettingTopics():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    BRAZIL_WOE_ID = 23424768
    brazil_trends = api.trends_place(BRAZIL_WOE_ID)
    trends = json.loads(json.dumps(brazil_trends, indent=1))
    
    tt = []
    for trend in trends[0]["trends"]:
        tt.append("<br>"+trend["name"])

    return "<h1>TRABALHO DE CLOUD 44BDT</h1><h3>AWS CODE PIPELINE - ELASTIC BEANSTALK</h3><p>Esta aplicacao lista os Trending Topics do Twitter a cada clique no botão abaixo</p><p><a href='getTrendingTopics'>Ver Trending Topics</a></p>"+ '\n'.join(tt)


if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0', debug=True)
