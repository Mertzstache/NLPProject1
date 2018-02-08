
class Corpus():

	def __init__(self, tweets):
		self.tweets = tweets

	def __iter__(self):
		return iter(self.tweets)