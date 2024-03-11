def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)

    print(f"--- Begin report of {path_to_file} ---")
    print()
    print_report(text)

def sort_on(dict):
    return dict["num"]


def print_report(text):
    num_words = get_num_words(text)
    counts = get_count_letters(text)
    print(f"{num_words} words found in the document.")
    print()

    array = []
    for key in counts.keys():
        array.append({"char":key ,
                      "num": counts[key]})
        
    array.sort(reverse=True, key=sort_on)
    for item in array:
        if(item["char"].isalpha()):
            print(f"The '{item["char"]}' character was found {item["num"]} times.")
    print()

    print("--- End report ---")

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
