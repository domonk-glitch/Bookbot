from stats import get_word_count 
from stats import letter_count


#def get_book_text(path):
#    with open(path) as f:
#        file_contents = f.read()
#        print(file_contents)

def main():
#    get_book_text("books/frankenstein.txt")
    get_word_count("books/frankenstein.txt")
    letter_count("books/frankenstein.txt")



main()
