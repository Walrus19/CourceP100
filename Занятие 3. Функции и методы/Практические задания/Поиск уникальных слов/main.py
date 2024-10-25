# TODO реализовать функцию
def get_unique_words(words):
    rezult = list(set(words.split()))
    rezult.sort()
    return rezult


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
