def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_contents = f.read()
    return book_contents

def num_words():
    word_list = get_book_text().split()
    num_words_in_list = len(word_list)
    return num_words_in_list

def num_letters():
    num_dict = {} 
    book_str = get_book_text().lower()
    for char in book_str:
        if char in num_dict:
            num_dict[char] += 1
        else:
            num_dict[char] = 1
    return num_dict
