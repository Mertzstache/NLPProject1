#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Printing JSON data"""

#****************************************
# main.py
# run like:
# $main.py <filename.json>
#****************************************

import sys, re, wikipedia, json
from imdb import IMDb
from jsonreader import create_corpus_from_file
from wizard import Wizard



def main():
    """main function"""
    filename = str(sys.argv[1]) if len(sys.argv) > 1 else "gg2018.json"
    gg_corpus = create_corpus_from_file(filename)

    data = json.load(open(filename))
    wizard = Wizard(gg_corpus)
    ggpage = wikipedia.page("Golden Globe Award")
    award_list = ggpage.section("Motion picture awards")+ "\n"+ ggpage.section("Television awards")

    print(wikipedia.summary("Call Me by Your Name (film)"))

    ia = IMDb()
    for person in ia.search_person('Mel Gibson'):
        print(person.personID, person['name'])
    print(ia.search_person('Call Me by Your Name'))
    # get the host for the awards
    gg_host = wizard.get_host()
    # print("host is:", gg_host)

    # gets the list of awards
    award_list = wizard.get_award_names()
    # print(award_list)


    # gather info for each of the awards
    wizard.get_all_award_info(award_list)
    # for elem in data:
    #   # print(elem['text'])
    #   m = re.search('robbed', elem['text']) #'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    #   if m:
    #       m.group(0)
    #       print(elem['text'])
    #       input("Found a tweet with a congrats! Press Enter to continue...")






if __name__ == "__main__":
    main()
