from stats import get_num_words, get_chars_dict, chars_report

import sys

def main():
    if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
    book_path = sys.argv[1] #"books/frankenstein.txt"
    text = get_book_text(book_path) 
    num_words = get_num_words(text)
    counter_chars = get_chars_dict(text)
    print("=" * 12 + " " + "BOOKBOT" + " " + "=" * 12)
    print(f"Analyzing book found at {book_path}...")
    print("-" * 11 + " " + "Word Count" + " " + "-" * 10)
    print(f"Found {num_words} total words")
    print("-" * 8 + " " + "Characters Count" + " " + "-" * 7)
    chars_report(counter_chars)
    print("=" * 14 + " " + "END" + " " + "=" * 14)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()