import random;
randomNumbers = 2
maxNumberOfGuesses = 10
def main():
    # This loop stores the number the player needs to guess.
    while True:
        doAgain = True
        print("Bagels, a deductive logic game.\nBy Zack Augustine zacka37@gmail.com\nGuess a random generated number based on clues\n")
        print('I am thinking of a ',randomNumbers,' digit number with no repeated digits.\nTry to guess what it is. Here are some clues:')
        print("When I say:      That means:\n Pico             One digit is currect but in the wrong position.\n Fermi            One digit is currect and in the right position.\n Bagels           No digit is correct.") 
        secretNumber = getSecretNumber()
        print('I have thought of a number that is ',randomNumbers,' digits.\n You have ', maxNumberOfGuesses,' guesses to get it right.'.format(maxNumberOfGuesses))
        numberOfGuesses = 1
        while numberOfGuesses <= maxNumberOfGuesses:
            guess = ''
            while len(guess) != randomNumbers or not guess.isdecimal():
                print('Guess #{}: '.format(numberOfGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNumber)
            print(clues)
            numberOfGuesses += 1
            if guess == secretNumber:
                break
            if numberOfGuesses > maxNumberOfGuesses:
                print('You ran out of guesses.\nThe answer was {}. '.format(secretNumber))
        # Do you want to play again?
        print("Do you want to play agian? (Y or N)")
        if not input('> ').lower().startswith('y'):
            doAgain = False
            break
    print("Thank you for playing.")
def getSecretNumber():
    numbers = list('123456789')
    random.shuffle(numbers)
    secretNumber = ''
    for i in range(randomNumbers):
        secretNumber += str(numbers[i])
    return secretNumber
def getClues(guess, secretNumber):
    if guess == secretNumber:
        print('You got it')
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append('Fermi')
        elif guess[i] in secretNumber:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
main()