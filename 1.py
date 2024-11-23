# TODO решите задачу
import json

def task() -> float:
    filename = "input.json"
    with open(filename, "r") as file:
        json_data = json.load(file)
    sum = 0
    for object in json_data:
        sum += (object["score"] * object["weight"])
    return round(sum, 3)


print(task())
