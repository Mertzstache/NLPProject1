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
from util import preprocess_awards


def main():
    """main function"""
    filename = str(sys.argv[1]) if len(sys.argv) > 1 else "gg2018.json"
    gg_corpus = create_corpus_from_file(filename)

    data = json.load(open(filename))
    wizard = Wizard(gg_corpus)

    #scrape award names from wikipedia
    ggpage = wikipedia.page("Golden Globe Award")
    award_list = ggpage.section("Motion picture awards")+ "\n"+ ggpage.section("Television awards")
    award_list = preprocess_awards(award_list)

    #get host
    gg_host = wizard.get_host()
    # print("host is:", gg_host)

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
