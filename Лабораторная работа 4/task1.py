import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:  # Считываем содержимое CSV файла
        reader = csv.DictReader(csv_file)   # Создаем reader для CSV
        data = list(reader)  # Преобразуем в список словарей

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:  # Сериализуем в JSON с отступами 4
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
