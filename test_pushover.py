#!/usr/bin/env python3
import pytest
import re

# The app and user token must only contain valid chars: I.e [a-zA-Z0-9_]
# and be 30 chars in length
pushover_token_pattern = re.compile('^\w{30}$')

@pytest.fixture
def pushover():
    import pushover
    return pushover

@pytest.fixture
def pushover_obj(pushover):
    """
    Sets up the pushover obj for testing
    """

    test_app_token = "A" * 30
    test_user_token = "B" * 30
    test_device_name = "Test_device_name"
    pushover_obj = pushover.Pushover(test_app_token)
    pushover_obj.user(
            user_token=test_user_token,
            user_device=test_device_name,
            )

    return pushover_obj

def test_pushover_exception(pushover):
    with pytest.raises(pushover.PushoverError):
        # Should raise exception about no app token supplied
        pushover.Pushover()

def test_pushover_app_token(pushover_obj):
    assert(pushover_token_pattern.match(pushover_obj.token))

def test_pushover_user_token(pushover_obj):
    assert(pushover_token_pattern.match(pushover_obj.user_token))

def test_pushover_device_name(pushover_obj):
    # The device name must only contain valid chars: I.e [a-zA-Z0-9_]
    assert(re.match('^\w{1,25}$', pushover_obj.user_device))
