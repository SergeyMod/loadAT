from datetime import datetime

import pytest

from src.groupevents import GroupEvents
from src.enum.type_event import TypeEvent

PARAM = [
    ('2025-05-02', '2025-05-02', 10),
    ('2025-05-02', '2025-05-23', 50),
    ('2025-03-02', '2025-05-23', 550)
]


class TestGroupEvents:
    @pytest.mark.parametrize("get_list_events", PARAM, indirect=True)
    def test_group_is_sorted(self, get_list_events):
        result_list = GroupEvents.group_data(get_list_events)
        GroupEvents.sorted_(result_list)
        for key in result_list.keys():
            for first_el, next_el in zip(result_list.get(key),
                                         result_list.get(key)[1:]):
                assert datetime.fromisoformat(
                    first_el.date) <= datetime.fromisoformat(next_el.date)

    @pytest.mark.parametrize("get_list_events", PARAM, indirect=True)
    def test_group_identical(self, get_list_events):
        identical_date = {i.date[:10] for i in get_list_events}
        result_list = GroupEvents.group_data(get_list_events)
        # не разобрался как тут можно прикрутить sorted или не так понял
        # добавил проверку на значения
        assert identical_date == set(result_list)
        assert len(identical_date) == len({*result_list.keys()})

    @pytest.mark.parametrize("get_list_events", PARAM, indirect=True)
    def test_group_filter(self, get_list_events):
        assert len(list(filter(lambda x: x.type_event != TypeEvent.OTHER,
                               get_list_events))) == len(
            GroupEvents.filter_(get_list_events))
