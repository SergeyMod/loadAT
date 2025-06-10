import os

import pytest

from untils.generate import get_list_events_, file_name_


@pytest.fixture(scope='session')
def get_list_events(request):
    return get_list_events_(*request.param)


@pytest.fixture()
def file_name(request):
    random_name = file_name_(request.getfixturevalue('get_list_events'))
    yield random_name
    os.remove(random_name)
