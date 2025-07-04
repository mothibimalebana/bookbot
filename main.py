from stats import get_word_count
from stats import dictionary_count
from stats import dict_to_list

def get_book_test(book_path):
    with open(book_path) as book:    # do something with book here
        file_contents = book.read()
        # print(file_contents)
    return file_contents

def main():
    frankenstein = get_book_test("./books/frankenstein.txt")
    # get_word_count(frankenstein)
    letter_count = dictionary_count(frankenstein)
    dict_to_list(letter_count)

main()