import re

from util import ngrams

class Tweet():

	def __init__(self, text):
		self.text = text

		split_text = text.split()

		self.tags = self.process_tags(split_text)
		self.uppercased = self.process_uppercased(split_text)
		self.uppercased_2grams = self.process_uppercased_2grams(split_text)

		# print(self.uppercased_2grams)


	# the stuff in here really should only be for pre-processing (aka caching)
	# all statistical and counting junk should exist in an exterior class

	def process_tags(self, text):
		return list(filter(lambda x: x.startswith('#'), text))

	def process_uppercased(self, text):
		return list(filter(lambda x: x[0].isupper(), text))

	def process_uppercased_2grams(self, text):
		return list(filter(lambda x: x[0][0].isupper() and x[1][0].isupper(), ngrams(text, 2)))




