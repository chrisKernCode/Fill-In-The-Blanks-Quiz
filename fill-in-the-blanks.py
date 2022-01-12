# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# Texts for the game to be displayed
# Right answers for the game
text_game_level_easy = "\n___1___ is the capital of Austria. \n The capital of Germany is ___2___. \n What a wonderful vist to the capital of Spain, \n I have enjoyed spending some days in ___3___. \n Once in a lifetime you should visit the capital \n of Hungary which is ___4___.\n"
right_answers_easy = ["Vienna", "Berlin", "Madrid", "Budapest"]

text_game_level_medium = "\nFigures of speech: \n Barking up the wrong ___1___. \n Beat around the ___2___. \n An ___3___ a day keeps the doctor away. \n Calm before the ___4___. \n The early bird gets the ___5___.\n" 
right_answers_medium = ["tree", "bush", "apple", "storm", "worm"]

text_level_hard = "\nA ___1___ is created with the def keyword.\n You specify the inputs a ___1___ takes by adding ___2___ \n separated by commas between the parentheses. ___1___s by default return ___3___ \n if you don't specify the value to return. ___2___ can be standard data types such as \n string, number, dictionary, tuple, and ___4___ or can be more complicated \n such as objects and lambda functions.\n"
right_answers_hard = ["function","arguments","None","list"]

# A list of the difficulty levels to be selected by the user  
difficulty_levels = ["easy","medium","hard",]


def select_difficulty_level():
# The user is asked to select the difficulty level of his/her choice for the game:
# The user's choices are: easy', 'medium', and 'hard.'
# The user has to type in his/her choice correctly otherwise the game won't be continue.d"

    game_difficulty_question = 'Select game difficulty:' + ' Type in easy, medium or hard to start the game.\n'
  
    difficulty_user_choice = input(game_difficulty_question).lower()
    while difficulty_user_choice not in difficulty_levels:
        print ("Wrong input!" + game_difficulty_question)
        difficulty_user_choice = input(game_difficulty_question).lower()

    print("\nAlright! Let's play with level " + str(difficulty_user_choice) + "!\n")
    return difficulty_user_choice


def prepare_game(how_difficult_you_want):
#Depending on the chosen difficulty level, the cooresponsing text and answers are selected (prepared).
   
    global text_game_level_easy
    global right_answers_easy
    global text_game_level_medium
    global right_answers_medium
    global text_level_hard
    global right_answers_hard

    if how_difficult_you_want == 'easy':
        return (text_game_level_easy, right_answers_easy)
    if how_difficult_you_want == 'medium':
        return (text_game_level_medium, right_answers_medium)
    if how_difficult_you_want == 'hard':
        return (text_level_hard, right_answers_hard)
    else: select_difficulty_level()


def return_question(question_text, question_number, correct_word, total_trials = 4):
# Gap-filling of correct guesses. Text display in regards to number of trials. 

    number_of_trials = total_trials
    gap_filling = '__' + str(question_number) + '__'
    text_display = make_display(question_text, gap_filling, number_of_trials, total_trials)
    answer_user = input(text_display).lower()
    while answer_user != correct_word.lower() and number_of_trials > 1:
        number_of_trials -= 1
        text_display = make_display(question_text, gap_filling, number_of_trials, total_trials)
        answer_user = input(text_display).lower()

    if number_of_trials > 1:
        print ("Congratulations! Your answers are right!")
        return (question_text.replace(gap_filling, correct_word), question_number + 1)
    else:
        return (None, question_number + 1)


def trials():
# Defining the number of trials a user has for each word. 

    print ('\nYou have 5 trials to guess each missing word correctly!\n')
    return 5


def make_display(current_question_text, gap_filling, number_of_trials, total_trials):
# Providing information on the user's performance and trials. 
    text_display = '\nGuess the missing word:\n{}\n\n'
    text_display += ' {}? '
    text_display = text_display.format(current_question_text, gap_filling)
    if number_of_trials == total_trials:
        return text_display
    new_text_display = "Your answer is not correct! Try again.\n\n"
    if number_of_trials > 1:
        new_text_display += "You still have {} trials. \n"
    else:
        new_text_display += 'Hurry up! You only have {} more trial! \n'
    return new_text_display.format(number_of_trials) + text_display


def start_the_game():
# initializing functions for starting the game and informing the user if he/she has won the game (TRUE or FALSE).
    game_difficulty_to_play = select_difficulty_level()
    question_text, correct_response = prepare_game(game_difficulty_to_play)
    trials_amount = trials()
    to_be_solved = 1
    while to_be_solved <= len(correct_response):
        question_text, to_be_solved = return_question(question_text, to_be_solved, correct_response[to_be_solved - 1], trials_amount)
        if question_text is None:
            print ("\nSorry, you lost the game!\n")
            return False

    print (question_text + '\nCorrect! You are a genius and winner of the game!\n')
    return True


#Starting the game.
start_the_game()