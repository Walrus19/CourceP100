import json


FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME, encoding="utf-8") as f:
        python_obj = json.load(f)
      # TODO считать содержимое JSON файла

      # TODO найти максимальный элемент по ключу score
    return max(python_obj, key = lambda item: item["score"])

if __name__ == '__main__':
    print(task())
