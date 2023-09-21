import random
from unidecode import unidecode

class Hangman:

    def __init__(self) -> None:
        with open('./word/liste_francais.txt', "r") as file:
            lines = file.readlines()
        self.word = unidecode(random.choice(lines).strip())
        print(self.word)
        self.word_guess = ['_'] * len(self.word) 
        self.letter_try = []
        self.chances = 10
        self.attempts = 0

    def guess(self, letter):
        if letter == self.word:
            return "correct"  # L'utilisateur a deviné le mot complet
        elif letter.isalpha() and len(letter) == 1:
            if letter in self.word:
                self.attempts += 1
                for i in range(len(self.word)):
                    if self.word[i] == letter:
                        self.word_guess[i] = letter
                if '_' not in self.word_guess:
                    return "correct"  # L'utilisateur a deviné toutes les lettres
                return "correct"  # La lettre est correcte
            else:
                self.chances -= 1
                if letter not in self.letter_try: self.letter_try.append(letter) # On ajoute les lettres de l'utilisateur
                return "incorrect"  # La lettre est incorrecte
        else:
            return "invalid"  # La lettre n'est ni valide ni correcte


    def is_game_over(self):
        return self.chances == 0
    
    def is_winner(self):
        return True if "_" not in self.word_guess else False
    
    def reset_game(self):
        # Réinitialiser le mot à deviner
        with open('./word/liste_francais.txt', "r") as file:
            lines = file.readlines()
        self.word = unidecode(random.choice(lines).strip())

        print(self.word)
        
        # Réinitialiser le mot partiellement deviné
        self.word_guess = ['_'] * len(self.word) 

        # Réinitialiser les lettres essayées
        self.letter_try = []

        # Réinitialiser les chances
        self.chances = 10

        # Réinitialiser le nombre d'essais
        self.attempts = 0

        # Réinitialiser l'état du jeu
        self.isFinished = False
        self.isWinner = False


    def display(self):
        print(" ".join(self.word_guess))