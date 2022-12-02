from collections import Counter


class Validator:
    def validWord(self, word, word_len):
        if len(word) != word_len:
            return 0
        elif self.checkStr(word):
            return 1
        else:
            return 0

    def checkStr(self, word):
        dic = Counter(word)
        for k, v in dic.items():
            if v > 1:
                return 0
        return 1


