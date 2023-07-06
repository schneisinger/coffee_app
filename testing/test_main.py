# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-name-in-module

"""Doc string for modules"""
from fastapi.testclient import TestClient
import pytest
from coffee.main import app, coffee_maker, money_machine


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

report_data = {}

@pytest.fixture
def report_from_main():
    report_data = coffee_maker.resources
    return report_data


@pytest.fixture
def test_get_report():
    response = client.get("/coffee_maker/")
    #assert response == report_data
    assert response.status_code == 200


def test_money_report():
    response = client.put("/money_machine/")
    #assert response == f"{money_machine.CURRENCY} {money_machine.profit}"
    assert response.status_code == 200


def test_refill_resources():
    response = client.get("/coffee_maker/")
    #assert response == coffee_maker.resources
    assert response.status_code == 200


def test_brew_product():
    response = client.put("/coffee_maker/{order}")
    assert response.status_code == 200


def test_add_recipe():
    response = client.put("/menu/")
    assert response.status_code == 200


def test_delete_recipe():
    response = client.delete("/menu/{product}")
    assert response.status_code == 200
