import datetime
import os


list_of_people = []


class Person:
    def __init__(self, name, surname, year, month, day):
        self.name = name
        self.surname = surname
        self.birth = datetime.date(year, month, day)

    def show(self):
        print(f"Imie: {self.name}")
        print(f"Nazwisko: {self.surname}")
        print(f"Data urodzenia: {self.birth}")

    def concat(self):
        person = []
        person.append(self.name)
        person.append(self.surname)
        birth = self.birth
        person.append(birth)
        return person


def main_menu():
    os.system('cls')
    print("Menu")
    print('Press "a" to add item')
    print('Press "d" to delete by name')
    print('Press "i" to delete by id')
    print('Press "q" to quit')


def add_person():
    os.system('cls')
    name = input("Imie: ")
    surname = input('Nazwisko: ')
    day = int(input("Dzień: "))
    month = int(input("Miesiac: "))
    year = int(input("Rok: "))
    new_person = Person(name, surname, year, month, day).concat()
    list_of_people.append(new_person)


def delete_by_name():
    os.system('cls')
    print("Do usunięcia")
    name = input("Imie: ")
    surname = input("Nazwisko: ")
    for j in list_of_people:
        if j[0].lower() == name.lower() and j[1].lower() == surname.lower():
            list_of_people.remove(j)


def delete_by_id():
    print("Do usuniecia po ID: ")
    num = int(input("Numer w liście: "))
    if list_of_people[num-1] in list_of_people:
        list_of_people.remove(list_of_people[num-1])
    else:
        print("nie ma tylu wpisów")


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
        'a': add_person,
        'd': delete_by_name,
        'i': delete_by_id
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