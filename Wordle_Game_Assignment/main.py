import random
import subprocess
import os

print("Game started")
def load_words():
    word_list = []   # list which store all the words jun chai file bata read gariyeko hunxa
    try:
        file = open("words.txt","r")
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
    leftover = {}
    #Exact match find gareyko
    for i in range(5):
        if guess[i] == hidden_word[i]:
            result[i] = "_/"
        else:
            letter = hidden_word[i]
            leftover[letter] = leftover.get(letter,0) + 1
    
    for i in range(5):
        if result[i] != "_/":
            letter = guess(i)
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
    print("You have total attempts.")

def play_game(guess,computer):
    if guess == computer:
        print("Congratulations!")
        print("You guess the game in X attempts.")
        print("End of the game")
    else:
        print("Game Over!")    
        print(f"The correct word was: {computer}")


def main():
    play_game()



if __name__ == "__main__":
    main()     
    
