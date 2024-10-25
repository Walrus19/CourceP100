ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
      # TODO проверить что в строку входят только символы 1 и 0
    rez = False
    for letter in str_:
        if letter == '0' or letter == '1':
            rez = True
        else:
            rez = False
    return(rez)

print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
