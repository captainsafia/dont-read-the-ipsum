#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import json
import string
import random
from config import *

def get_json(search_term):
	request = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=%s&api-key=%s' % (search_term, NYT_KEY)
	response = urllib.request.urlopen(request)
	str_response = response.readall().decode('utf-8')
	obj = json.loads(str_response)
	return obj
	#print(obj['response']['docs'])

def json_to_string(json):
	first_paragraphs = ''
	for doc in json['response']['docs']:
		if doc.get('lead_paragraph'):
			first_paragraphs += (doc.get('lead_paragraph') + ' ')
		#print(doc['lead_paragraph'])
	#print(first_paragraphs)
	return first_paragraphs


def clean_up_text(text,expected):
	#print(text)
	exclude = set(string.punctuation)
	re_include = ['/','\\',"'","(",")",'~','`']
	for char in re_include:
		exclude.remove(char)
	exclude_words = ['RT', 'MT',' (',') ']
	text = text.strip()
	word_list = text.split(" ")
	word_list = filter(lambda word: word not in exclude_words, word_list)
	word_list = filter(lambda word: not word.startswith('@'), word_list)
	#ASK SAFIA ABOUT THE PARENS AND HOW TO DETECT THEM AT THE END OR
	#BEGINNING OF THIS LOOP HERE. THINK OF THE ¯\(ツ)/¯
	word_list = (word for word in word_list if not word.startswith("http"))
	cleaned_text = ''
	counter = 0
	for word in word_list:
		counter += 1
		cleaned_text += (word + ' ')
		if counter > expected:
			break
	cleaned_text = "".join(char for char in cleaned_text if char not in exclude)
	#print(cleaned_text)
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
        jumbled += (word + " ")
    return jumbled.strip()

# jason = get_json('alpaca')
# gerbil = json_to_string(jason)
# wash = clean_up_text(gerbil)
# shuffle = get_jumbled_text(wash)
# print(shuffle)


