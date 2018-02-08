#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Printing JSON data"""

#****************************************
# main.py
# run like:
# $main.py <filename.json>
#****************************************

import sys
from corpus import Corpus
from wizard import Wizard


# things to think about as a team:
# ensemble methods will have the best performance. we can put as much 
# engineering time as we want into this project. what kinds of things 
# should we focus on?

# start simple, build up from there to improve performance. let's get 
# a baseline up and running if we can do that quickly we can start playing 
# around with more fun things (statistical methods and whatnot)

# the baseline should just be simple rules (E.G. a search for "best 
# picture award is ?some")


def main():
    """main function"""
    filename = str(sys.argv[1]) if len(sys.argv) > 1 else "gg2018.json"
    gg_corpus = Corpus(filename)

    wizard = Wizard(gg_corpus)
    # gg_host = wizard.get_host()
    wizard.get_award_names()
   

if __name__ == "__main__":
    main()
