__author__ = 'Monosrija'

import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

class BotFeatures:

    def __init__(self):
        try:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            auth.secure = True
            api = tweepy.API(auth)
            api.verify_credentials()
            self.api =api
        except tweepy.TweepError as e:
            return e.reason

    def get_user(self, screen_name):
        try:
            return self.api.get_user(screen_name = screen_name)
        except tweepy.TweepError as e:
            print e

    def reTweet_by_hashloc(self, query, geo, n, lang):
        for tweet in tweepy.Cursor(self.api.search, geocode=geo, q=query, lang=lang).items(n):
            try:
                if tweet.retweeted is False:
                    tweet.retweet()
            except tweepy.TweepError as e:
                print e
            except StopIteration:
                break


    def send_message(self, user, msg):
        try:
            self.api.send_direct_message(screen_name=user,text=msg)
        except tweepy.TweepError as e:
                print e

    def follow_user(self, user):
        try:
            self.api.create_friendship(screen_name =user)
        except tweepy.TweepError as e:
                print e

    def reply_to_status(self, user):
        try:
            tweets=self.api.user_timeline(user, count =1)
            for tweet in tweets:
                print tweet
                try:

                    status=self.api.get_status(tweet.id_str)
                    txt = "welcome " +user
                    self.api.update_status(status=txt, in_reply_to_status_id=status.id)
                except tweepy.TweepError as e:
                    print e
                except StopIteration:
                    break
        except tweepy.TweepError as e:
                    print e

    def retweet_by_user(self, user,n):
        tweets=self.api.user_timeline(id=user, count=n)
        for tweet in tweets:
            try:
               if tweet.retweeted is False:
                    tweet.retweet()
            except tweepy.TweepError as e:
                print e
            except StopIteration:
                break

    def follow_many_users(self, search_query, n):
        for tweet in tweepy.Cursor(self.api.search, q=search_query, lang='en').items(n):
            try:
                self.follow_user(tweet.user.screen_name )
                print tweet.user.screen_name
            except tweepy.TweepError as e:
                print e

