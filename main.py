def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(num_words)

def get_num_words(text):
    words_split = text.split()
    return len(words_split)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

main()
