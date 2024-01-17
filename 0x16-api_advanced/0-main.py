#!/usr/bin/python3
"""
0-main
"""
import sys
from importlib import import_module

if __name__ == '__main__':
    module = import_module('0-subs')
    number_of_subscribers = module.number_of_subscribers

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
