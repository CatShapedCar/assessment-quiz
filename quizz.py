import time
# self explanatory
import webbrowser
# allows you to open links!!
# use webbrowser.open('https://www.example.com')
import random
#lets you randomize stuff
import turtle
#discipline turtle for people who get EVERYTHING wrong.
answer1 = 0
answer2 = 0
answer3 = 0
answer4 = 0
answer5 = 0
answer6 = 0
answer7 = 0
answer8 = 0
questionrandomize = 0
questionsanswered = 0
score = 0
#initializing stupid variables for this stupid idiot randomizing question system its so bad grr

print("Hello !")
print("Welcome to the quizshow.")
print()
print("What is your name?")
#no real purpose to asking this but i guess its courtesy
errorcounter = 0
#this variable is for detecting if someone keeps doing wrong answers on purpose
while True:
        name = str(input())
        if name == "":
            print("Your response is empty, please fix that.")
            print("Type a new response now.")
            errorcounter = errorcounter + 1
            if errorcounter > 4:
                print()
                print("It appears you are typing in wrong answers on purpose again ")
                print("You are now stuck here until you restart")
                time.sleep(100000000)
        else:
            print("Hello, " + name +"")
            break
print("Are you ready for the questions?")
errorcounter = 0
#resetting the error counter to be kind
print("1. Yes")
print("2. No")
while True:
    try:
        readiness = int(input())
        if readiness == 1:
            print("Then let's get into the questions!")
            break
        elif readiness == 2:
            print("Alright, just say 1 when you are.")
    except ValueError:
        print("Hey, please put your response as either 1 or 2. No letters please.")
        errorcounter = errorcounter + 1
        if errorcounter > 3:
            print()
            time.sleep(1)
            print("I know what you're doing.")
            time.sleep(1)
            print("Again, I will keep you here until you decide to restart.")
            time.sleep(30)
            print("There's really nothing more here for you, just restart.")
            time.sleep(100000000000)
print()
errorcounter = 0

