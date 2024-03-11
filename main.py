def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(num_words)
    counts = get_count_letters(text)
    print(counts)
    

def get_count_letters(text):
    lower_case_text = text.lower()
    return_dict = {}

    for char in lower_case_text:
        if not (char in return_dict.keys()):
            return_dict[char] = 1
        else:
            return_dict[char] += 1
    
    return return_dict

def get_num_words(text):
    words_split = text.split()
    return len(words_split)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

main()
