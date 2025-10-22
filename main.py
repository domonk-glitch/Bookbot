file_contents = None

def get_word_count(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
        print(f"Found {count} total words")

#def get_book_text(path):
#    with open(path) as f:
#        file_contents = f.read()
#        print(file_contents)

def main():
#    get_book_text("books/frankenstein.txt")
    get_word_count("books/frankenstein.txt")



main()
