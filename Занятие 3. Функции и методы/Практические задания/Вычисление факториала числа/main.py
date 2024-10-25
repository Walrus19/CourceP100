# TODO Запишите функцию `factorial`
def factorial(number:int) -> int:
    if type(number) is int:
        if number == 0:
                return 1
        else:
            rezult = 1
            for i in range(1,number+1):
                rezult = rezult * i
            return rezult
# TODO Вызовите функцию factorial и распечатайте результат
print(f"Факториал числа 0 равен {factorial(0)}")
print(f"Факториал числа 5 равен {factorial(5)}")