#this is where the questions start so nice
#TODO: CHANGE THE QUESTIONS WHEN IT SAYS WHAT QUSTION NUMBER IT IS TO QUESTIONSANSWERED AND NOT QUESTIONRANDOMIZE
#yay i did it 11pm sunday 10/5/26
#add more questions probably
while questionsanswered < 8:
    #TODO: fix this shenanigans
    #this is really ineffective but it works so im very happy yayyy
    questionrandomize = random.randint(1, 8)
    if questionrandomize != 8:
        questionrandomize += 1
    else:
        questionrandomize = 1
    #this is so bad gosh
    #FINALLY FIXED THE SYSTEM IM SO HAPPY FINALLY
    #
    #i could maybe just add enough questions that it doesnt matter but thats lazy
    if questionrandomize == 1:
        if answer1 != 0:
            pass
        else:
            print("Question", questionsanswered + 1)
            print("What is the capital of the United States?")
            print("1. New York")
            print("2. Washington D.C")
            print("3. Illinois")
            print("4. California")
            while True:
                try:
                    answer1 = int(input())
                    if answer1 == 1:
                        print("Sorry, New York isn't the capital.")
                        break
                    elif answer1 == 2:
                        print("Correct! Washington D.C is in fact the capital of the United States.")
                        score = score + 1
                        print("Your score is now", score,"!")
                        break
                    elif answer1 == 3:
                        print("Sorry, Illinois isn't the capital.")
                        break
                    elif answer1 == 4:
                        print("Sorry, California isn't the capital.")
                        break
                    else:
                        print("Please enter a valid number.")
                except ValueError:
                    print("Please enter a number input, no letters or special characters.")
                    errorcounter = errorcounter + 1
                    if errorcounter > 2:
                        webbrowser.open('https://tenor.com/view/camp-dayz-no-gif-16261799211561498106')
                        #opens a silly link when you enter an invalid input too many times
            print()
            errorcounter = 0
            questionsanswered = questionsanswered + 1
    if questionrandomize == 2:
        if answer2 != 0:
            pass
        else:
            print("Question", questionsanswered + 1)
            print("What programming language is this program written in?")
            print("1. Python")
            print("2. C++")
            print("3. JavaScript")
            print("4. Unity")
            while True:
                try:
                    answer2 = int(input())
                    if answer2 == 1:
                        print("Correct! Python is this program's language.")
                        score = score + 1
                        print("Your score is now", score,"!")
                        break
                    elif answer2 == 2:
                        print("Sorry, C++ isn't the correct coding language.")
                        break
                    elif answer2 == 3:
                        print("Sorry, Javascript isn't the correct coding language.")
                        break
                    elif answer2 == 4:
                        print("Sorry, Unity isn't the correct coding language.")
                        break
                    else:
                        print("Please enter a valid number.")
                except ValueError:
                    print("Please enter a number input, no letters or special characters.")
                    errorcounter = errorcounter + 1
                    if errorcounter > 2:
                        webbrowser.open('https://tenor.com/view/camp-dayz-no-gif-16261799211561498106')
            if answer2 != 1:
                print("Just a tip, you could have looked at the top of the window for this one.")
            print()
            errorcounter = 0
            questionsanswered = questionsanswered + 1
    if questionrandomize == 3:
        if answer3 != 0:
            pass
        else:
            print("Question", questionsanswered + 1)
            print("Where is the Great Wall of China located?")
            print("1. Singapore")
            print("2. China")
            print("3. Nigeria")
            print("4. United States of America")
            while True:
                try:
                    answer3 = int(input())
                    if answer3 == 1:
                        print("Yeah not quite")
                        break
                    elif answer3 == 2:
                        print("Correct!! The Great Wall of China is, in fact, in China.")
                        score = score + 1
                        print("Your score is now", score,"!")
                        break
                    elif answer3 == 3:
                        print("Sorry, the Great Wall isn't in Nigeria.")
                        break
                    elif answer3 == 4:
                        print("I don't think the great wall is in America, sorry.")
                        break
                    else:
                        print("Please enter a valid number.")
                except ValueError:
                    print("Please enter a number input, no letters or special characters.")
                    errorcounter = errorcounter + 1
                    if errorcounter > 2:
                        webbrowser.open('https://tenor.com/view/camp-dayz-no-gif-16261799211561498106')
            print()
            errorcounter = 0
            questionsanswered = questionsanswered + 1
    if questionrandomize == 4:
        if answer4 != 0:
            pass
        else:
            print("Question", questionsanswered + 1)
            print("What is 13 * 19")
            print("1. 303")
            print("2. 281")
            print("3. 219")
            print("4. 247")
            while True:
                try:
                    answer4 = int(input())
                    if answer4 == 1:
                        print("Sorry, 13 * 19 isn't 303.")
                        break
                    elif answer4 == 2:
                        print("Sorry, 13 * 19 isn't 281.")
                        break
                    elif answer4 == 3:
                        print("Sorry, 13 * 19 isn't 219.")
                        break
                    elif answer4 == 4:
                        print("Correct, 13 * 19 is 247.")
                        score = score + 1
                        print("Your score is now", score,"!")
                        break
                    else:
                        print("Please enter a valid number, as in 1 - 4. Please don't enter the actual number.")
                except ValueError:
                    print("Please enter a number input, no letters or special characters.")
                    errorcounter = errorcounter + 1
                    if errorcounter > 2:
                        webbrowser.open('https://tenor.com/view/camp-dayz-no-gif-16261799211561498106')
            print()
            errorcounter = 0
            questionsanswered = questionsanswered + 1
    if questionrandomize == 5:
        if answer5 != 0:
            pass
        else:
            print("Question", questionsanswered + 1)
            print("What is the smallest planet in our Solar System?")
            print("1. Mars")
            print("2. Earth")
            print("3. Mercury")
            print("4. Uranus")
            while True:
                try:
                    answer5 = int(input())
                    if answer5 == 1:
                        print("Sorry, Mars isn't the smallest planet.")
                        break
                    elif answer5 == 2:
                        print("Sorry, Earth is not the smallest planet.")
                        break
                    elif answer5 == 3:
                        print("Correct, Mercury is the smallest planet in our Solar System!")
                        score = score + 1
                        print("Your score is now", score,"!")
                        break
                    elif answer5 == 4:
                        print("Wrong, Uranus is not the smallest planet.")
                        break
                    else:
                        print("Please enter a valid number, as in 1 - 4. Please don't enter the actual number.")
                except ValueError:
                    print("Please enter a number input, no letters or special characters.")
                    errorcounter = errorcounter + 1
                    if errorcounter > 2:
                        webbrowser.open('https://tenor.com/view/camp-dayz-no-gif-16261799211561498106')
            print()
            errorcounter = 0
            questionsanswered = questionsanswered + 1
    if questionrandomize == 6:
        if answer6 != 0:
            pass
        else:
            print("Question", questionsanswered + 1)
            print("What is the largest volcano in the world?")
            print("1. Lake Toba")
            print("2. Yellowstone Volcano")
            print("3. Rangitoto")
            print("4. Mauna Loa")
            while True:
                try:
                    answer6 = int(input())
                    if answer6 == 1:
                        print("Lake Toba is not the largest volcano.")
                        break
                    elif answer6 == 2:
                        print("Yellowstone is not the largest volcano.")
                        break
                    elif answer6 == 3:
                        print("Sorry, Rangitoto is not the largest volcano.")
                        break
                    elif answer6 == 4:
                        print("Correct, Mauna Loa is the world's largest volcano, located in Hawaii")
                        score = score + 1
                        print("Your score is now", score,"!")
                        break
                    else:
                        print("Please enter a valid number.")
                except ValueError:
                    print("Please enter a number input, no letters or special characters.")
                    errorcounter = errorcounter + 1
                    if errorcounter > 2:
                        webbrowser.open('https://tenor.com/view/camp-dayz-no-gif-16261799211561498106')
            print()
            errorcounter = 0
            questionsanswered = questionsanswered + 1
    if questionrandomize == 7:
        if answer7 != 0:
            pass
        else:
            print("Question", questionsanswered + 1)
            print("How many plays does Billie Jean have on Spotify? (as of 10/5/26)")
            print("1. 2,714,559,108")
            print("2. 3,101,271,399")
            print("3. 1,890,712,171")
            print("4. 2,420,192,091")
            while True:
                try:
                    answer7 = int(input())
                    if answer7 == 1:
                        print("Correct, Billie Jean currently has 2,714,559,108 plays.")
                        score = score + 1
                        print("Your score is now", score,"!")
                        break
                    elif answer7 == 2:
                        print("Wrong, Billie Jean currently has 2,714,559,108 plays, not 3,101,271,399")
                        break
                    elif answer7 == 3:
                        print("Sorry, Billie Jean doesn't have 1,890,712,171 plays currently.")
                        break
                    elif answer7 == 4:
                        print("Sorry, but Billie Jean does not currently have 2,420,192,091 plays.")
                        break
                    else:
                        print("Please enter a valid number.")
                except ValueError:
                    print("Please enter a number input, no letters or special characters.")
                    errorcounter = errorcounter + 1
                    if errorcounter > 2:
                        webbrowser.open('https://tenor.com/view/camp-dayz-no-gif-16261799211561498106')
            print()
            errorcounter = 0
            questionsanswered = questionsanswered + 1
    if questionrandomize == 8:
        if answer8 != 0:
            pass
        else:
            print("Question", questionsanswered + 1)
            print("How many answers does this question have?")
            print("1. 2")
            print("2. 1")
            while True:
                try:
                    answer8 = int(input())
                    if answer8 == 1:
                        print("Correct.")
                        score = score + 1
                        print("Your score is now", score,"!")
                        break
                    elif answer8 == 2:
                        print("There is 2 answers. But the answer for 2 is 1.")
                        break
                    else:
                        print("Yeah, that's really off.")
                        break
                except ValueError:
                    print("Please enter a number input, no letters or special characters.")
                    errorcounter = errorcounter + 1
                    if errorcounter > 2:
                        webbrowser.open('https://tenor.com/view/camp-dayz-no-gif-16261799211561498106')
            print()
            errorcounter = 0
            questionsanswered = questionsanswered + 1
