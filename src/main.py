from src.utils import load_operations, get_last_five_operations
from src.operation_func import Operation

# Список всех операций клиента
operations_list = load_operations()

# Создаем список из 5 последних успешных операций
last_five_operations = get_last_five_operations(operations_list)

# Перебираем список и выводим данные
for element in last_five_operations:
    operation = Operation(element)
    print(f"""\n{operation.date()} {operation.description()}
{operation.hide_number(operation.account_from())} -> {operation.hide_number(operation.account_to())}
{operation.amount()}""")