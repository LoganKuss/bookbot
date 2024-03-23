def main():
    path_of_book = "books/frankenstein.txt"
    text = get_book_text(path_of_book)
    num_words = num_of_words(text)
    num_of_chars = num_of_characters(text)
    print(f"The number of words in Mary Shelley's Frankenstein are {num_words}")
    print(num_of_chars)

def num_of_words(text):
    words = text.split()
    word_num = len(words)
    return word_num

def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_characters(text):
    chars_dict = {}
    for c in text:
        lowered_chars = c.lower()
        if lowered_chars in chars_dict:
            chars_dict[lowered_chars] +=1
        else:
            chars_dict[lowered_chars] = 1
    return chars_dict



main()