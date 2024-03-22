def main():
    path_of_book = "books/frankenstein.txt"
    text = get_book_text(path_of_book)
    num_words = num_of_words(text)
    print(f"The number of words in Mary Shelley's Frankenstein are {num_words}")

def num_of_words(text):
    words = text.split()
    word_num = len(words)
    return word_num

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()