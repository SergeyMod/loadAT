import os
import json


from src.randomEvent import RandomEvent


def get_list_events_(start_date, end_date, count):
    return [RandomEvent.random_event([start_date, end_date]) for _ in range(count)]

def file_name_(list_events):
    random_name = f'{RandomEvent.random_string(10)}.json'
    list_events = [i.__dict__ for i in list_events]
    if len(list_events) == 1:
        list_events[0]['type_event'] = 'dsad'
    with open(random_name, "w", encoding='utf8') as f:
        json.dump(list_events, f, indent=2, default=str)
    return random_name