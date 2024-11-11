import json


FILENAME = "input.json"


def task() -> int:
    with open(FILENAME, encoding="utf-8") as f:
        python_obj = json.load(f)
      # TODO Десериализуйте содержимое JSON файла
    # print(python_obj)
      # TODO Просуммируйте все значения по ключу contains_improvement_appeals
    sum = 0
    for i in python_obj:
        sum = sum + i['contains_improvement_appeals']
    return sum

if __name__ == '__main__':
    print(task())
