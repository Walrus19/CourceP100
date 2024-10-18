numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_none = numbers.index(None)
average = round((sum(numbers[0:index_none])+sum(numbers[index_none+1:])) / len(numbers), 2)
a = index_none

numbers[4] = average
print("Измененный список:", numbers)
