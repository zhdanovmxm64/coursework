import json
import os

path_to_data = os.path.abspath("../data")
path_to_operations = os.path.join(path_to_data, "operations.json"))

def load_operations():
    """Загружает данные из файла и дабавляет в список все операции клиента """

    with open(path_to_operations, "r", encoding='utf8') as file:
        operations_list = json.load(file)

        return operations_list

def get_last_five_operations(operations_list):
    """Сортировка по дате из 5 последних операций"""

    operations_list_clean = [opr for opr in operations_list if opr != {} and opr["state"] == "EXECUTED"]
    operations_list_clean.sort(key=lambda dictionary: dictionary["date"], reverse=True)
    last_five_operations = operations_list_clean[0:5]

    return last_five_operations