import json
from corpus import Corpus
from tweet import Tweet

#------------------------------------------------
# reads in the initial corpus from the json file
# and returns a corpus object
#-------------------------------------------------

def create_corpus_from_file(file_path="gg2018.json"):
	json_data = read_json_data(file_path)
	unique_tweets_raw = get_unique_tweets(json_data)
	return Corpus(map(lambda x: Tweet(x), unique_tweets_raw))


def read_json_data(file_path):
	return json.load(open(file_path))


# there are a lot of redundant tweets (retweets). we can just ignore these
# and save processing time. I don't think their frequencies encode any useful
# signals
def get_unique_tweets(json_data):

	unique_tweets = set()

	for elem in json_data:

		tweet = elem['text']

		if tweet not in unique_tweets:
			unique_tweets.add(tweet)

	return unique_tweets