def get_word_count(book):
    words_array = book.split()
    word_count = len(words_array)
    print(f"{word_count} words found in the document")

def dictionary_count(book):
    word_dictionary = {}
    book = book.lower()

    for words in book:
        word_dictionary[words] = 0

    for words in book:
        word_dictionary[words] += 1
    
    return word_dictionary 

def dict_to_list(dictionary):
    list = []

    for item in dictionary:
        list.append(item)
    
    print(list)
    
    return list

def sort_on(items):
    for item in items:
        return item

