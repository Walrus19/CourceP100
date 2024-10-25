# TODO Напишите функцию `is_palindrome`
def is_palindrome(stroka):

    rezult = ''.join(stroka.lower().split())
    return rezult == rezult[::-1]


is_palindrome("Кит на море не романтик")

