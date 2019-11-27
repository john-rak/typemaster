# script to add words to pickled dictionary

import os
from collections import defaultdict
import random
import pickle


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

def generate_random_basic_words(wordlist, length) -> str:
    randStr = ''
    for word in random.sample(wordlist, k=length):
        if is_valid_word(word):
            randStr += word + ' '
        else:
            word = random.sample(wordlist, k=1)[0]
            while not is_valid_word(word):
                word = random.sample(wordlist, k=1)[0]
            randStr += word + ' '
    return randStr[:-1]

def is_valid_word(word):
    return word.isascii() and 2 < len(word) < 10

def generate_random_line(linelist, length) -> str:
    line = random.sample(linelist, k=1)[0].strip()
    while not is_valid_line(line):
        line = random.sample(linelist, k=1)[0].strip()
    return line


def is_valid_line(line):
    return line.isascii() and 15 < len(line) < 50

def generate_files() -> list:
    file_paths = []
    for path, _, files in os.walk('/Users/jrak/Work/'):
        for file in files:
            filepath = os.path.join(path, file)
            if os.path.isfile(filepath) and filepath.endswith('.py'):
                file_paths.append(filepath)
    print(file_paths)
    return file_paths


def generate_words() -> dict:
    WORD_LIST = defaultdict(lambda: 0)
    file_paths = generate_files()

    for filepath in file_paths:
        with open(filepath, 'r') as f:
            try:
                data = f.readlines()
                for line in data:
                    for word in line.split():
                        WORD_LIST[word] += 1
                print('Read file.')
            except FileNotFoundError:
                print('Unable to read file.')
    return dict(WORD_LIST)


def generate_words_list() -> list:
    WORD_LIST = []
    file_paths = generate_files()
    for filepath in file_paths:
        with open(filepath, 'r') as f:
            try:
                data = f.readlines()
                for line in data:
                    for word in line.split():
                        WORD_LIST.append(word)
                print('Read file.')
            except FileNotFoundError:
                print('Unable to read file.')
    return WORD_LIST
    # print(sorted(WORD_LIST.items(),key= lambda x:x[1]))


def generate_lines() -> list:
    LINE_LIST = []
    file_paths = generate_files()
    for filepath in file_paths:
        with open(filepath, 'r') as f:
            try:
                data = f.readlines()
                for line in data:
                    if line.isascii():
                        LINE_LIST.append(line)
                print('Read file.')
            except FileNotFoundError:
                print('Unable to read file.')
    return LINE_LIST


def main():
    line_list = []
    if os.path.isfile('lines_list.pkl'):
        with open('lines_list.pkl', 'rb') as file:
            line_list = pickle.load(file)
            print('Found pickled file!')
    else:
        print('Calling generate_lines()...')
        line_list = sorted(generate_lines())
        with open('lines_list.pkl', 'wb') as file:
            pickle.dump(word_list, file)
    run_basic_lines(line_list)


if __name__ == '__main__':
    print('Calling main()...')
    main()
