import random
import os

print("Game started")
def load_words():
    word_list = []   # list which store all the words jun chai file bata read gariyeko hunxa
    try:
        folder = os.path.dirname(__file__)
        path = os.path.join(folder, "words.txt")
        file = open(path, "r")
        # file = open("words.txt","r")
        for line in file:
            word = line.strip().upper()
            word_list.append(word)
        file.close()
        return word_list
    except FileNotFoundError:
        print("Error:The target file was not found.")
        return word_list

def choose_word(word_list):
    computer = random.choice(word_list)
    return computer
 #
    

def is_valid_guess(guess, word_list):
    if len(guess) != 5:
        return False
    if not guess.isalpha():  #isalpha ley valid sabda haru matra entry hos vanera ensure garxa
        return False
    if guess.upper() not in word_list:  
        return False
    
    return True 
 
def check_guess(guess,hidden_word):
    result = ["."]*5
    leftover = {}     #dictionary
    #Exact match find gareyko
    for i in range(5):
        if guess[i] == hidden_word[i]:
            result[i] = "_/"
        else:
            letter = hidden_word[i]
            leftover[letter] = leftover.get(letter,0) + 1
    
    for i in range(5):
        if result[i] != "_/":
            letter = guess[i]
            if letter in leftover and leftover[letter] > 0:
                result[i] = "*"
                leftover[letter] -=1
    
    return result

def display_rules():
    print("Welcome to the Python Wordles!")
    print("Guess the hidden Five-letter word.")
    print("Symbols:")
    print("_/ = correct letter and correct position")
    print("* = correct letter but wrong position")
    print(". = letter not present")
    print("You have 6 attempts.")

def play_game(word_list, hidden_word):
    attempts = 6
    
    while attempts >0:
        guess = input("Enter a 5-letter guess: ").upper()

        if not is_valid_guess(guess,word_list):
            print("Invalid guess! Try again.")
            continue
        else:
            result = check_guess(guess,hidden_word)
            print("Result: ", " ".join(result))

        if result == ["_/","_/","_/","_/","_/"]:
            print("Congratulations!")
            print(f"You guess it in {6- attempts + 1} attempts.")
            print("End of the game")
            return
        
        attempts -=1
        print(f"You have {attempts} attempts left.") 
        
    print("Game Over!")
    print(f"The hidden word was: {hidden_word}")


def main():
    display_rules()
    word_list = load_words()
    hidden_word = choose_word(word_list)
    play_game(word_list,hidden_word)




if __name__ == "__main__":
    main()     
    
