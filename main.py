with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

def word_count(file_contents):
    print(len(" ".split(file_contents)))