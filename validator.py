from collections import Counter


class Validator:
    def validWord(self, word):
        if type(word) != str:
            print("niepoprawne słowo")
            return 0
        else:
            if self.checkStr(word):
                return 1

    def checkStr(self, word):
        dic = Counter(word)
        for k, v in dic.items():
            if v > 1:
                return 0
        return 1


