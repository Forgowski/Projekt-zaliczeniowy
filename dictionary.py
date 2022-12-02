import random


class Dictionary:
    data_base = []
    len_of_chosen_word = 0

    def __init__(self):
        try:
            with open("dictionary.txt", 'r', encoding="utf-8") as file:
                holder = file.read()
                self.data_base = holder.split(" ")
        except FileNotFoundError:
            print("nie znaleziono pliku")

    def random(self):
        chosen_word = random.choice(self.data_base)
        self.len_of_chosen_word = len(chosen_word)
        return chosen_word
