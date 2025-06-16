import os
import json
import tempfile

import pytest

from src.randomEvent import RandomEvent


@pytest.fixture(scope='session')
def get_list_events(request):
    start_date, end_date, count = request.param
    return [RandomEvent.random_event([start_date, end_date]) for _ in range(count)]


@pytest.fixture()
def file_name(request):
    with tempfile.TemporaryDirectory() as temp_dir:
        random_name = os.path.join(temp_dir, f'{RandomEvent.random_string(10)}.json')
        list_events = request.getfixturevalue('get_list_events')
        list_events = [i.__dict__ for i in list_events]
        if len(list_events) == 1:
            list_events[0]['type_event'] = 'dsad'
        with open(random_name, "w", encoding='utf8') as f:
            json.dump(list_events, f, indent=2, default=str)
        yield random_name
