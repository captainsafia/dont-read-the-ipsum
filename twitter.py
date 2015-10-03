import time
import os
import tweepy
import datetime
import pprint
import string
import random
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#   print tweet._json['text']

#officialjaden

def get_tweets_from_user(number, user):
	tweets = api.user_timeline(id = user, count = number )
	all_tweets = ''
	for tweet in tweets:
		all_tweets += (' ' + tweet.text + ' ')
	return all_tweets



def get_replies_to_user(number, user):
	all_replies = ''
	replies = api.search(q = user, count = number)
	for tweet in replies:
		if tweet.text not in all_replies:
			all_replies += (tweet.text)
	return all_replies

def clean_up_text(text):
	exclude = set(string.punctuation)

	exclude_words = ['RT', 'MT']
	word_list = text.split(" ")
	word_list = filter(lambda word: word not in exclude_words, word_list)
	word_list = filter(lambda word: not word.startswith('@'), word_list)
	word_list = filter(lambda word: not word.startswith("http"), word_list)
	cleaned_text = ''
	for word in word_list:
		cleaned_text += (' ' + word + ' ')
	cleaned_text = "".join(char for char in cleaned_text if char not in exclude)
	return cleaned_text



	return cleaned_text

def get_jumbled_text(text):
    """
    Return jumpled version of text.
    """
    text = text.split(" ")
    jumbled = ""

    while len(text) > 0:
        word = random.choice(text)
        del text[text.index(word)]
        jumbled += (" " + word + " ")

    return jumbled.strip()

# print get_tweets_from_user(500, 'officialjaden')
# print get_replies_to_user(500, 'officialjaden')

#remove pound sign, punctuation, URLs
