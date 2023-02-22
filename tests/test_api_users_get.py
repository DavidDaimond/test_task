import pytest

import requests as req

from config import API


@pytest.mark.parametrize("uid,code", [(1, 200),
                                      (2, 200),
                                      (4, 200),
                                      (12, 200),
                                      (13, 404),
                                      (15, 404)
                                      ])
def test_get_single_user(uid, code):
    resp = req.get(API.methods['SINGLE_USER_GET'] + str(uid))
    assert resp.status_code == code


@pytest.mark.parametrize("uid", [uid for uid in range(1, 13)])  # this going to check first 12 defined users
def test_check_user_defined_data_single(uid):
    resp = req.get(API.methods['SINGLE_USER_GET'] + str(uid))
    assert resp.json()['data'] == API.users_list[uid - 1]


@pytest.mark.parametrize("page", (pg for pg in range(0, 3)))
def test_get_list_users(page):
    resp = req.get(API.methods['LIST_USERS_GET'], params={'page': page})
    assert resp.status_code == 200


@pytest.mark.parametrize("delay", (dl for dl in range(0, 3)))
def test_get_list_users_delay(delay):
    resp = req.get(API.methods['DELAYED_RESPONSE_GET'], params={'delay': delay})
    assert resp.status_code == 200
