"""Tests for app.py using Flask's built-in test client."""

import pytest
from app import app


@pytest.fixture
def client():
    # A "fixture" sets up something tests need. Here: a fake browser.
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ---------- /hello tests ----------
def test_hello_default(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_hello_with_name(client):
    response = client.get("/hello?name=Alex")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Alex!"}


# ---------- /sum tests ----------
def test_sum_valid(client):
    response = client.post("/sum", json={"numbers": [1, 2, 3]})
    assert response.status_code == 200
    assert response.get_json() == {"sum": 6}


def test_sum_floats(client):
    response = client.post("/sum", json={"numbers": [1.5, 2.5]})
    assert response.status_code == 200
    assert response.get_json() == {"sum": 4.0}


def test_sum_missing_field(client):
    response = client.post("/sum", json={"wrong_key": [1, 2]})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_sum_no_json_body(client):
    response = client.post("/sum", data="not json")
    assert response.status_code == 400


def test_sum_not_a_list(client):
    response = client.post("/sum", json={"numbers": "123"})
    assert response.status_code == 400


def test_sum_non_numeric_items(client):
    response = client.post("/sum", json={"numbers": [1, "two", 3]})
    assert response.status_code == 400


def test_sum_empty_list(client):
    response = client.post("/sum", json={"numbers": []})
    assert response.status_code == 400