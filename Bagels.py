import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    """The main game loop for the bagels game"""
    print("{0:>40}".format("Bagels, A deductive logic game"))
    print(f"""I am thinking of a {NUM_DIGITS}-digit number with no repeated digits
    try to guess what it is. Here are some clues:
When I say:             That means
Pico                      One digit is correct but in the wrong position
Fermi                     One digit is correct and in the right position
Bagels                    No digit is correct""")

    while True:
        secretnum = getsecretnum()
        print("{0:>30}".format("I have thought up a number"))
        print(f"You have {MAX_GUESSES} guesses to get it.")

        numguesses = 1
        while numguesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numguesses}")
                guess =input("> ")

            clues = getclues(guess,secretnum)
            print(clues)
            numguesses += 1

            if guess == secretnum:
                break
            if numguesses > MAX_GUESSES:
                print("You ran out of guesses. ")
                print(f"The answer was {secretnum}")

        print("Do you want to play again? (yes or no) ")
        if not input("> ").lower().startswith("y"):
            break
    print("Thank you for playing")

def getsecretnum():
    """Returns a string made up of unique random digits"""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secretnum = ""
    for i in range(NUM_DIGITS):
        secretnum += str(numbers[i])
    return secretnum

def getclues(guess, secretnum):
    """Returns a string with the pico,fermi,bagels clues
    for a guess and secret number pair"""
    if guess == secretnum:
        return "You got it"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            #A correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secretnum:
            # A correct digit is in the incorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return  " ".join(clues)

main()