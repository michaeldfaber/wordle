import os
import random

word = ''
wordsFilename = 'words.txt'
guessNumber = 1
guesses = []

green = '\033[92m'
yellow = '\033[93m'
end = '\033[0m'

def clear():
    os.system('clear')

def loadWord():
    global word
    with open(wordsFilename) as fp:
        count = 1
        lineNumber = random.randint(1,12972)
        for line in iter(fp.readline, ''):
            if count == lineNumber:
                word = str(line).upper()
                return
            else:
                count = count + 1

def isValidGuess(guess):
    if len(guess) != 5:
        return False
    
    for character in guess:
        if character.isdigit():
            return False

    with open(wordsFilename) as fp:
        for line in iter(fp.readline, ''):
            if guess == line.replace('\n', '').upper():
                return True

    return False

def isCorrectGuess(guess):
    for i in range(0,5):
        if guess[i] != word[i]:
            return False
    return True

def colorizeGuess(guess):
    characterDict = {}
    for i in range(0,5):
        if word[i] in characterDict.keys():
            characterDict[word[i]] = characterDict[word[i]] + 1
        else:
            characterDict[word[i]] = 1

    colorizedGuess = {
        0: '',
        1: '',
        2: '',
        3: '',
        4: '',
    }
    
    # first pass, correct letters in correct position
    for i in range(0,5):
        if guess[i] == word[i]:
            colorizedGuess[i] = green + guess[i] + end
            characterDict[guess[i]] = characterDict[guess[i]] - 1

    # second pass, correct letters in wrong position, and wrong letters
    for i in range(0,5):
        if colorizedGuess[i] != '': # correct letter created in first pass
            continue
        if guess[i] in characterDict.keys():
            if characterDict[guess[i]] > 0:
                colorizedGuess[i] = yellow + guess[i] + end
                characterDict[guess[i]] = characterDict[guess[i]] - 1
                continue
        
        colorizedGuess[i] = guess[i]

    return colorizedGuess[0] + colorizedGuess[1] + colorizedGuess[2] + colorizedGuess[3] + colorizedGuess[4]

def printGuesses():
    count = 1
    for guess in guesses:
        print(str(count) + "/6:\t" + guess)
        count = count+1
    print("\n")

def main():
    global guessNumber
    loadWord()
    print("\nWelcome to " + green + "W" + end + yellow + "o" + end + green + "r" + end + yellow + "d" + end + green + "l" + end + yellow + "e" + end + "!")
    print("\nEnter your first guess:")

    while guessNumber <= 6:
        validGuess = False
        while (validGuess == False):
            guess = str(raw_input()).upper()
            if isValidGuess(guess) == False:
                clear()
                printGuesses()
                print(guess + " is not a valid guess. Try again")
                continue
            else:
                validGuess = True

            if isCorrectGuess(guess):
                print(green + guess + end + " is correct! You won! Well done!\n")
                return
        
        guesses.append(colorizeGuess(guess))
        guessNumber = guessNumber + 1
        clear()
        printGuesses()

    print("You lost! The word was: " + word)

if __name__ == "__main__":
    main()