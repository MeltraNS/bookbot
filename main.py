def main():#here's what to do when the function first starts
    book_path = "books/frankenstein.txt"#set book_path as the string of the book we want to check out
    text = get_book_text(book_path) #what we want to print out is the strings
    #print(text)
    print(word_count(text))


def get_book_text(path): #define get book text with string path as an argument
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

main()
