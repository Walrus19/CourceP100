INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r') as f_src:
        with open(OUTPUT_FILE, "w") as f_dst:
            for line in f_src:
                f_dst.write(line.upper())
    ...  # TODO перезаписать содержимое одного файла в другой
    f_src.close()
    f_dst.close()

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as file:
        for current_line in file:
            print(current_line, end="")
