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
    
    words = text.split('\n')

    print(f'{words = }')

    frequency = {}

    for word in words:
        if word in frequency:
            # we've seen this word before
            print(f'Incrementing the count for {word}')
            frequency[word] += 1 # add one
        else:
            # this is the first time seeing this word
            print(f'Adding an initial count for {word}')
            frequency[word] = 1

    print(f'{frequency = }')

# product = {
#     'name': 'GPU9000',
#     'price': 100000
# }
# product['price'] *= 0.9

if __name__ == '__main__':
    main()

