# ✧･ﾟ:* ✧･ﾟ:HANGMAN GAME Project :･ﾟ✧*:･ﾟ✧
**Demonstration video: https://youtu.be/84bm6jGY1G4**

This project is the final project for **01219114/01219115 Programming 1**.
In this project, I have met all the requirements from teacher which are
1. Display results on Python Turtle Graphics window; direct use of tkinter
   window is not allowed
2. Interact with user on the console, i.e., ask input and show output 
3. Implement at least 3 classes, one of which contains a list or dict 
   of objects from another class as an attribute
4. Read/write data from/to text files

## ♡ What the project is?

This project is a Hangman game that we usually play when we were young
but the game will be shown and play in the computer, not on the
blackboard.

### ☀ How to play?
At the start of the game, you will go to the main menu page to 
choose whether you want to start the game or want to exit the game. 
* If you want to start the game, you must press `1` + `enter`.
* If you want to exit the game you can press `2` + `enter`.

Then a window will appear for selecting the difficulty level of the game.
The levels of the game are divided according to the difficulty of the words.
You can choose to play according to your aptitude. There are three levels 
in this game:

* **Basic level [1]** : contains vocabulary words for elementary students.
* **Intermediate level [2]** : contains vocabulary words for middle and high school
  students.
* **Expert level [3]** : contains vocabulary words for university students.

You can select one of these three levels by pressing `number` + `enter` and the game
will start.

After that, you need to choose how many round you want to play the game in 
that level. Actually, there are 50 words in each level, so you can choose to
play from 1 time to 50 times. The game will randomly choose word(s) for you and words
will never be randomly repeated more than once.

You need to guess an alphabets for multiple times until you fill all the blanks with
the correct alphabets. 
* If you choose the right one until you complete the word, you will win. 
* If you choose wrong alphabets for 9 times and not complete the 
word, the game will over.

After finish the game, it will return you back to the main menu page and you 
can decide whether you want to play again or exit the game. 

  
## ♡ Modules

My game consists of five modules as the following...

### ☀ 1. Module `vocab.py`

This module contains the `Vocabulary` class. There are 3 methods in this class 
which are:
* **random_word()** → open the `.txt` file and return a list of vocabulary words. 
* **index_clue()** → random the clue for the user.
* **count_correct()** → count how many alphabets that user need to fill in to win this game.

### ☀ 2. Module `vocabContainer.py`

This module contains the `VocabContainer` class for collecting
the number of vocabulary words you want to play. There are 1 method
in this class which are:
* **add()** → collect `n` vocabulary word(s) as a user wants.

### ☀ 3. Module `outplay.py`

This module contains the `Outplay` class for setting the game on the screen
that is not included in the game processing. There are 8 methods in this class
which are:
* **rec()** → use the Python Turtle to draw the rectangle to decorate the screen.
* **choose_start()** → use the Python Turtle Graphics window to interact with the user by asking whether the user 
  wants to start or exit the game.
* **choose_level()** → use the Python Turtle Graphics window to interact with the user by asking whether the user
  wants to play which level (from 3 levels) in this game.
* **times_input()** → use the Python Turtle Graphics window to interact with the user by asking how many times
  the user wants to play this game (in one round).
* **board()** → use the Python Turtle to draw the board background for wrong alphabet input.
* **lose()** → use the Python Turtle to draw the page showing that the user lose this round.
* **win()** → use the Python Turtle to draw the page showing that the user win this round.
* **summarize()** → use the Python Turtle to summarize the score for user.

### ☀ 4. Module `play.py`
This module contains the `Play` class for setting the game on the screen
in the game processing parts. There are 7 methods in this class
which are:
* **update()** → update the blank with user input.
* **show_update()** → show the clue of the word.
* **stage()** → set up the screen for this game.
* **pop_up_check()** → tell the user that is the input alphabet is correct or not.
* **header()** → show "HANGMAN GAME" on top of the screen.
* **draw_heart()** → draw heart status in the top left corner.
* **hangman()** → draw hangman on the screen.

### ☀ 5. Module `main.py`
This module implements the game that let the users play by gathering all classes together.


## ♡ Text file
This project consists of 3 `.txt` file including:
* `basic.txt`
* `intermediate.txt`
* `expert.txt`


## ♡ Message from me ♡

♡♡♡ I hope you will enjoy my game ♡♡♡

Thank you for paying an attention.
