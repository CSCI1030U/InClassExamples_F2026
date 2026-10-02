# import sys 

# if len(sys.argv) < 2:
#     print('Error:  Must supply a name argument!')
#     sys.exit(1)

# print(f'Hello, {sys.argv[1]}, from {sys.argv[0]}!')

import argparse 

argument_parser = argparse.ArgumentParser(description = 'An app that greets you')
argument_parser.add_argument('name', help = 'The name to greet')
argument_parser.add_argument('-l', '--loud', action='store_true', help='Shout the greeting')
args = argument_parser.parse_args()

greeting = f'Hello, {args.name}'
if args.loud:
    print(greeting.upper()) 
else:
    print(greeting)

