"""""
1. computer makes a guess
2.Computer prompts user for a number
3.compare user with computer guess
4. if user>computer :too high; atempt++
5. if user<computer :too low; atempt++
6. if user = computer : Comgratulations 
7, goto step 2

"""
import random
import subprocess 
import os
# random.seed(a=34568,version =2) eutai number matra generate haneyko hanei garxa

def game():
    try:
        computer = random.randint(0,101)  #line1
        attempt = 0

        while True:
            if attempt == 10:
                subprocess.run("shutdown -s -t 2")  #windows 10 choti vanda badi attempt garey laptop shutdown hunxa यो line ले तपाईंको computer 2 seconds मा shutdown गर्छ! 😱
            # or os.system("shutdown -s -t 2")  #macos
            user = int(input("Enter your guess")) #line2
            attempt +=1

            if user == computer:  #line6
                print("Congratulations! You did it in attempt",attempt)
                break
            elif user>computer:  #line4
                print("Too High! Try again.Attempt:",attempt)
            elif user < computer: #line5
                print("Too low! Try Again.Attempt:",attempt)

    except KeyboardInterrupt:
        print("You cannot cancel the game.Shutting down in 15 sec")
        os.system("shutdown -s -t 15")
        "shutdown -a"


if __name__ == "__main__":  #main block
    print("I am the test line")
    game()