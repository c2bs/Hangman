import random

def welcome_hangman():
    print("Welcome to hangman!")
    print(" ")
    user_name = input("What is your name? ")
    print(" ")
    print("Hello", user_name, "good luck! You will be given a randomly selected word by the computer and have 8 guesses to solve!")
    print(" ")
    print("Okay", user_name, "below is how many letters are in the word")
welcome_hangman()

words = "about add after ago any apple ask ate away back bad bag base bat bee being best bike bill bird black blue boat both bring brown bus by cake call candy change child city clean club coat cold corn could cry cup cut dear deep deer doing doll door dress drive drop dry duck each eat eating egg end fall far farm fast feed feel feet find fire fish five fix flag floor fly food foot four fox full funny game gas gave girl give glad goat gold gone grass green grow hand happy hard hill hit hold hole hop ice inch inside job jump just keep king know lake land last late lay left leg light line little live lives long looking lost lot love mad meat men met mile milk mine miss moon more most mother move much must myself nail name need new next nice night nine north now nut off only open other our outside over page park part pay pick plant playing pony post pull put rabbit rain read rest riding road rock room said same sang saw say school sea seat seem seen set seven sheep ship shoe show sick side sing sky sleep small snow spell start stay still story take talk tall teach tell thank that told took tree truck use walk warm wash way week wet what white who why wind wish woke wood work yellow yet your zoo"

words_string = words.split()

def random_word():
    return random.choice(words_string)
random_word()

def again():
    again = input("Would you like to play again? Enter Y or N ").lower()
    if again == "y":
        game()
    else:
        print("Thanks for playing!")



def game():
    word = random_word()
    word_dashes = len(word) * '-'
    print(word_dashes)
    guessed = False
    l_guessed = []
    letters = ("abcdefghijklmnopqrstuvwxyz")
    guesses = 9
    while guessed == False and guesses > 1:
        user_guess = input("Choose a letter or guess the word: ")
        user_guess = user_guess.lower()
        if len(user_guess) == 1:
            if user_guess in word:
                print("Correct letter... you are getting close!")
                guesses -= 1
                print("You have", guesses - 1 , "guesses remaining.")
                l_guessed.append(user_guess)
                print("These are the letters you have guessed so far: ", l_guessed)
            elif user_guess not in word:
                print("Not a correct letter.")
                guesses -= 1
                print("You have", guesses - 1, "guesses remaining.")
                l_guessed.append(user_guess)
                print("These are the letters you have guessed so far: ", l_guessed)
            elif user_guessed in l_guessed:
                print("You have already guessed this letter, you did not lose a guess.")
            elif user_guess not in letters:
                print("That is not a letter, you did not lose a guess.")
        elif len(user_guess) == len(word):
            if user_guess == word:
                print("Congratulations! You guessed the word", word,"!")
                guessed = True
            elif user_guess != word:
                print("Nice try but thats not the word.")
                guesses -= 1
                print("You have", guesses - 1, "guesses remaining.")
        else:
            print("What are you doing! You're lucky you didn't lose a guess.")

        correct_dashes = ''
        if guessed == False:
            for letter in word:
                if letter in l_guessed:
                    correct_dashes += letter
                else:
                    correct_dashes += "-"
            print(correct_dashes)
        if correct_dashes == word:
            guesses = 0
            guessed = True
            print("You guessed the word, congratulations!")
    if guesses == 1:
        if user_guess != word:
            print("You lost! The word was:", word)



    again()
game()
