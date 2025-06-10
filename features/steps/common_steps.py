import os

from behave import given

from tests.untils.generate import get_list_events_, file_name_

@given('Даны данные для генерации рандомных данных')
def param(context):
    context.param = ('2025-05-02', '2025-05-02', 10)

@given('Дан список рандомных данных')
def get_list_events(context):
    context.list_events = get_list_events_(*context.param)

@given('Генерируем рандомные имя файла')
def file_name(context):
    random_name = file_name_(context.list_events)
    return random_name