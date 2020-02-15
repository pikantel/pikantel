import os


tab = []


def add_item():
    if len(tab) < 10:
        x = int(input("Dodaj liczbę: "))
        tab.append(x)
    else:
        print("Za dużo danych w liście")


def get_last():
     print(tab.pop())


def how_many():
     print(len(tab))


def main_menu():
    os.system('cls')
    print("Menu")
    print('Press "a" to add item')
    print('Press "p" to pop item')
    print('Press "i" to count items in list')


def show_error(value):
    os.system('cls')
    if value == 0:
        print("value_error")
        input()
    else:
        print("error")
        input()


def function_selector(klucz):
    switcher = {
        'a': add_item,
        'p': get_last,
        'i': how_many
    }
    return switcher.get(klucz, lambda: show_error(0))


if __name__ == '__main__':
    while 1:
        main_menu()
        x = input()
        if x == 'q':
            os.system('cls')
            break
        func = function_selector(x)
        func()
