money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0

all_ = money_capital + salary
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while all_ > spend:
    count += 1
    all_ = all_ - (spend * increase)



print("Количество месяцев, которое можно протянуть без долгов:", count)
