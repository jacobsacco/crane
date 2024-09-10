#!/usr/bin/python3

from string import ascii_lowercase
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("infile", help="A wordlist file to filter. Must have one word per line.")
parser.add_argument("-l", "--num-letters", type=int, default=5, help="What number of letters to filter words for. Defaults to 5")
parser.add_argument("-u", "--up-to", type=int, default=5000, help="Maximum number of words to produce. Defaults to 8000")
parser.add_argument("-o", "--output", type=str, default=None, help="Path of file to write filtered output to. Default is Nletters.txt where N is the number of letters")
args = parser.parse_args()

if args.output is None:
    args.output = f"{args.num_letters}letters.txt"

with open("100k.txt") as infile:
    words = [line.strip().lower() for line in infile.readlines() if len(line) == 6] #6 because 5 letters + newline

filtered = []
roman_numeral = set('xlvi')
for word in words:
    if set(word).issubset(roman_numeral):
        #print(word)
        continue
    if all(map((lambda char: char in ascii_lowercase), word)):
        filtered.append(word)

with open(args.output, 'w') as outfile:
    outfile.write("\n".join(filtered[:args.up_to]))
