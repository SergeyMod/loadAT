import pytest

from src.groupevents import GroupEvents


@pytest.mark.parametrize("get_list_events", [('2025-05-02', '2025-05-02', 1)], indirect=True)
def test_exception(get_list_events, file_name):
    with pytest.raises(ValueError):
        GroupEvents.read_file(file_name)
