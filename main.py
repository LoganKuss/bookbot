# My solution:
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        final_file_contents = ''.join(c for c in file_contents if c.isalpha()).lower()
        
    return final_file_contents

def count_words(full_string):
    text = full_string.split()
    word_num = len(text)
    print(f"There are {word_num} words in the book")

def count_letters(string):
    letter_num = {}

    for s in string:
        letter_num[s] = letter_num.get(s, 0)+1
    
    return letter_num    

def print_report(letters):
    sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    for letter, count in sorted_letters:
        print(f"the {letter} character was found {count} times")




text_final = main()
final_report = count_letters(text_final)

print_report(final_report)