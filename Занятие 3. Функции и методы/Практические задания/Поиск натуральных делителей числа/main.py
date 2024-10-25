def get_list_number_divisors(number):
      # TODO Найдите список делителей числа number
    a=[]
    for i in range(1,number+1):
        if number % i == 0:
            a.append(i)
    return a
print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
