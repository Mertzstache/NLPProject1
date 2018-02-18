import re
import spacy
# from nltk import word_tokenize

from util import ngrams


nlp = spacy.load('en')


class Tweet():

	spacy_parse = None

	def __init__(self, text):

		self.text = text

		# self.nltk_text = word_tokenize(text)

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
		self.uppercased_runs = self.__process_uppercased_runs(self.split_text)


	def __str__(self):
		return self.text

	# WARNING: do not call this on many tweets, or the runtime will blow up
	# this should only be used on heavily filtered subsets
	def get_named_entities(self):
		self.__process_parse(self.text)
		return [(ent.text, ent.label_) for ent in self.spacy_parse.ents]


	def re_findall(self, pattern):
		return re.findall(pattern, self.text)

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

	# returns a list of 2grams from this tweet
	def __process_2grams(self, text):
		return list(ngrams(text, 2))

	# extract all sets of two tokens in a row that are uppercased; looking for proper names of people
	def __process_uppercased_2grams(self, text):
		return list(filter(lambda x: x[0][0].isupper() and x[1][0].isupper(), ngrams(text, 2)))

	# get a list of every run of uppercased tokens greater than 1
	def __process_uppercased_runs(self, text):
		return self.re_findall(r'(\b[A-Z][\w,-]*(?: +\b[A-Z][\w,-]*)+)')


	# should not be called on every tweet or the program will never finish. only small subsets
	# runs the spacy parser on the text of this tweet.
	def __process_parse(self, text):
		if self.spacy_parse == None:
			self.spacy_parse = nlp(text)


	# copied from old main file. not working as it stands
	# def process_link_in_tweet(self, text):
		# m = re.search('https?:\/\/(www\.)?', elem['text']) #'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
		# if m:
		#     m.group(0)




	# --------------------------------------------------------------------------------------
	# everything below this line should be considered one-off, in other words you're pretty
	# sure this function is only going to be called one or two times (for a particular arglist.
	# This saves us memory (maybe we don't care, we can just download more?)
	# https://downloadmoreram.com/
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


	def not_contains_partial(self, fragment):
		for token in self.split_text_lower:
			if token.startswith(fragment.lower()):
				return None

		return True


	def contains_word(self, word):
		for token in self.split_text_lower:
			if token == word:
				return True

		return None


	def not_contains_word(self, word):
		for token in self.split_text_lower:
			if token == word:
				return None

		return True

	# note that this is a filter, if you want to actually get the entities that were
	# matched, call that specific function. don't modify this one
	def filter_re_search(self, pattern):
		return re.search(pattern, self.text)

	# careful when using this, might overconstrain search
	# should be fine if our corpus is big enough, but need to
	# run empirical tests
	def contains_all(self, word_list):
		for needle in word_list:
			if not self.contains_word(needle.lower()):
				return None

		return True


	def contains_any(self, word_list):
		for needle in word_list:
			if self.contains_word(needle.lower()):
				return True

		return None

	def contains_any_partial(self, word_list):
		for needle in word_list:
			if self.contains_word_partial(needle.lower()):
				return True

		return None
