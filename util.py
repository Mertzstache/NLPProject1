from imdb import IMDb
import csv

def ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def remove_stopwords(word_list, stop_list):
    return [item for item in word_list if not item in stop_list]

def is_person(entity, d):
    # STOP_WORDS = ['for','in','-','–','or','a', 'the', 'I']
    # ia = IMDb()
    words = entity.split()
    for w in words:
        if w.lower() in d:
            return False
    return True

    #return len(ia.search_person(entity)) > 0 or entity.lower != "golden globe" or entity.lower != "golden globes"
    # return len(remove_stopwords) == 2 and entity.lower != "golden globe" and entity.lower != "golden globes" and len[]

def get_list_of_words(inputFileName):
    data = []
    # pp = pprint.PrettyPrinter()
    with open(inputFileName, "U") as csvfile:
        test = csv.reader(csvfile, delimiter = "\t")
        for row in test:
            #pp.pprint(row)
            for word in row:
                data.append(word)
    
    csvfile.close()
    #pp.pprint(data)
    print('three' in data)
    return data

def preprocess_awards(award_list):
    award_list = award_list.splitlines()
    award_list = [award.lower().split() for award in award_list]
    # print(award_list)
    STOP_WORDS = ['for','in','-','–','or','a']
    award_list = [remove_stopwords(award, STOP_WORDS) for award in award_list]
    return award_list
