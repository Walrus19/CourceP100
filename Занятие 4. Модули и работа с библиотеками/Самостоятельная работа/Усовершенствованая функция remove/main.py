# TODO написать функцию remove
def remove(list_, value):
    if not value in list_:
        raise ValueError()
    index = list_.index(value)
    return list_[:index] + list_[index+1:]


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]

list__ = [0 , 1 , 2, 3, 7, 5]
# print(remove(list__, 7))
