# text user interfaces (TUIs)

import argparse 
import string 
from collections import Counter 

def parse_arguments():
    parser = argparse.ArgumentParser(description='Report word frequencies in a text file.')
    parser.add_argument('filename')
    parser.add_argument('-n', type=int, default=10, help='Number of words to show (default 10)')
    parser.add_argument('-i', '--ignore-case', action='store_true', help='Case insensitive counting')
    parser.add_argument('--exclude', nargs='*', default=[], help='Words to exclude from the count')
    return parser.parse_args()

def main():
    args = parse_arguments()

    excluded = []
    for word in args.exclude:
        if args.ignore_case:
            excluded.append(word.lower())
        else:
            excluded.append(word)
    
    with open(args.filename, 'r') as file:
        text = file.read()

    print(f'{text = }') 


if __name__ == '__main__':
    main()

