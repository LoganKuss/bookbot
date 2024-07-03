import os

def main():
    original_path = "books/"
    files = [f for f in os.listdir(original_path) if os.path.isfile(os.path.join(original_path, f))]
    if not files:
        print("No books found in the 'books' directory")
        return
    
    for i, file in enumerate(files, start=1):
        print(f"{i}. {files}: ")

    try:
        book_choice = int(input("Type 1, 2, 3, etc."))
        if not book_choice >= 1 and book_choice <= len(files):
            raise ValueError("Choice out of range")
    except ValueError as e:
        print(f"Invalid input: {e}")

    name_of_book = files[book_choice - 1]
    path_of_book = os.path.join(original_path, name_of_book)
    text = get_book_text(path_of_book)
    num_words = num_of_words(text)
    num_of_chars = num_of_characters(text)
    char_sorted_list = chars_dict_to_sorted_list(num_of_chars)
    
    print(f"---- Begin report of {path_of_book}----")
    print(f"There are {num_words} found in the book/n")

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("---End Report---")

def num_of_words(text):
    words = text.split()
    word_num = len(words)
    return word_num

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

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