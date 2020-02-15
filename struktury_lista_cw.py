import random
import time
import os

new_list = []

def gen_lcg(c):
    b = int(time.time()*1000000)
    counter = 0
    while 1:
        x = (1002 * b + c) % 1001
        counter += 1
        b = x
        if counter == 10:
            time.sleep(0.001)
            b = int(time.time()*1000000)
            counter = 0
        yield x


def next_number():
    gen = gen_lcg(563)
    return next(gen)


def main_menu():
    os.system('cls')
    print("Menu")
    print('Press "a" to add item')
    print('Press "q" to quit')
    print('Press "p" to print list')


def delete_selected():
    pass


def add_to_list():
    os.system('cls')
    n = next_number()
    new_list.append(n)
    print(f"{n} dodany do listy")
    input()


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
        'a': add_to_list
    }
    return switcher.get(klucz, lambda: show_error(0))


if __name__ == '__main__':
    gen = gen_lcg(613)
    for x in range(100):
        new_list.append(next(gen))

    while 1:
        main_menu()
        x = input()
        if x == 'q':
            os.system('cls')
            break
        if x == 'p':
            os.system('cls')
            print(new_list)
        func = function_selector(x)
        func()


