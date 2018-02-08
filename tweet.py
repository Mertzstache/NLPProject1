import re

from util import ngrams

class Tweet():

	def __init__(self, text):

		self.text = text
		self.text_lower = text.lower()

		self.split_text = self.text.split()
		self.split_text_lower = self.text_lower.split()

		
		# from a machine learning perspective, these are the features
		# that we are going to be working with
		# what features matter?
		self.contains_word_best = self.__contains_best(self.split_text)
		self.tags = self.__process_tags(self.split_text)
		self.uppercased = self.__process_uppercased(self.split_text)
		self.uppercased_2grams = self.__process_uppercased_2grams(self.split_text)



	def __str__(self):
		return self.text


	# ------------------------------------------------------------------------
	# the stuff in here really should only be for pre-processing (aka caching)
	# all statistical and counting junk should exist in an exterior class
	# ------------------------------------------------------------------------



	# does this tweet have the word "best" in it?
	def __contains_best(self, text):
		return "best" in text

	# extract a list of twitter hashtags from this tweet
	def __process_tags(self, text):
		return list(filter(lambda x: x.startswith('#'), text))

	# extract all uppercased tokens
	def __process_uppercased(self, text):
		return list(filter(lambda x: x[0].isupper(), text))

	# extract all sets of two tokens in a row that are uppercased; looking for proper names of people
	def __process_uppercased_2grams(self, text):
		return list(filter(lambda x: x[0][0].isupper() and x[1][0].isupper(), ngrams(text, 2)))


	# copied from old main file. not working as it stands
	# def process_link_in_tweet(self, text):
		# m = re.search('https?:\/\/(www\.)?', elem['text']) #'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
		# if m:
		#     m.group(0)




	# --------------------------------------------------------------------------------------
	# everything below this line should be considered one-off, in other words you're pretty 
	# sure this function is only going to be called one or two times. This saves us memory 
	# (maybe we don't care, we can just download more?) https://downloadmoreram.com/
	# --------------------------------------------------------------------------------------

	# let's say we're looking for the word host, well maybe hostess is the same
	# thing. this checks the beginning of each token for a substring E.G. "host"
	# and returns true as soon as it finds it
	#
	# so ['the', 'hostess', 'is', ...] =>  True
	# ['the', 'best', 'phost'] => None
	def contains_word_partial(self, fragment):
		for token in self.split_text_lower:
			if token.startswith(fragment.lower()):
				return True

		return None