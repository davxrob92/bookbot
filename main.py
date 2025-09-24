# this function takes a filepath as input and returns the contents of a file as a string

def get_book_text(path_to_file):
    with open(path_to_file) as f: 
        return f.read()

def count_book_words(text):
    return len(text.split())

        
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_book_words(book_text)
    print(f"Found {num_words} total words")
main()
