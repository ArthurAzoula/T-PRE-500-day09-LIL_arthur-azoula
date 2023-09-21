import tkinter as tk
from hangman import Hangman
from constants.constant import SCREEN_WIDTH, SCREEN_HEIGHT, ALPHABET
from PIL import Image, ImageTk

class Gui:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Hangman GUI')
        self.root.config(bg='green')

        # Jeu
        self.hangman = Hangman()

        # Créez un cadre pour les éléments de l'interface
        frame = tk.Frame(self.root, bg='green', padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        # Label pour le nombre de chances
        self.chances_remaining_label = tk.Label(frame, text=f"Chances remaining: {self.hangman.chances}", font=('Roboto', 16), fg='white', bg='green')
        self.chances_remaining_label.grid(row=0, column=0, columnspan=4)

        # Label pour le mot partiellement deviné
        self.word_to_guess = tk.Label(frame, text=f"{' '.join(self.hangman.word_guess)}", font=('Roboto', 24), fg='white', bg='green')
        self.word_to_guess.grid(row=1, column=0, columnspan=4)

        # Créez un cadre pour les boutons de l'alphabet
        alphabet_frame = tk.Frame(frame, bg='green')
        alphabet_frame.grid(row=2, column=0, columnspan=4)

        # Créez les boutons pour l'alphabet
        self.alphabet_buttons = []
        for i, letter in enumerate(ALPHABET):
            button = tk.Button(alphabet_frame, text=letter.upper(), command=lambda l=letter: self.guess_letter(l), font=('Roboto', 16), width=3, height=1, bg='brown', fg='white')
            self.alphabet_buttons.append(button)
            row = i // 8
            column = i % 8
            button.grid(row=row, column=column, padx=5, pady=5)

        # Label pour le message de fin de partie
        self.end_message = tk.Label(frame, font=('Roboto', 18), fg='white', bg='green')
        self.end_message.grid(row=3, column=0, columnspan=4)

    def guess_letter(self, letter):
        # Appeler la méthode guess() de la classe Hangman avec la lettre cliquée
        guess_result = self.hangman.guess(letter)

        if guess_result == "correct":
            # La lettre est correcte, mettre à jour l'affichage du mot partiellement deviné
            self.set_word_to_guess(self.hangman.word_guess)
            if '_' not in self.hangman.word_guess:
                self.show_message("Congratulations! You've won.", foreground='green')
                self.hangman.reset_game()
                self.set_word_to_guess(self.hangman.word_guess)
        elif guess_result == "incorrect":
            # La lettre est incorrecte, mettre à jour l'affichage des chances restantes
            self.chances_remaining_label.config(text=f"Chances remaining: {self.hangman.chances}")
            if self.hangman.is_game_over():
                self.show_message(f"Sorry, you've lost. The word was '{self.hangman.word}'.", foreground='red')
                self.hangman.reset_game()
                self.set_word_to_guess(self.hangman.word_guess)

    def set_word_to_guess(self, word):
        # Mettre à jour le texte du Label word_to_guess
        self.word_to_guess.config(text=f"{' '.join(word)}")

    def make_guess(self):
        # Vérifier si le jeu est terminé
        if not self.hangman.is_game_over():
            # Appeler la méthode guess() de la classe Hangman avec le mot complet
            guess_result = self.hangman.guess(self.hangman.word)
            if guess_result == "correct":
                self.show_message("Congratulations! You've won.", foreground='green')
            else:
                self.show_message(f"Sorry, you've lost. The word was '{self.hangman.word}'.", foreground='red')
            self.hangman.reset_game()
            self.set_word_to_guess(self.hangman.word_guess)

    def show_message(self, message, foreground='white'):
        # Mettre à jour le texte du Label end_message
        self.end_message.config(text=message, foreground=foreground)

    def run(self):
        self.root.mainloop()