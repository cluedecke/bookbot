from stats import total_words, char_count

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    book = get_book_text("books/frankenstein.txt")
    print(f"{total_words(book)} words found in the document")
    char_counts = char_count(book)
    for char, counts in char_counts.items():
        print(f"'{char}': {counts}")
    
main()

