# TODO Напишите функцию `calculate_parking_load`
def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    if (occupied_parking_spaces <= total_parking_spaces and
            occupied_parking_spaces > 0 and total_parking_spaces > 0 and
            type(total_parking_spaces) is int and type(occupied_parking_spaces) is int):
            rezult = occupied_parking_spaces / total_parking_spaces * 100
            return rezult

total_parking = 1000
occupied_parking = 300
# print(type(total_parking))
# print(type(occupied_parking))
rez = calculate_parking_load(total_parking, occupied_parking)
print(rez)
