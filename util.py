from imdb import IMDb
import csv

def ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def remove_stopwords(word_list, stop_list):
    return [item for item in word_list if not item in stop_list]

def strip_common_list(tokens, char_list=",'"):
    return [token.strip(char_list) for token in tokens]

def is_person(entity, d):
    # STOP_WORDS = ['for','in','-','–','or','a', 'the', 'I']
    # ia = IMDb()
    # print('best' in d)
    words = entity.split()
    for w in words:
        # print(w.lower())
        if w.lower() in d:
            # print(w.lower())
            return False
    # print(entity)
    return True

    #return len(ia.search_person(entity)) > 0 or entity.lower != "golden globe" or entity.lower != "golden globes"
    # return len(remove_stopwords) == 2 and entity.lower != "golden globe" and entity.lower != "golden globes" and len[]
def is_not_award_name(entity, award_tokens):
    # print(' '.join(award_tokens) in entity.lower())
    split_entity = entity.split()
    split_entity = [e.lower() for e in split_entity]
    # print(split_entity)
    for a in award_tokens + ['golden', 'globes', 'globe', 'best']:
        if a in split_entity:
            return False
    return True

def get_list_of_words(inputFileName):
    data = []
    # pp = pprint.PrettyPrinter()
    with open(inputFileName, "U") as csvfile:
        test = csv.reader(csvfile, delimiter = "\t")
        for row in test:
            #pp.pprint(row)
            for word in row:
                if word != 'moss':
                    data.append(word)

    csvfile.close()
    #pp.pprint(data)
    # print('three' in data)
    return data

def preprocess_awards(award_list):
    award_list = award_list.splitlines()
    award_list = [award.lower().split() for award in award_list]
    # print(award_list)
    STOP_WORDS = ['for','in','-','–','or','a']
    award_list = [remove_stopwords(award, STOP_WORDS) for award in award_list]
    return award_list
