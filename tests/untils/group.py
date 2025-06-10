from datetime import datetime

from src.run import Run, TypeEvent


def group(list_events):
    return Run.group_data(list_events)


def is_sorted(group_events):
    for key in group_events.keys():
        for first_el, next_el in zip(group_events.get(key),
                                     group_events.get(key)[1:]):
            assert datetime.fromisoformat(
                first_el.date) <= datetime.fromisoformat(next_el.date)


def group_identical(list_events, group_events):
    identical_date = {i.date[:10] for i in list_events if
                      i.type_event != TypeEvent.OTHER}
    assert len(identical_date) == len({*group_events.keys()})