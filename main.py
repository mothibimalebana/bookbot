from stats import get_word_count
from stats import dictionary_count
from stats import dict_to_list
from stats import sort_on
import sys


def get_book_test(book_path):
    with open(book_path) as book:    # do something with book here
        file_contents = book.read()
        # print(file_contents)
    return file_contents

def print_list(list):
    frankenstein = get_book_test()
    # print("============ BOOKBOT ============")
    # print(f"Analyzing book found at {bookpath}")
    # print("----------- Word Count ----------")
    get_word_count(frankenstein)
    # print("--------- Character Count -------")
    for item in list:
        if(item["char"].isalpha()):
            print(f"'{item["char"]}: {item["num"]}'\n")
    # print("============= END ===============")

def main():
    frankenstein = get_book_test(bookpath)
    letter_count = dictionary_count(frankenstein)   #returns number of letters
    list_of_dict = dict_to_list(letter_count)       #converts dictionary to list
    list_of_dict.sort(reverse=True, key=sort_on)
    print_list(list_of_dict)


main()