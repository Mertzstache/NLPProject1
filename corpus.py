
class Corpus():

	def __init__(self, tweets):
		self.tweets = list(tweets)

	def __iter__(self):
		return iter(self.tweets)

	def __len__(self):
		return (len(self.tweets))

	# filter this corpus and return the subset
	# fn must be a boolean function on Tweet (should be defined in the Tweet subclass)
	def filter(self, fn):
		return Corpus(filter(fn, self))

	def filter_re_search(self, pattern):
		return self.filter(lambda x: x.filter_re_search(pattern))