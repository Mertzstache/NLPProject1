#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Printing JSON data"""

#****************************************
# main.py
# run like:
# $main.py <filename.json>
#****************************************

import sys
from jsonreader import create_corpus_from_file
from wizard import Wizard



def main():
	"""main function"""
	filename = str(sys.argv[1]) if len(sys.argv) > 1 else "gg2018.json"
	gg_corpus = create_corpus_from_file(filename)

	wizard = Wizard(gg_corpus)
	

	# get the host for the awards
	# gg_host = wizard.get_host()
	# print("host is:", gg_host)


	# gets the list of awards
	award_list = wizard.get_award_names()
	# print(award_list)


	# gather info for each of the awards

	for award_tokens in award_list:
	  	award_info = wizard.get_info_for_award(award_tokens)
	  	# print(award_tokens, award_info)

	# award_info = wizard.get_info_for_award(['best', 'actor'])
	# print(award_info)






if __name__ == "__main__":
	main()
