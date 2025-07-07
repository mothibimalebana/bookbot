def get_word_count(book):
    words_array = book.split()
    word_count = len(words_array)
    print(f"Found {word_count} total words")

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
        if(item.isalpha()):
            dictionary_item = {}
            dictionary_item["char"] = item
            dictionary_item["num"] = dictionary[item]
            list.append(dictionary_item)
    return list


def sort_on(items):
    return items["num"]

