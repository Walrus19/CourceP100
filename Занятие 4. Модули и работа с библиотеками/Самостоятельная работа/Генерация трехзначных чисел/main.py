# TODO написать функцию, которая выдает трехзначное число
from random import choice
def games_apparat():
    list_ = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return int(str(choice(list_)) + str(choice(list_)) + str(choice(list_)))

print(games_apparat())