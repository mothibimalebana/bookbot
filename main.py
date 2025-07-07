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

def print_list(list, book_path):
    book = get_book_test(book_path)
    # print("============ BOOKBOTpath_to_ =========
    # print(f"Analyzing book found at {bookpath}")
    # print("----------- Word Count ----------")
    get_word_count(book)
    # print("--------- Character Count -------")
    for item in list:
        if(item["char"].isalpha()):
            print(f"'{item["char"]}: {item["num"]}'\n")
    # print("============= END ===============")

def main():
    try:
        if len(sys.argv) != 2:
            raise Exception("python3 main.py <path_to_book>")
    except Exception as e:
        print(f"program is used as follows: {e}")
        sys.exit(1)

    path_to_book = str(sys.argv[1])
    book = get_book_test(path_to_book)
    letter_count = dictionary_count(book)   #returns number of letters
    list_of_dict = dict_to_list(letter_count)       #converts dictionary to list
    list_of_dict.sort(reverse=True, key=sort_on)
    print_list(list_of_dict, path_to_book)


main()