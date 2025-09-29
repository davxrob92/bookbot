# this function takes a filepath as input and returns the contents of a file as a string
from stats import count_book_words, get_book_characters, sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        return f.read()
        
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_book_words(book_text)
    character_count = get_book_characters("books/frankenstein.txt")
    sortied = sorted_dict(character_count)
    print("============ BOOKBOT ============")
    print(f"Found {num_words} total words")
    print("--------- Character Count ------- ")
    for s in sortied:
        if s["char"].isalpha() == True:
            print(s["char"]+":",s["num"])
    print("============= END ===============")
main()
