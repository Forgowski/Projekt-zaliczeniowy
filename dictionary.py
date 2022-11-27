import random


class Dictionary:
    data_base = []

    def __init__(self):
        with open("dictionary.txt", 'r', encoding="utf-8") as file:
            holder = file.read()
            self.data_base = holder.split(" ")

    def random(self):
        return random.choice(self.data_base)
