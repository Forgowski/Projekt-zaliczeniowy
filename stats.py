class Stats:
    def __init__(self):
        self.cows = 0
        self.bulls = 0
        self.lives = 10

    def addCows(self):
        self.cows += 1

    def addBulls(self):
        self.bulls += 1

    def clearCows(self):
        self.cows = 0

    def clearBulls(self):
        self.bulls = 0

    def showStats(self):
        print(f"bulls: {self.bulls} cows: {self.cows}")