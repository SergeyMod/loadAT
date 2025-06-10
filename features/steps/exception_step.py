import os

from behave import given, when, then

from src.run import Run
from tests.untils.generate import file_name_

@given('Подставляем данные для генерации рандомных данных вызывающих исключение')
def param(context):
    context.param = ('2025-05-02', '2025-05-02', 1)

@when('Чтение файла с данными для выброса исключения')
def exception(context):
    file_name = file_name_(context.list_events)
    try:
        Run.read_file(file_name)
    except ValueError as e:
        context.exception = e
    else:
        context.exception = None
    os.remove(file_name)

@then('Выброшено исключние ValueError')
def check_exception(context):
    assert context.exception is not None, "Исключение не было выброшено"
    assert isinstance(context.exception, ValueError)
