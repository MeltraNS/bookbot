def main():#here's what to do when the function first starts
    book_path = "books/frankenstein.txt"#set book_path as the string of the book we want to check out
    text = get_book_text(book_path) #what we want to print out is the strings
    #print(text)
    print("text is " + str(word_count(text)) + " words long")
    print(character_count(text))


def get_book_text(path): #define get book text with string path as an argument
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def character_count(text):
    lowered_string = text.lower()
    total_chars = {}
    for character in lowered_string:
        if character not in lowered_string:
            total_chars[character] = 1
        else:
            total_chars[character] = text[character]
            total_chars[character] += 1
    return total_chars


main()
