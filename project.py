from wordlist import random_word, get_categories, random_word2
# import random
# Words = ("Football","Point Guard","Quaterback","Soccer","Intersteller","The Martian","Star Wars","Avengers","Algorithm","Cybersecurity","Encryption","software","JavaScript")
hangman_board = {0:(" ",
                    " " ,
                    " "),
                 1: (" o ", 
                     " ",
                     " "),
                 2: ("o",
                     "|",
                     " "),
                 3: (" o",
                     "/|",
                     " "),
                 4: (" o",
                     "/|\\",
                     " "),
                 5: (" o",
                     "/|\\",
                     "/"),
                 6: (" o",
                     "/|\\",
                     "/ \\ ")}
                     
#for line in hangman_board[6:
   # print(line)
def display_man(wrong_gusses):
    # print("**********")
    for line in hangman_board[wrong_gusses]:
        print(line)
    print("================")
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    pass
def main():
    answer = random_word()
    # print(answer)
    #hint = ["_"] * len(answer)
    # found =  [False for i in range(len(answer))]
    # print(answer)
    # print(found)
    
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    print("Categories to choose from: ", end="")
    for cat in get_categories():
        print(cat , " ", end="")
    print()
    choice = input ("Which category would you like?: ").lower().capitalize()
    answer = random_word2(choice)
    hint = ["_"] * len(answer)
    # print(answer)

    while  is_running:
        # print(found)
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        guessed_letters.add(guess)
        if guess in answer:
              for i in range(len(answer)):
                if guess == answer[i]:
                    # found[i] = True
                    hint[i] = guess
        else:
            wrong_guesses += 1
        # print(hint)
        print("Guessed letters: ", guessed_letters)
        if not '_' in hint:
            print("YOU WINNN!!!!")
            break
        if wrong_guesses == 6:
            print("You lost!!!")
            break


if __name__ == "__main__":
    main()
