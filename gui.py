import tkinter as tk
from hangman import Hangman
from constants.constant import SCREEN_WIDTH, SCREEN_HEIGHT, ALPHABET

class Gui:

    def __init__(self) -> None:
        self.hangman = Hangman()
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        # Créez la fenêtre principale
        self.root = tk.Tk()
        self.root.title('Hangman GUI')

        # Créez un canvas pour dessiner le pendu
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        # Créez un bouton pour soumettre la lettre souhaitée
        self.button_guess = tk.Button(self.root, text='Guess', command=self.make_guess)
        self.button_guess.pack()

        # Label pour le nombre de chances
        self.chances_remaining_label = tk.Label(self.root, text=f"Chances remaining: {self.hangman.chances}")
        self.chances_remaining_label.pack()

        # Label pour le mot partiellement deviné
        self.word_to_guess = tk.Label(self.root, text=f"{' '.join(self.hangman.word_guess)}")
        self.word_to_guess.pack()

        # Label pour le message d'invitation
        self.instruction_label = tk.Label(self.root, text="Choose a letter:")
        self.instruction_label.pack()

        # Créez les boutons pour l'alphabet
        self.alphabet_buttons = []
        for letter in ALPHABET:
            button = tk.Button(self.root, text=letter.upper(), command=lambda l=letter: self.guess_letter(l))
            self.alphabet_buttons.append(button)
            button.pack(side=tk.LEFT)

    def guess_letter(self, letter):
        # Appeler la méthode guess() de la classe Hangman avec la lettre cliquée
        guess_result = self.hangman.guess(letter)
        
        if guess_result == "correct":
            # La lettre est correcte, mettre à jour l'affichage du mot partiellement deviné
            self.set_word_to_guess(self.hangman.word_guess)
            if '_' not in self.hangman.word_guess:
                self.show_message("Congratulations! You've won.")
                self.reset_game()
        elif guess_result == "incorrect":
            # La lettre est incorrecte, mettre à jour l'affichage des chances restantes
            self.chances_remaining_label.config(text=f"Chances remaining: {self.hangman.chances}")
            if self.hangman.is_game_over():
                self.show_message(f"Sorry, you've lost. The word was '{self.hangman.word}'.")
                self.reset_game()

    def set_word_to_guess(self, word):
        # Mettre à jour le texte du Label word_to_guess
        self.word_to_guess.config(text=f"{' '.join(word)}")

    def make_guess(self):
        # Vérifier si le jeu est terminé
        if not self.hangman.is_game_over():
            # Appeler la méthode guess() de la classe Hangman avec le mot complet
            guess_result = self.hangman.guess(self.hangman.word)
            if guess_result == "correct":
                self.show_message("Congratulations! You've won.")
            else:
                self.show_message(f"Sorry, you've lost. The word was '{self.hangman.word}'.")
            self.reset_game()

    def show_message(self, message):
        # Créez un label pour afficher le message
        message_label = tk.Label(self.root, text=message)
        message_label.pack()
        
    def reset_game(self):
        # Réinitialiser le jeu
        self.hangman.reset_game()
        self.set_word_to_guess(self.hangman.word_guess)
        self.chances_remaining_label.config(text=f"Chances remaining: {self.hangman.chances}")

    def run(self):
        self.root.mainloop()
