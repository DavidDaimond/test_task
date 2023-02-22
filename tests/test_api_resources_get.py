import pytest

import requests as req

from config import API


@pytest.mark.parametrize("rid,code", [(1, 200),
                                      (2, 200),
                                      (4, 200),
                                      (12, 200),
                                      (13, 404),
                                      (15, 404)
                                      ])
def test_get_single_resource(rid, code):
    resp = req.get(API.methods['SINGLE_RESOURCE_GET'] + str(rid))
    assert resp.status_code == code


@pytest.mark.parametrize("rid", [rid for rid in range(1, 13)])  # this going to check first 12 defined resources
def test_check_resource_defined_data_single(rid):
    resp = req.get(API.methods['SINGLE_RESOURCE_GET'] + str(rid))
    assert resp.json()['data'] == API.resources_list[rid - 1]


@pytest.mark.parametrize("page", (pg for pg in range(0, 3)))
def test_get_list_resources(page):
    resp = req.get(API.methods['LIST_RESOURCE_GET'], params={'page': page})
    assert resp.status_code == 200


