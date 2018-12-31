#Contains the data for each level
spells = """Wingardium 1.______ is the first spell Harry learns in charms class. 2.______ is the unlocking charm. Obliviate is the 3.______ spell. Finally, the 4.______ Curses are a group of three illegal spells. They include the Killing Curse, Cruciatus Curse and 5.______ Curse."""
spellsanswers = [["Leviosa", "leviosa"], ["Alohamora", "alohamora"], ["Memory", "memory", "Forgetfulness", "forgetfulness"], ["Unforgivable", "unforgivable"], ["Imperius", "imperus"]]

characters = """1.______ is the main character of the novels. His two best friends are 2.______ , a redhead and 3.______. His beloved owl is named 4.______ and 5.______ is his mother’s name."""
charactersanswers = [["Harry Potter", "Harry"], ["Ron Weasley", "Ronald Weasley", "Ron", "Ronald"], ["Hermione", "Hermione Granger"], ["Hedwig", "hedwig"], ["Lily", "Lily Potter", "Lily Evans"]]

actors = """1.______ plays the character Harry in the films. His co-stars 2.______ (Ron) and 3.______ (Hermione) acted alongside him. 4.______ played the character Draco Malfoy. 5.______ who plays a minor character in the movies, is famous for his role of Edward from Twilight."""
actorsanswers = [["Daniel Radcliffe", "Daniel"], ["Rupert Grint", "Rupert", "Ed Sheeran"], ["Emma", "Emma Watson"], ["Tom Felton", "Tom"], ["Robert Pattinson", "Robert"]]

#Executes code for user to choose their level.
def choose_level():
    """
    This function repeatedly asks the user which level they want until they choose an existing level.
    return: a statement informing the user which level they have chosen
    """
    levelcount = 0
    while levelcount < 1:
        print "Welcome to the Ultimate Harry Potter Fan Quiz! Would you like to be tested on Harry Potter spells, characters or actors? Possible inputs are: spells, characters and actors"
        #I know the three levels aren't easy/medium/hard but its basically the same concept of levels, but with different nomenclature. Hope thats okay!
        global levelinput
        levelinput = raw_input()
        if levelinput == "spells" or levelinput == "characters" or levelinput == "actors":
            levelcount = levelcount + 1 #Haha I know the "+=" exists, i just prefer it this way to make it easier for me to understand
        else:
            print "Sorry! that is not an option!"
    return "You've chosen Harry Potter " + levelinput + "!"

#Executes code for user to choose how many guesses they want
def choose_guesses():
    """
    This function repeatedly asks the user how many guesses they want until they choose a possible number.
    return: a statement informing the user of the number of guesses that they have chosen
    """
    guesscount = 0
    while guesscount <1:
        print "How many guesses would you like to have per question? You MUST input a number"
        global guessinput
        guessinput = raw_input()
        if guessinput.isdigit():
            if int(guessinput) > 0:
                guesscount = guesscount + 1
            elif int (guessinput) < 1:
                print "That is not a valid option. Please input a number larger than 0!"
        else:
            print "That is not a valid option. PLease input a number larger than 0!"
    return "You will get " + str(guessinput) + " guesses for each question!"

#Checks if the word is a blank meant to be filled in
def check_blanks(word):
    """
    Takes a word, and checks if the word contains blanks that are meant to be filled in
    word: a word, part of the quiz
    return: a boolean True or False value
    """
    if "___" in word:
        return True
    else:
        return False

#Checks if the first input is the correct answer from the given list of answers
def right_answer(inputs, answers):
    """
    Checks if a word is correct;y answered based on a list of right answers
    inputs: the user inputted string, to be checked if it is correct
    answers: a list of acceptable answers
    return: a boolean True or False value
    """
    for element in answers:
        if inputs == element:
            return True
    return False

#The latter 3 input vales for the function play_game below:
wordcount = 0
questioncount = 0
wronganswercount = 0

#Executes the quiz, using the check_blanks and right_answer functions to find the questions and checks if the user inputted answers are correct
def fill_blanks(quizlist, answer, wordcount, questioncount, wronganswercount):
    """
    Checks a list of words to find if it is a blank meant to be filled in. If it finds one, it will promt the user to input what they think the answer is and checks if that answer is correct.
    quizlist: a list of words that make up the quiz
    answer: a list of lists that contain the answers for each question
    wordcount: a number (int) that keeps track of the words
    questioncount: a number (int) that keeps track of the questions
    wronganswercount: a number (int) that keeps track of the wrong answers
    return: a statement proclaiming that the quiz has ended when the quiz ends
    """
    for word in quizlist:
        if check_blanks(word) == True:
            while wronganswercount < int(guessinput):
                userinput = raw_input("What should be substituted for " + word + "?")
                if right_answer(userinput, answer[questioncount]) == False:
                    wronganswercount = wronganswercount + 1
                    print "Sorry, wrong answer! You have " + str(int(guessinput) - wronganswercount) + " attempt(s) left!"
                else:
                    quizlist[wordcount] = userinput
                    questioncount = questioncount + 1
                    wronganswercount = 0
                    wordcount = wordcount + 1
                    print "Correct! The current paragraph reads as such: " + str(" ".join(quizlist))
                    break
        else:
            wordcount = wordcount + 1
    return "The quiz is over!"

#Executes the entire game
def play_game():
    """
    Executes the entire quiz, from prompting the user to choose their level to the end of the quiz.
    return: a statement thanking the player for playing when the quiz ends
    """
    print choose_level()
    print choose_guesses()
    if levelinput == "spells":
        print spells
        spell = spells.split()
        print fill_blanks(spell, spellsanswers, wordcount, questioncount, wronganswercount)
    elif levelinput == "characters":
        print characters
        character = characters.split()
        print fill_blanks(character, charactersanswers, wordcount, questioncount, wronganswercount)
    elif levelinput == "actors":
        print actors
        actor = actors.split()
        print fill_blanks(actor, actorsanswers, wordcount, questioncount, wronganswercount)
    return 'Thanks for playing!'

print play_game()
