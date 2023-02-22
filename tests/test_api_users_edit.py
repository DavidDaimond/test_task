import pytest

import requests as req
from random import randint

from config import API


@pytest.fixture()
def gen_email():
    name = ''.join([chr(randint(97, 123)) for i in range(8)])
    address = ''.join([chr(randint(97, 123)) for i in range(6)])
    dome = ''.join([chr(randint(97, 123)) for i in range(3)])
    return name + '@' + address + '.' + dome


@pytest.fixture()
def gen_password():
    return ''.join([chr(randint(65, 123)) for i in range(8)])


def test_create_user(gen_email, gen_password):
    resp = req.post(API.methods['CREATE_POST'], params={'email': gen_email, 'password': gen_password})
    assert resp.status_code == 201


@pytest.mark.parametrize("uid,data", ((1, {'name': 'Nuck Figgers', 'job': 'Sticker Collection Senior Engineer'}),
                                      (2, {'name': 'Sick Ducker', 'job': 'Do Nothing Middle Engineer'}),
                                      (3, {'name': 'Steve Jobless'}),
                                      (7, {'job': 'NoName Lang Junior Developer'}),
                                      (92, {'something': 'something'}),
                                      (77, {1254: 555}),
                                      (0, {})
                                      ))
def test_update_put_user(uid, data):
    resp = req.put(API.methods['UPDATE_PUT'] + str(uid), json=data)
    assert resp.status_code == 200


@pytest.mark.parametrize("uid,data", ((1, {'name': 'Nuck Figgers', 'job': 'Sticker Collection Senior Engineer'}),
                                      (2, {'name': 'Sick Ducker', 'job': 'Do Nothing Middle Engineer'}),
                                      (3, {'name': 'Steve Jobless'}),
                                      (7, {'job': 'NoName Lang Junior Developer'}),
                                      (92, {'something': 'something'}),
                                      (77, {1254: 555}),
                                      (0, {})
                                      ))
def test_update_patch_user(uid, data):
    resp = req.patch(API.methods['UPDATE_PATCH'] + str(uid), json=data)
    assert resp.status_code == 200


@pytest.mark.parametrize("uid", [uid for uid in range(1, 15, 2)])
def test_delete_user(uid):
    resp = req.delete(API.methods['DELETE_DELETE'] + str(uid))
    assert resp.status_code == 204


@pytest.mark.parametrize("data,status_code", (
        ({"email": "michael.lawson@reqres.in", "password": "iloveducksick"}, 200),
        ({"email": "lindsay.ferguson@reqres.in", "password": "ship"}, 200),

        ({"email": "tobias.funke@reqres.in", "password": "pass3641ord"}, 200),
        ({"email": "byron.fields@reqres.in", "password": "ilov3sick"}, 200),
        ({"email": "nuck.figgers@reqres.in", "password": "ilonmuskisguy"}, 400),
        ({"email": "d.d.d@reqres.in", "password": "IwannaworkinIBSsomuchpleasehiremeIloveyourcompany"}, 400)
)
                         )
def test_register_user(data, status_code):
    resp = req.post(API.methods['REGISTER_SUCCESSFUL_POST'], json=data)
    assert resp.status_code == status_code
