def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict


def chars_dict_to_sorted_list(chars_dict):
    chars_list = []
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Sort by count (descending), then by character (ascending)
    chars_list.sort(key=lambda x: (-x["num"], x["char"]))
    return chars_list
