#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Printing JSON data"""

#****************************************
# parsejson.py
# run like:
# $parsejson.py <filename.json>
#****************************************

import sys
import json
import re
#from pprint import pprint
#import numpy as np
#import os
#import shutil

def main():
    """main function"""
    filename = str(sys.argv[1])

    data = json.load(open(filename))

    for elem in data:
        # print(elem['text'])
        m = re.search('https?:\/\/(www\.)?', elem['text']) #'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
        if m:
            m.group(0)
            print(elem['text'])
            input("Found a tweet with a link! Press Enter to continue...")
   # pprint(data)


if __name__ == "__main__":
    main()
