def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    print(lower(text))

def get_num_words(text):
    words = text.split()
    return len(words)

def get_split_words(text):
    words = text.split()
    return words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def lower(text):
    lowered = text.lower()
    words = lowered.split()
    return words



main()