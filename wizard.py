from encoded_knowledge import *
from collections import Counter
from util import is_person, preprocess_awards, remove_stopwords, get_list_of_words
import wikipedia

class Wizard():

    # all the fun stuff happens in here

    def __init__(self, corpus):
        self.corpus = corpus
        self.cache_useful_corpora()
        self.d = get_list_of_words("3esl.txt")


    # memory grows with log of original corpora size, should be ok
    # this method caches some often used subsets of corpus (we query these subsets
    # for each award that we are looking at)
    def cache_useful_corpora(self):

        self.corpus_contain_best = self.corpus.filter(
        lambda x: x.contains_word_partial('best'))
        self.corpus_contain_best_nominee = self.corpus_contain_best.filter(
        lambda x: x.contains_word_partial('nomin'))
        self.corpus_contain_best_win = self.corpus_contain_best.filter(
        lambda x: x.contains_any(['win', 'won', 'wins']))
        self.corpus_contain_best_present = self.corpus_contain_best.filter(
        lambda x: x.contains_word_partial('present'))
        self.corpus_contain_congrat_not_win = self.corpus_contain_best.filter(
        lambda x: x.contains_word_partial('congrat')).filter(
        lambda x: x.not_contains_partial('win'))
        self.corpus_contain_robbed = self.corpus.filter(
        lambda x: x.contains_word_partial('robbed'))

        # for tweet in self.corpus_contain_robbed:
        # 	print(tweet)
        # print(len(self.corpus_contain_robbed))
        # print(len(self.corpus_contain_best))



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

        ggpage = wikipedia.page("Golden Globe Award")
        award_list = ""
        for string in (ggpage.section("Motion picture awards") + "\n"+ ggpage.section("Television awards")).splitlines():
            temp = ""
            for character in string:
                if character == ":":
                    break
                temp += character
            award_list += temp + "\n"
        # print(award_list)
        award_list = preprocess_awards(award_list)
        # print(award_list)
        return award_list


    def get_award_names_local(self):

        entities = []

        corpus = self.corpus_contain_best.filter(
            lambda x: x.contains_any_partial(['congrat', 'nom', 'hope', 'should', 'could']))

        for tweet in corpus:
            entities += tweet.re_findall(r'(Best(?: +[A-Z-–][\w,]*)+)')
            
        counter = Counter(entities)
        print(counter.most_common(50))



    def get_all_award_info(self, award_list):

        award_info = []
        # for award_tokens in award_list:
        #     award_info.append((' '.join(word for word in award_tokens), 
        #         self.get_info_for_award(award_tokens)))

        self.get_info_for_award(award_list[0])

        return award_info



    def get_info_for_award(self, award_tokens):

        # print(award_tokens, "\n\n")

        info = {}
        # info['presenters'] = self.__get_presenters(award_tokens)
        info['nominees'] = self.__get_nominees(award_tokens)
        # info['winners'] = self.__get_winners(award_tokens)

        return info


    def who_was_robbed(self):
        corpus = self.corpus_contain_robbed

        candidates = [] 

        for tweet in corpus:
            # print(tweet)
            candidate = list(filter(is_person, list(map(lambda x: ' '.join(x), tweet.uppercased_2grams))))
            candidates += candidate
        cand_counter = Counter(candidates)
        return cand_counter.most_common(60)

    def __get_presenters(self, award_tokens):

        # corpus = self.corpus_contain_best.filter_re_search('\w+\W\w+\W(won|wins)')
        corpus = self.corpus_contain_best_present.filter(lambda x: x.contains_any(award_tokens))

        print("presenter")

        candidates = []

        for tweet in corpus:
            #print(tweet)
            # tweet.text = remove_stopwords(tweet.text, award_tokens)
            # tweet.split_text = tweet.text.split()
            candidate = list(filter(is_person,list(map(lambda x: ' '.join(x), tweet.uppercased_2grams))))
            candidates += candidate

        cand_counter = Counter(candidates)
        print(cand_counter.most_common(10))
        return cand_counter.most_common(1)


    def __get_nominees(self, award_tokens):


        corpus = self.corpus.filter(
            lambda x: x.contains_any_partial(['congrat', 'nom', 'hope', 'should', 'could', 'rob']))

        for tweet in corpus:
            print(tweet)
            print("runs", tweet.uppercased_runs)
            print("\n")
            


        # corpus = self.corpus_contain_best_nominee.filter(lambda x: x.contains_any(award_tokens))

        #candidates = []

        # for tweet in corpus:
            # print(tweet)
            # people_mentioned = [i for i in tweet.uppercased_2grams if is_person(str(i))]
            # if len(people_mentioned) > 0:
            #     for ppl in people_mentioned:
            #         candidates += ppl




        # cand_counter = Counter(candidates)
        # print(cand_counter.most_common(20))




    def __get_winners(self, award_tokens):

        corpus = self.corpus_contain_best_win.filter(lambda x: x.contains_any(award_tokens)).filter(
            lambda x: x.contains_word(award_tokens[1]))

        winner_is_actress = True if any(token in ['actress'] for token in award_tokens) else False
        winner_is_actor = True if any(token in ['actor'] for token in award_tokens) else False
        winner_is_director = True if any(token in ['director'] for token in award_tokens) else False

        genre_drama = True if any(token in ['drama'] for token in award_tokens) else False
        genre_comedy = True if any(token in ['comedy'] for token in award_tokens) else False

        winner_is_television = True if any(token in ['television'] for token in award_tokens) else False
        
        if winner_is_actor:
            corpus = corpus.filter(lambda x: x.contains_word('actor'))
        elif winner_is_actress:
            corpus = corpus.filter(lambda x: x.contains_word('actress'))
        elif winner_is_director:
            corpus = corpus.filter(lambda x: x.contains_word('director'))

        if genre_comedy:
            corpus = corpus.filter(lambda x: x.contains_word('comedy'))
        elif genre_drama:
            corpus = corpus.filter(lambda x: x.contains_word('drama'))

        if winner_is_television:
            corpus = corpus.filter(lambda x: x.contains_any(['TV', 'television']))
        else: 
            corpus = corpus.filter(lambda x: x.not_contains_partial('television'))




        winner_is_movie = not (winner_is_actor or winner_is_actress or winner_is_director)

        # print("winner")

        candidates = []

        for tweet in corpus:
            # print(tweet)
            candidate = tweet.re_findall(r'(\b[A-Z][\w,]*(?:\s+\b[A-Z][\w,]*)+)\s+(?:win|won)')
            # print(candidate)
            if len(candidate) > 0 and winner_is_movie != is_person(candidate[0], self.d):
                candidates += candidate

        cand_counter = Counter(candidates)
        # print(cand_counter.most_common(10))
        return cand_counter.most_common(1)
