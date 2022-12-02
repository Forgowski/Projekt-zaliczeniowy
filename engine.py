from stats import Stats
from dictionary import Dictionary
from validator import Validator


class Engine:
    word = ""
    mistakes = 0
    lives = 0

    def __init__(self, difficulty_lvl=10):
        self.lives = difficulty_lvl
        self.dic = Dictionary()
        self.word = self.dic.random()
        self.stats = Stats()
        self.validator = Validator()
        self.game()

    def game(self):
        print(f"długość wylsowanego słowa to: {self.dic.len_of_chosen_word}")
        while self.lives > 0:
            while True:
                player_try = input("\npodaj słowo: ")
                if self.validator.validWord(player_try, self.dic.len_of_chosen_word):
                    break
                else:
                    print("słowo musi być izogramem i posiadać odpowiednią długość")

            self.compare(player_try)
            if self.stats.bulls == self.dic.len_of_chosen_word:
                print("gratulacje to prawidłowe słowo")
                break
            else:
                self.stats.showStats()
                self.lives -= 1
                if self.lives == 0:
                    print("Koniec żyć spróbuj jeszcze raz!")
                else:
                    print(f"Pozostało {self.lives} żyć")

    def compare(self, player_try):
        self.stats.clearBulls()
        self.stats.clearCows()
        for i in range(self.dic.len_of_chosen_word):
            if player_try[i] in self.word:
                if player_try[i] == self.word[i]:
                    self.stats.addBulls()
                else:
                    self.stats.addCows()
