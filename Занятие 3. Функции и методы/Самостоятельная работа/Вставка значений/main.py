# TODO реализовать функцию
def insert(list_, value, index=0):
    new_list = list_[:index] + [value] + list_[index:]
    return new_list


print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]
