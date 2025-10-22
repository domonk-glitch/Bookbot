def get_word_count(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
        print(f"Found {count} total words")


def letter_count(path):
    chara = {}
    with open(path) as f:
        file_contents = f.read()
        lower_string = file_contents.lower()
        letters = list(lower_string)
        count = len(letters)
        for letter in letters:
            if letter in chara:
                chara[letter] += 1

            else:
                chara[letter] = 1
        
        for char in chara:
            number = chara[char]
            print(f"'{char}': {number}")
