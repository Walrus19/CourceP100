list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию
max_value_index = 0
max_value = list_numbers[max_value_index]
for i, list_number in enumerate(list_numbers):
     if max_value <= list_number:
         max_value = list_number
         max_value_index = i
list_numbers[max_value_index], list_numbers[len(list_numbers)-1] = list_numbers[len(list_numbers)-1], list_numbers[max_value_index]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
