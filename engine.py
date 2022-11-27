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
