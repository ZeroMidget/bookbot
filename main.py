def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    words = lower(text)
    worddict = (count_chars(words))
    sorted_list =(sort(worddict))
    for char, count in sorted_list:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
#counts strings to determine word count
def get_num_words(text):
    words = text.split()
    return len(words)

#splits words into string
def get_split_words(text):
    words = text.split()
    return words

#gets path to book text
def get_book_text(path):
    with open(path) as f:
        return f.read()

#lower cases entire text and splits by word
def lower(text):
    lowered = text.lower()
    return lowered


#dictionary
def count_chars(text):
    my_dict = {}
    for char in text:
        if char.isalpha():
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
    return my_dict

#counting letters report
def sort(dict):
    num = []
    for key, value in dict.items():
        num.append((key,value))
    num.sort(reverse=True, key=lambda x:x[1])    
    return (num)


main()