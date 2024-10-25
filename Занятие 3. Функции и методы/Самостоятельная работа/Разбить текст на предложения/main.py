# TODO реализовать функцию
def get_sentences_list(str):
    new_str = []
    count = 0
    str1 = str.split(".")
    for i, substr in enumerate(str1):
        if substr:
            new_str.append(substr.strip())
            count += 1
    return new_str


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
