def main():
    path = "books/frankenstein.txt"
    text = get_book_text(f"./{path}")
    num_words = count_num_words(text)
    
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n\n")
    
    sorted_num_chars = sorted(count_characters(text).items(), key=lambda item: item[1], reverse=True)

    for k, v in sorted_num_chars:
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
def count_num_words(text):
    lines = text.split()
    return len(lines)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    chars = dict()
    s = "".join((text.lower()).split())
    for i in s:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

main()
