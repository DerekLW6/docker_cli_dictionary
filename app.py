import json
from difflib import get_close_matches

data = json.load(open('data.json'))

# Write a function to look up/print definition 
def lookup(word):
    # ensuring lowercase
    word = word.lower() 

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if (yn == "Y" or yn == 'y'):
            return data[get_close_matches(word, data.keys())[0]]
        elif (yn == "N" or yn == 'n'):
            print("The word doesn't exist. Please double check it.")
            return ".."
        else:
            print("The word doesn't exist. Please double check it.")
            return ".."
    else:
        print('Word not found. Please try again.')
        return '..'

# Getting user input
running = True

while running:
    print("Hit 0 to quit")
    user_input = input("Input a word to lookup:")
    if user_input == '0':
        running = False
        print("Program Ending")
        print('==============')
    else:
        a = lookup(user_input)
        for x in range(len(a)): 
            print(a[x])

