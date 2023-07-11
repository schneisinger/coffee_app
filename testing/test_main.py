# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-name-in-module

"""Doc string for modules"""
from fastapi.testclient import TestClient
import pytest
from coffee.main import app, coffee_maker


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


@pytest.fixture
def test_get_report():
    response = client.get("/coffee_maker/")
    assert response.status_code == 200


def test_money_report():
    response = client.get("/money_machine/")
    assert response.status_code == 200


def test_refill_resources():
    response = client.put(
        "/coffee_maker/",
        json = {"coffee": 100, "water": 100, "milk": 100,}
        )
    assert response.status_code == 200


def test_brew_product():
    response = client.put(
        "/coffee_maker/brew_espresso/",
        data = "brew_espresso",
        )
    assert response.status_code == 200


def test_add_recipe():
    response = client.put(
        "/menu/",
        json = {"name": "weird", "water": 50, "milk": 15, "coffee": 36, "price": 1.5}
        )
    assert response.status_code == 200


def test_delete_recipe():
    response = client.delete("/menu/delete_espresso/")
    assert response.status_code == 200
