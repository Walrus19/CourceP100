from unicodedata import digit

number = 2342354235235

list_digits = [int(char) for char in str(number)]  # TODO c помощью list comprehension получить список цифр числа

# print(list_digits)

print(sum(list_digits))  # TODO найти сумму цифр числа
print(sum([num for num in list_digits if num % 2 == 0]))  # TODO найти сумму всех четных чисел
print(len(list_digits)) # TODO найти количество цифр
print(min(list_digits))  # TODO найти минимальную цифру
print(list_digits[0] - list_digits[-1])  # TODO найти разность между первой и последней цифрой
