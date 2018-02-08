from encoded_knowledge import *
from collections import Counter

class Wizard():

	# all the fun stuff happens in here

	def __init__(self, corpus):
		self.corpus = corpus
		self.cache_useful_corpora()


	# memory grows with log of original corpora size, should be ok
	# this method caches some often used subsets of corpus (we query these subsets
	# for each award that we are looking at)
	def cache_useful_corpora(self):

		self.corpus_contain_best = self.corpus.filter(
			lambda x: x.contains_word_partial('best'))
		self.corpus_contain_best_nominee = self.corpus_contain_best.filter(
			lambda x: x.contains_word_partial('nominee'))
		self.corpus_contain_best_win = self.corpus_contain_best.filter(
			lambda x: x.contains_any(['win', 'won', 'wins']))
		self.corpus_contain_best_present = self.corpus_contain_best.filter(
			lambda x: x.contains_word_partial('present'))

		# free up memory, this one was just stepping stone
		self.corpus_contain_best = None


	# this just takes all tweets that contain the substring "host"
	# it then takes all of the capitalized 2grams that we filtered before
	# in each tweet. it returns the capitalized 2gram that occurs most often
	# in the corpus given these contraints
	def get_host(self):

		candidates = []

		for tweet in self.corpus:
			if tweet.contains_word_partial("host"):
				candidates += map(lambda x: ' '.join(x), tweet.uppercased_2grams)

		cand_counter = Counter(candidates)
		# print(cand_counter.most_common(10))

		# get the highest counted object, and extract the string out of it
		return cand_counter.most_common(1)[0][0]


	def get_award_names(self):
		
		# candidates = []

		# for tweet in self.corpus:
		# 	if tweet.contains_word_partial("present"):
		# 		print(tweet)

		# let's hardcode these for now. we can revisit later if we have time

		return ALL_AWARDS_LOWER_FILTERED



	def get_info_for_award(self, award_tokens):

		return ('presenter', self.__get_presenters(award_tokens))
		# self.__get_nominees(award_name)
		# self.__get_winners(award_name)

		
		


	def __get_presenters(self, award_tokens):

		corpus = self.corpus_contain_best_present.filter(lambda x: x.contains_all(award_tokens))

		for tweet in corpus:
		 	print(tweet.uppercased_2grams, "\n")

		candidates = []

		for tweet in corpus:
			candidates += map(lambda x: ' '.join(x), tweet.uppercased_2grams)


		cand_counter = Counter(candidates)
		top_list = cand_counter.most_common(10)

		if top_list:
			return top_list[0][0]
		else:
			return 'none'



	def __get_nominees(self, award_name):
		pass


	def __get_winners(self, award_name):
		pass

