from imdb import IMDb

def ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def remove_stopwords(word_list, stop_list):
    return [item for item in word_list if not item in stop_list]

def is_person(entity):
    ia = IMDb()
    return len(ia.search_person(entity)) > 0

def preprocess_awards(award_list):
    award_list = award_list.splitlines()
    award_list = [award.lower().split() for award in award_list]
    STOP_WORDS = ['for','in','-','–','or','a']
    award_list = [remove_stopwords(award, STOP_WORDS) for award in award_list]
    return award_list
