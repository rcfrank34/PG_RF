import random

number = random.randint(0,3)

words = ["Wizard","Trigger","Computer","Mouse"]
hint1 = ["Uses magic","Something you push","Keys and mice","Gets chased by cats"]
hint2 = ["Has a wand","On Xbox controller","Internet is on this","Has a tail"]

secretword = words[number]
guess = ""
counter = 1


while True:
    print("Guess my secret word!")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer.")
    guess = input()

    if guess == secretword:
        print("You win! You are the actual GOAT.")
        if counter == 1
            print("It took you " + str(counter) + " guess.")
        elif counter >=2
            print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "give up":
        print("Wow. You gave up. So lazy. I am shaking my head in disappointment.")
        print("You failed " + str(counter) + " times.")
        break

    else:
        print("Try again.")
        counter +=1

    

