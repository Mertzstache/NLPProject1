from collections import Counter

class Wizard():

	# all the fun stuff happens in here

	def __init__(self, corpus):
		self.corpus = corpus


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

		return cand_counter.most_common(1)[0][0]



	def get_award_names(self):
		pass


	def get_presenters(self):
		pass


	def get_nominees(self):
		pass


	def get_winners(self):
		pass

