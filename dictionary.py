class Dictionary:
    data_base = []

    def __init__(self):
        with open("dictionary.txt", 'r', encoding="utf-8") as file:
            holder = file.read()
            data_base = holder.split(" ")
            print(data_base)

Dictionary()
