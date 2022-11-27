from engine import Engine


while True:
    print("1. Nowa gra")
    print("2. Zasady gry")
    print("3. Koniec")
    while True:
        answer = int(input("\n"))
        if answer == 1:
            game = Engine()
            break
        elif answer == 2:
            print("Tekstowa gra, w której komputer (Host) losuje słowo, które jest izogramem (izogram jest to wyraz\n\
w którym nie powtarzają się żadne litery) i informuje użytkownika (Guesser) o ilości liter\n\
w słowie. Użytkownik (Guesser) stara się zgadnąć co to za słowo Komputer (Host) po każdej próbie\n\
zwraca liczbe Cows & Bulls. Liczba przy słowie Cows oznacza literę występującą w słwoie lecz na złej\n\
pozycji, liczba przy słowie Bulls oznacza poprawną literę na poprawnej pozycji. Gra kończy się kiedy\n\
liczba przy Bulls bęzie taka sama jak długość słowa wylosowanego przez komputer.")
            break
        elif answer == 3:
            exit(0)
        else:
            print("wpisz poprawną liczbe")
