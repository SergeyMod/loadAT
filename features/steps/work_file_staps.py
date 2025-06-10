import json
import os

from behave import then, when

from tests.untils.generate import file_name_
from src.run import Run
from src.event import Event, TypeEvent


@when('Чтение файла')
def read(context):
    file_name = file_name_(context.list_events)
    context.read_list = Run.read_file(file_name)
    os.remove(file_name)

@when('Запись в файл')
def write(context):
    context.file_name = file_name_(context.list_events)
    context.dict_group = Run.group_data(context.list_events)
    Run.write_file(context.file_name, context.dict_group)

@then('Записаный список и считаный из файла идентичны')
def eq_read(context):
    assert context.list_events == context.read_list, 'Списки отличаются'

@then('Тестовый список и считаный из записанного файла идентичны')
def eq_write(context):
    with (open(context.file_name, 'r', encoding='utf8') as f):
        data_in_file = {key: [Event(date=i["date"],
                                    title=i["title"],
                                    type_event=TypeEvent(i["type_event"]),
                                    participants=i["participants"],
                                    place=i["place"]) for i in list_events]
                        for key, list_events in json.load(f).items()}
    os.remove(context.file_name)
    assert context.dict_group == data_in_file