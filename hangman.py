import random

class Hangman:

    def __init__(self) -> None:
        with open('liste_francais.txt', "r") as file:
            lines = file.readlines()
        self.word = random.choice(lines).strip()
        self.word_guess = ['_'] * len(self.word) 
        self.chances = 7

    def play(self):
        isFinished = False
        isWinner = False

        while not isFinished and self.chances > 0:
            guess_word = self.guess()
            if guess_word in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == guess_word:
                        self.word_guess[i] = guess_word
                self.display()
                if '_' not in self.word_guess:
                    isFinished = True
                    isWinner = True
            else:
                self.chances -= 1
                self.display()
                print(f"Chances remaining: {self.chances}")

        if isWinner:
            print("Congratulations! You won.")
        else:
            print(f"Sorry, you lost. The word was '{self.word}'.")

    def guess(self):
        while True:
            guess_word = input("Choose a letter [A-Z, a-z]: ").lower()
            if guess_word.isalpha() and len(guess_word) == 1:
                return guess_word
            else:
                print("Please enter a valid single letter.")

    def display(self):
        print(" ".join(self.word_guess))