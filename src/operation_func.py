from _datetime import datetime

class Operation:

    def __init__(self, operation):
        """Cловарь с данными по операции"""
        self.operation = operation

    def __repr__(self):
        """Информация об экземпляре"""
        return f"Class Operation({self.operation})"

    def date(self):
        """Дата операции"""
        operation_date_str = self.operation["date"]
        operation_date = datetime.strptime(operation_date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return operation_date.strftime("%d.%m.%Y")

    def description(self):
        """Описание операции"""
        return self.operation["description"]

    def account_from(self):
        """Данные карты отправления, если они есть"""
        if "from" in self.operation.keys():
            return self.operation["from"]
        else:
            return ""

    def account_to(self):
        """Данные счета назначения"""
        return self.operation["to"]

    def hide_number(self, account):
        if account == "":
            return "Внесение средств"
        else:
            account = account.split(" ")
            account_number = account[-1]
            account.pop(len(account) - 1)
            account_name = " ".join(account)
            if "Счет" in account:
                return f"{account_name} **{account_number[16:20]}"
            else:
                return f"{account_name} {account_number[0:4]} {account_number[4:6]}** **** {account_number[12:16]}"

    def amount(self):
        """Сумма и валюта операции"""
        return f'{self.operation["operationAmount"]["amount"]} {self.operation["operationAmount"]["currency"]["name"]}'