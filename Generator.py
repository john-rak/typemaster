import os

class Generator:

    directory = any
    format_out = any
    word_len = int
    line_len = int
    filetype = str

    def __init__(self, directory='/Users/jrak/Work', filetype='.py', min_length=5, max_length=50, format_out='word'):
        self.directory = directory
        self.filetype = filetype
        self.min_length = min_length
        self.max_length = max_length
        self.format_out = format_out

    def generate_file_paths(self) -> list:
        file_paths = []
        for path, _, files in os.walk(self.directory):
            for file in files:
                filepath = os.path.join(path, file)
                if os.path.isfile(filepath) and filepath.endswith(self.filetype):
                    file_paths.append(filepath)
        print(file_paths)
        return file_paths

    def is_valid_text(self, text):
        valid = False
        if self.format_out == 'word':
            valid = text.isascii() and self.min_length < len(text) < self.max_length
        elif self.format_out = 'line':
            valid = text.isascii() and self.min_length < len(text) < self.max_length

        return valid




    def run(self):
        pass