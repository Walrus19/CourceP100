# TODO Распечатать таблицу умножения
size = 9
for i in range(2, size + 1):
    for j in range(2, size + 1):
        end = " " if j != size else ""
        result = i * j
        print(f"{result:2}", end=end)
    print()