import re

from util import ngrams

class Tweet():

	def __init__(self, text):

		self.text = text
		self.split_text = text.split()

		
		# from a machine learning perspective, these are the features
		# that we are going to be working with
		# what features matter?
		self.contains_word_best = self.contains_best(self.split_text)
		self.tags = self.process_tags(self.split_text)
		self.uppercased = self.process_uppercased(self.split_text)
		self.uppercased_2grams = self.process_uppercased_2grams(self.split_text)

		# print(self.uppercased_2grams)




	# the stuff in here really should only be for pre-processing (aka caching)
	# all statistical and counting junk should exist in an exterior class



	# does this tweet have the word "best" in it?
	def contains_best(self, text):
		return "best" in text

	# extract a list of twitter hashtags from this tweet
	def process_tags(self, text):
		return list(filter(lambda x: x.startswith('#'), text))

	# extract all uppercased tokens
	def process_uppercased(self, text):
		return list(filter(lambda x: x[0].isupper(), text))

	# extract all sets of two tokens in a row that are uppercased; looking for proper names of people
	def process_uppercased_2grams(self, text):
		return list(filter(lambda x: x[0][0].isupper() and x[1][0].isupper(), ngrams(text, 2)))



	# def process_link_in_tweet(self, text):
		# m = re.search('https?:\/\/(www\.)?', elem['text']) #'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
        # if m:
        #     m.group(0)
