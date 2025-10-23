from stats import get_word_count 
from stats import letter_count

path = "books/frankenstein.txt"

#def get_book_text(path):
#    with open(path) as f:
#        file_contents = f.read()
#        print(file_contents)

def main():
#    get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    get_word_count(path)
    print("--------- Character Count -------")
    letter_count(path)



main()
