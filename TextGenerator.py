import os
from collections import defaultdict
import random

class TextGenerator:

    directory = any
    format_out = any
    word_len = int
    line_len = int
    filetype = str
    generated_text = list

    def __init__(self, directory='/Users/jrak/Work/houston', filetype='.py', min_length=5, max_length=50, format_out='word'):
        self.directory = directory
        self.filetype = filetype
        self.min_length = min_length
        self.max_length = max_length
        self.format_out = format_out
        self.generated_text = []

    def generate_file_paths(self) -> list:
        file_paths = []
        for path, _, files in os.walk(self.directory):
            for file in files:
                filepath = os.path.join(path, file)
                if os.path.isfile(filepath) and filepath.endswith(self.filetype):
                    file_paths.append(filepath)
        return file_paths

    def is_valid_text(self, text):
        valid = False
        if self.format_out == 'word':
            valid = text.isascii() #and self.min_length < len(text) < self.max_length
        elif self.format_out == 'line':
            valid = text.isascii() and self.min_length < len(text) < self.max_length

        return valid

    def scrape_file_text(self, text_data) -> None:
        if self.format_out == 'word':
            for line in text_data:
                for word in line.split():
                    if self.is_valid_text(word):
                        self.generated_text.append(word)
        elif self.format_out == 'line':
            for line in text_data:
                line = line.strip()
                if self.is_valid_text(line):
                    self.generated_text.append(line)

    def iterate_and_scrape_files(self, file_path_list):
        filecount = 0
        for filepath in file_path_list:
            with open(filepath, 'r') as f:
                try:
                    data = f.readlines()
                    self.scrape_file_text(data)
                    filecount += 1
                except FileNotFoundError:
                    print('Unable to read file.')

        print(f'Read {filecount} files successfully.')

    # ---------------
    # Word specific logic
    # ---------------
    def generate_words_list(self) -> None:
        assert self.format_out == 'word'
        file_paths = self.generate_file_paths()
        self.iterate_and_scrape_files(file_paths)

    def generate_random_string_from_words(self) -> str:
        randStr = ''
        while len(randStr) < self.min_length:
            index = random.randint(0, len(self.generated_text))
            word = self.generated_text[index]
            randStr += word + ' '

        return randStr[:-1]



    # ---------------
    # Line specific logic
    # ---------------
    def generate_lines_list(self) -> None:
        assert self.format_out == 'line'

        file_paths = self.generate_file_paths()
        self.iterate_and_scrape_files(file_paths)


    def generate_random_line(self) -> str:
        return random.sample(self.generated_text, k=1)[0]




    def run(self):
        pass