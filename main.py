from stats import count_words, count_character, sorted_character_numbers

import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = count_words(book_text)
    num_character = count_character(book_text)
    sorted_list = sorted_character_numbers(num_character)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
    pass

main()