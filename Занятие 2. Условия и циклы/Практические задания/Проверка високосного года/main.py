year = 2012

if int(year) % 4 == 0 and (int(year) % 100 !=0 or int(year) % 400 == 0):  # TODO Напишите условие проверки високосного года
    print(year, "является високосным годом.")
else:
    print(year, "не является високосным годом.")
