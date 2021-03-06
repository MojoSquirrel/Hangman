import random

word_list = ["apple", "pear", "glasses", "crow", "orange", "wall", "crazy", "grape", "cream"]

def list_duplicates_of(seq, item): #if a letter has multiple instances in a word
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at + 1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def gallows(wrong_guesses):
    gallows_full = [
        "|---------         ",
        "|        |         ",
        "|        |         ",
        "|        0         ",
        "|       -|-        ",
        "|       / \        ",
        "|                  ",
        "|__________________\n",
    ]
    gallows_progress = [
        "|---------         ",
        "|                  ",
        "|                  ",
        "|                  ",
        "|                  ",
        "|                  ",
        "|                  ",
        "|__________________\n",
    ]
    for i in range(1, wrong_guesses + 1):
        gallows_progress[i] = gallows_full[i]

    for i in range(0, len(gallows_full)):
        print(gallows_progress[i])

while True: #main loop
    word = word_list[random.randint(0, len(word_list) - 1)] #pulls a word out of the wordlist
    n = len(word) #The len function gets the number of items in a list or string
    answer = [' _ '] *n
    wrong_guess = []
    score = 6

    print("Welcome to Hangman!")
    gallows(len(wrong_guess))

    print(answer) #Shows the user how many letters there are in the word
    print("\n")

    

    while True: #guess loop
        
        guess = str(input("Guess a letter:\n> ")) #define as string for index/count
        guess = guess.lower() # converts input to lowercase
        
        location_of_guessed_letters = list_duplicates_of(word,guess)
        i = 0

        #error handling conditions
        if len(guess) != 1: 
            print("Please enter 1 letter\n")
            continue
        elif guess.isalpha() == False: #checks if input is a character or number
            print("Please enter a letter, not a number\n")
            continue
        elif guess in wrong_guess or guess in answer:
            print("You can't choose the same letter twice \n")
            continue
            
        elif location_of_guessed_letters == []: #if guess is not in word
            print(guess + " is not in the word, try again\n")
            score -= 1
            wrong_guess.append(guess) #adds wrong guess to wrong_guess list
            print('Wrong Guess: ', wrong_guess) #prints wrong guesses for user
            gallows(len(wrong_guess))
            answer_word = "".join(answer) #concattenates answer into one string
            print(answer_word) #lets user see their progress in the answer
            
            if score <= 0:
                print("You lose!")
                break
                
            else:
                continue
            
        else: #if guess is in word
            for letter in location_of_guessed_letters:
                specific_location = location_of_guessed_letters[i] #individual location of guessed letter
                i += 1 #increases list item for location of guessed letter
                answer[specific_location] = guess #replaces list item with guess
                answer_word = "".join(answer) #concattenates answer into one string
                
            print(answer_word) #lets user see their progress in the answer
            
            if answer_word == word: #compares answer to origional word for winning condition
                print("You've escaped the noose this time, but I've got my eye on you, buster.")
                break
                
            continue
    x = int(input("would you like to continue? Enter 1 to continue, any other key to quit:")) #exit/continue for main loop
    if x == 1:
        continue
    else:
        break
