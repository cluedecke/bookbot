def total_words(book):
    words = book.split()
    return len(words)

def char_count(book):
    book = book.lower()
    char_dict = {}
    for char in book:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:   
            char_dict[char] = 1
            
    return char_dict


