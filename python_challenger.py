#level selection
level_options = ["easy","medium","hard","expert"]

#Quiz questions and answers
quiz_sentences = ["Functions: Your [__1__] should use [__2__]s appropriately to avoid [__3__]. Function parameters should have [__4__] names and should all be used in the body of the [__2__].",
    "It might act upon other things besides number, were objects found whose [__1__] fundamental relations could be expressed by those of the abstract science of [__2__], and which should be also susceptible of [__3__] to the action of the operating notation and [__4__] of the engine. - Augusta [__5__] King",
    "Be not afraid of [__1__]: some are [__2__] great, some [__3__] [__1__], and some have [__1__] thrust upon [__4__] - [__5__] Shakespeare",
    "I have a [__1__] that one day this nation will [__2__] up and live out the true meaning of its creed: 'We hold these truths to be [__3__]: that all men are created [__4__].' I have a [__1__] that one day on the red hills of [__5__] the sons of former [__6__]s and the sons of former [__6__] owners will be able to sit down together at the table of [__7__]."]
number_of_blanks = [4,5,5,7]
quiz_answers = [["code","function","repetition","logical"],
    ["mutual","operations","adaptations","mechanism","Ada"],
    ["greatness", "born", "achieve","them","William"],
    ["dream","rise","self-evident","equal","Georgia","slave","brotherhood"]]

#User to select difficulty
level_selected = None
while not level_selected in [0,1,2,3]:
    index = 0
    print "#"*35
    print "Welcome to the Python Challenger!"
    print "Please choose your quiz level:"
    for print_levels in level_options:
        print str(index) + " - " + print_levels
        index+=1
    level_selected = int(raw_input("Level selected: "))
    print ""

#User to select number of guesses per question
number_of_guesses = None
while not number_of_guesses in [1,2,3,4,5,6,7,8,9,10]:
    print "#"*35
    print "Please input number of guesses you'd like to have for each quetion (1-10):"
    number_of_guesses = int(raw_input("Number of guesses per question selected: "))
    print ""
print "You have " + str(number_of_guesses) + " guesses per blank"
print ""
print "#"*35
print "This is the " + level_options[level_selected] + " quiz"
print ""

#Checks if answer provided by user is correct and replaces answer holder and
#reprints sentence if correct
def check_answer(answer, blank_number, level_selected):
    if answer == quiz_answers[level_selected][blank_number-1]:
        print "Correct! Moving onto the next blank!"
        print ""
        index = 0
        for word in quiz_sentence_split:
            if "[__" + str(blank_number) + "__]" in word:
                word = word.replace("[__" + str(blank_number) + "__]", answer)
                quiz_sentence_split[index] = word
            index+=1
        print " ".join(quiz_sentence_split)
        print ""
        return True
    else:
        print "Wrong answer! Please try again!"
        print ""
        return False

#Keeps track of number of guessses left and returns if answer provided by
#user is correct
def guess_counter(max_guesses, blank_number, level_selected):
    guesses_remaining = max_guesses
    answer_is_correct = False
    while guesses_remaining > 0 and not answer_is_correct:
        print "Number of guesses remaining: " + str(guesses_remaining)
        answer = raw_input("Guess the answer for [__" + str(blank_number) + "__]: ")
        answer_is_correct = check_answer(answer, blank_number, level_selected)
        guesses_remaining-=1
    return answer_is_correct

#Creates list of from sentence and controls number of times user will loop
#through the game
blank_number = 1
counter = number_of_guesses
answer_is_correct = True
quiz_sentence_split = quiz_sentences[level_selected].split()
print " ".join(quiz_sentence_split)
print ""
while blank_number <= number_of_blanks[level_selected] and answer_is_correct:
    answer_is_correct = guess_counter(number_of_guesses, blank_number, level_selected)
    blank_number+=1

#Determines if the user has managed to solve the sentence or not
if blank_number == number_of_blanks[level_selected] + 1 and answer_is_correct:
    print "Congratulations, you solved the entire sentence!"
else:
    print "Sorry, you were not able to solve the entire sentence"
