def main():#here's what to do when the function first starts
    book_path = "books/frankenstein.txt"#set book_path as the string of the book we want to check out
    text = get_book_text(book_path) #what we want to print out is the strings
    print(f"--- Begin report of{book_path} ---")
    print(str(word_count(text)) + " words found in document")
    for i in character_count(text):
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")


def get_book_text(path): #define get book text with string path as an argument
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def character_count(text):
    lowered_string = text.lower()
    total_chars = {}
    change_to_tuple_list = []
    for character in lowered_string:
        if character not in total_chars and character.isalpha() == True:
            total_chars[character] = 1
        elif character.isalpha() == False:
            pass
        else:
            total_chars[character] += 1
    for unsorted in total_chars:
        change_to_tuple_list.append((unsorted, total_chars[unsorted]))
    sorted_list = sorted(change_to_tuple_list, key=lambda v: v[1], reverse=True)
    return sorted_list

main()
