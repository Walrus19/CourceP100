import json
from idlelib.iomenu import encoding

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
      # TODO Десериализуйте содержимое файла из переменной INPUT_FILE
    with open(INPUT_FILE, encoding="utf-8") as input_f:
        python_obj = json.load(input_f)
      # TODO Сериализуйте содержимое в файл из переменной INPUT_FILE
    with open(OUTPUT_FILE, "w", encoding="utf-8") as output_f:
        json.dump(python_obj, output_f, ensure_ascii=False, indent = 4)
if __name__ == '__main__':
    # Нужно для проверки задания
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
