# TODO реализовать функцию
def remove_whitespace(str_wth_more_space):
    words_list = str_wth_more_space.split(" ")
    words_list_without = []
    for word in words_list:
        if word:
            words_list_without.append(word)
    return ' '.join(words_list_without)

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
