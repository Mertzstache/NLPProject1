
def ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

def remove_stopwords(word_list, stop_list):
	return [item for item in word_list if not item in stop_list]
