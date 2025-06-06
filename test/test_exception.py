import pytest

from src.run import Run


@pytest.mark.parametrize("get_list_events", [('2025-05-02', '2025-05-02', 1)], indirect=True)
def test_exception(get_list_events, file_name):
    with pytest.raises(ValueError):
        Run.read_file(file_name)
