def get_book_test(book_path):
    with open(book_path) as book:    # do something with book here
        file_contents = book.read()
        # print(file_contents)
    return file_contents

def get_word_count(book):
    words_array = book.split()
    word_count = len(words_array)
    print(f"{word_count} words found in the document")

def main():
    frankenstein = get_book_test("./books/frankenstein.txt")
    get_word_count(frankenstein)

main()