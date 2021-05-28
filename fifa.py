#!/usr/bin/python

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--debug', action='store_true')
    args = parser.parse_args()

    if args.debug:
    	print("Debug")

    print("Hello Euro")