import json
from tweet import Tweet

class Corpus():

	tweets = None

	def __init__(self, file_path):
		json_data = self.read_json_data(file_path)

		unique_tweets_raw = self.get_unique_tweets(json_data)
		self.tweets = list(map(lambda x: Tweet(x), unique_tweets_raw))


	def read_json_data(self, file_path):
		return json.load(open(file_path))



	def get_unique_tweets(self, json_data):

		unique_tweets = set()

		for elem in json_data:

			tweet = elem['text']

			if tweet not in unique_tweets:
				unique_tweets.add(tweet)

		return unique_tweets