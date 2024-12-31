
def count_words(text):
    word_counter = 0
    words = text.split()
    for word in words:
        word_counter += 1
    return word_counter


def count_chars(text):
    result_dict = dict()
    for char in text.lower():
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            if char in result_dict:
                result_dict[char] += 1
            else:
                result_dict[char] = 1
    return sorted(result_dict.items(), key=lambda x:x[1], reverse=True)



def main():
    path_to_file = 'books/frankenstein.txt'
    with open(path_to_file) as f:
        file_contents = f.read()
        # print(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document\n")
        chars = count_chars(file_contents)
        for key in chars:
            print(f"The '{key[0]}' character was found {key[1]} times")
        print('--- End report ---')

if __name__ == '__main__':
    main()