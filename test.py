__author__ = 'Monosrija'

from TwitterBot import BotFeatures

task = BotFeatures()

user1 = task.get_user(screen_name = '@LexerSpeaks')
user2 = task.get_user(screen_name = '@JohnshonKnows')


#1. Find top 10 tweets in english language with a specified query/hashtag and from a given location and retweet
#task.reTweet_by_hashloc("sunset at sea", "40.7128,-74.0059,50km", n=10, lang='en')

# #2.follow a user
#task.follow_user(user2.screen_name)
#
# #3. Send message to a user
#task.send_message(user2.screen_name, "Welcome to Twitter")
#
# #4. Reply to recent tweets of a given user
#task.reply_to_status(user2.screen_name)
#
# #5. Given a user retweet his recent tweets
#task.retweet_by_user(user2.screen_name, 1)
#
# #6. Follow 'n' no of users whose tweets matched the search query
task.follow_many_users("#EuroCup", 1)
