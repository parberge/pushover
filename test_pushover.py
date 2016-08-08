#!/usr/bin/env python3

import pytest

@pytest.fixture
def pushover():
    import pushover
    return pushover

def test_pushover_exception(pushover):
    with pytest.raises(pushover.PushoverError):
        pushover.Pushover()

def test_pushover_token(pushover):
    # According to https://pushover.net/api the token should be 30 chars long
    my_test_token = "A" * 30
    pushover_obj = pushover.Pushover(my_test_token)
    assert(len(pushover_obj.token) == 30)
