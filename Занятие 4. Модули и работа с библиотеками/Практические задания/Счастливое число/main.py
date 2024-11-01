def is_lucky_number(num: int) -> bool:
      # TODO проверить что число шестизначное и положительное
    if len(str(num)) != 6 and num <= 0:
        raise ValueError('Некорректное значение')
     # TODO проверить счастливое число или нет
    else:
        list_digit = [int(nummer) for nummer in str(num) ]
        return sum(list_digit[:3]) == sum(list_digit[3:])

print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
