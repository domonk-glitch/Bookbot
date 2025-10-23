# Word count function splits all words apart and counts.
def get_word_count(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
        print(f"Found {count} total words")

# Dictionary for further analysis of individual characters.
chara = {}

# Letter count function breaks full text down into individual characters, counts them and stores them in 'chara' dictionary for further analysis.
def letter_count(path):
    with open(path) as f:
        file_contents = f.read()
        lower_string = file_contents.lower()
        letters = list(lower_string)
        for letter in letters:
            if letter in chara:
                chara[letter] += 1

            else:
                chara[letter] = 1
       
# Sorting function for the characters stored in the 'chara' dictionary. Will sort them by number of appearances before sending to print.
#def sort(chara):



# Code snippet to print the detailed reports. Will be changing to print a list of dictionaries soon.
        for char in chara:
            number = chara[char]
            print(f"'{char}': {number}")
