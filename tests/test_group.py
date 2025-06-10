import pytest

from tests.untils.group import group_identical, is_sorted, group

PARAM = [
    ('2025-05-02', '2025-05-02', 10),
    ('2025-05-02', '2025-05-23', 50),
    ('2025-03-02', '2025-05-23', 550)
]


class TestGroup:
    @pytest.mark.parametrize("get_list_events", PARAM, indirect=True)
    def test_group_is_sorted(self, get_list_events):
        is_sorted(group(get_list_events))

    @pytest.mark.parametrize("get_list_events", PARAM, indirect=True)
    def test_group_identical(self, get_list_events):
        group_identical(get_list_events, group(get_list_events))
