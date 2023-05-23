from src.operation_func import Operation
import pytest as pytest


@pytest.fixture
def class_fixture_1():
    operation_test_1 = Operation({'date': '2000-12-08T22:46:21.935582',
                                  'operationAmount': {'amount': '41096.24',
                                                      'currency': {'name': 'USD', 'code': 'USD'}},
                                  'description': 'Открытие вклада',
                                  'to': 'Счет 90424923579946435907'})
    return operation_test_1


@pytest.fixture
def class_fixture_2():
    operation_test_2 = Operation({'date': '2001-11-19T09:22:25.899614',
                                  'operationAmount': {'amount': '30153.72',
                                                      'currency': {'name': 'руб.', 'code': 'RUB'}},
                                  'description': 'Перевод организации',
                                  'from': 'Maestro 7810846596785568',
                                  'to': 'MasterCard 6783917276771847'})
    return operation_test_2


def test___repr__(class_fixture_1):
    assert class_fixture_1.__repr__() == "Class Operation({'date': '2000-12-08T22:46:21.935582', " \
                                         "'operationAmount': {'amount': '41096.24', " \
                                         "'currency': {'name': 'USD', 'code': 'USD'}}, " \
                                         "'description': 'Открытие вклада', " \
                                         "'to': 'Счет 90424923579946435907'})"


def test_date(class_fixture_1):
    assert class_fixture_1.date() == "08.12.2000"


def test_description(class_fixture_1):
    assert class_fixture_1.description() == "Открытие вклада"


