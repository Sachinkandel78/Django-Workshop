
                    PYTHON WORDLE GAME
                    

Project Name:
-------------
Python Command-Line Wordle Game

Author:
-------
Sachin Kandel

Description:
------------
This project is a command-line implementation of the popular
Wordle game using Python.

The program randomly selects a five-letter English word from
a dictionary file (words.txt). The player has six attempts to
guess the hidden word.

After every valid guess, feedback is provided using symbols:

_/  = Correct letter in the correct position
*   = Correct letter but in the wrong position
.   = Letter is not present in the hidden word

The game continues until the player guesses the word or runs
out of attempts.

-----------------------------------------------------------
Project Structure
-----------------------------------------------------------

wordle/
│
├── main.py
├── words.txt
└── README.txt

-----------------------------------------------------------
Features
-----------------------------------------------------------

• Loads words from an external text file.
• Randomly selects a hidden five-letter word.
• Accepts user guesses.
• Validates user input.
• Prevents invalid words from counting as attempts.
• Displays feedback after every guess.
• Shows remaining attempts.
• Displays a winning or losing message.

-----------------------------------------------------------
How to Run
-----------------------------------------------------------

1. Make sure both files are in the same folder:

   main.py
   words.txt

2. Open a terminal or command prompt.

3. Navigate to the project folder.

4. Run the program using:

   python main.py

-----------------------------------------------------------
Game Rules
-----------------------------------------------------------

1. The computer randomly selects a hidden five-letter word.

2. The player has six attempts to guess the word.

3. Every guess must:
   - Contain exactly five letters.
   - Contain only alphabetic characters.
   - Exist in words.txt.

4. Invalid guesses do not reduce the number of attempts.

5. Feedback Symbols:

   _/  = Correct letter and correct position
   *   = Correct letter but wrong position
   .   = Letter not present

6. Guess the word before all six attempts are used.

-----------------------------------------------------------
Functions Used
-----------------------------------------------------------

load_words()
    Reads all words from words.txt.

choose_word()
    Randomly selects a hidden word.

is_valid_guess()
    Checks whether the user's guess is valid.

check_guess()
    Compares the guess with the hidden word and generates
    feedback.

display_rules()
    Displays the game instructions.

play_game()
    Handles the game loop.

main()
    Starts the program.

-----------------------------------------------------------
Error Handling
-----------------------------------------------------------

The program handles:

• Missing words.txt file
• Words shorter than five letters
• Words longer than five letters
• Numbers
• Symbols
• Invalid dictionary words


-----------------------------------------------------------
Sample Output
-----------------------------------------------------------

Welcome to the Python Wordle!

Guess the hidden Five-letter word.

Enter a 5-letter guess:
APPLE

Result:
_/ . . . _/

You have 5 attempts left.


Thank You
