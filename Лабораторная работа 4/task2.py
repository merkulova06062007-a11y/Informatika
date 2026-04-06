import json

filename = "input.json"

def task() -> float:
    with open(filename, encoding="utf-8") as f:
        json_data = json.load(f)

    sum_values = sum(item["score"] * item["weight"] for item in json_data)
    return round(sum_values, 3)

if __name__ == '__main__':
    print(task())
