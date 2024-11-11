from idlelib.iomenu import encoding

INPUT_FILE = "input.txt"


OUTPUT_FILE = "output.txt"


def task(count):
    ...  # TODO построчно записать лесенку в файл
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f1:
        for i in range(count):
            str = "*" * (i+1)+"\n"
            f1.write(str)



if __name__ == '__main__':
    # Необходимо для проверки
    task(10)
    with open(OUTPUT_FILE, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
