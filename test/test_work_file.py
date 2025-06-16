import json
import os

import pytest

from src.event import Event
from src.enum.type_event import TypeEvent
from src.randomEvent import RandomEvent
from src.groupevents import GroupEvents


class TestWorkFile:
    PARAM = [
        ('2025-05-02', '2025-05-02', 10),
        ('2025-05-02', '2025-05-23', 50),
        ('2025-03-02', '2025-05-23', 550)
    ]

    @pytest.mark.parametrize("get_list_events", PARAM, indirect=True)
    def test_read_file(self, file_name, get_list_events):
        assert get_list_events == GroupEvents.read_file(file_name)

    @pytest.mark.parametrize("get_list_events", PARAM, indirect=True)
    def test_write_file(self, get_list_events):
        list_for_write = GroupEvents.group_data(get_list_events)
        file_name = f'{RandomEvent.random_string(10)}.json'
        GroupEvents.write_file(file_name, list_for_write)
        with (open(file_name, 'r', encoding='utf8') as f):
            data_in_file = {key: [Event(date=i["date"],
                                        title=i["title"],
                                        type_event=TypeEvent(i["type_event"]),
                                        participants=i["participants"],
                                        place=i["place"]) for i in list_events]
                            for key, list_events in json.load(f).items()}
        os.remove(file_name)
        assert list_for_write == data_in_file
