# script to add words to pickled dictionary

#internal imports
import TextGenerator
import UI
import StatsTracker

import os
from collections import defaultdict
import random
import pickle

test_generator = any #TextGenerator.TextGenerator()
test_UI = any #UI.UI()
test_StatsTracker = any #StatsTracker.StatsTracker()



def run_basic(wordlist):
    streak = 0
    while True:
        realStr = generate_random_basic(wordlist, 4)
        attempt = input(realStr+'\n')
        if attempt == realStr:
            streak += 1
            print(f'\nCORRECT! Current streak: {streak}\n')
        else:
            print('INCORRECT! Game over...')
            break

def run_basic_lines(line_list):
    streak = 0
    while True:
        realStr = generate_random_line(line_list, 1)
        attempt = input(realStr + '\n')
        if attempt == realStr:
            streak += 1
            print(f'\nCORRECT! Current streak: {streak}\n')
        else:
            print('INCORRECT! Game over...')
            break


def main():
    test_gen = TextGenerator.TextGenerator(format_out='word', min_length=40)
    test_gen.generate_words_list()
    for i in range(5):
        print(test_gen.generate_random_string_from_words())

def main2():
    test_gen = TextGenerator.TextGenerator(format_out='line')
    test_gen.generate_lines_list()
    for i in range(5):
        print(test_gen.generate_random_line())


if __name__ == '__main__':
    print('Calling main()...')
    main()
