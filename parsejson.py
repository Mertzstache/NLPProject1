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
# from pprint import pprint
#import numpy as np
#import os
#import shutil

def main():
    """main function"""
    filename = str(sys.argv[1])

    data = json.load(open(filename))

    for elem in data:
        print(elem['text'])
        input("Press Enter to continue...")
   # pprint(data)


if __name__ == "__main__":
    main()