time.sleep(1)
print()
print("Thank you for playing!")
print("You ended with a score of", score,"!")
percentage = 0
# initializing it first
percentage = 100 / 8
percentage = percentage * score
roundedpercent = round(percentage, 1)
print("That's",roundedpercent,"%.")
time.sleep(1)
if score == 8:
    print("Congratulations on getting all of them right!")
    print("Watch this")
    webbrowser.open('https://tenor.com/view/confetti-gif-27343800')
    time.sleep(4)
    print("Hopefully that worked")
    time.sleep(1)
    print("If it didnt, it was meant to open a link for you.")
elif score >= 6:
    print("Good job on getting so many correct!")
elif score >= 4:
    print("Congrats on your score!")
elif score == 3:
    print("Congrats on your score!")
    print("If you would like, try getting a higher score next time!")
elif score == 2:
    print("Congrats on your score!")
    print("If you would like, try getting a higher score next time!")
elif score == 1:
    print("Congrats on your score!")
    print("If you would like, try getting a higher score next time!")
else:
    print("Well, 0 is unfortunate but good job regardless.")
    print("Sorry if that sounded rude")
    time.sleep(1)
    print("I'll bring the turtle for you.")
    time.sleep(1)
    t = turtle.Turtle()
    t.speed(2)
    turtleturns = 0
    while turtleturns < 4:
        t.forward(100)
        t.right(90)
        turtleturns += 1
    turtle.done()
print("Anyway, thank you for playing!")
print()
print("------")
print("Credits")
print()
print("Tyler - All of the coding")
print("Zeeshan - Great Wall of China question and Testing")
print("Taua - Nothing but he wanted to be here (Testing sometimes)")
print()
print("------")
print()
time.sleep(1)
print("Press enter to end the program.")
endprogram = input()
#This just waits for an input, and since nothing is after it, it will instantly end when it is entered.