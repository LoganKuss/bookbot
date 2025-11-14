from stats import num_words
from stats import num_letters
from stats import sorted_char_dict

def main():
    num_of_words = num_words()
    print("============ BOOKBOT ============")
    print("Analiysing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("-------- Character Count -------")
    
    char_counts = num_letters()
    sorted_chars = sorted_char_dict(char_counts) 
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============ END ============")


main()

