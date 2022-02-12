from flask import json, jsonify
from app import app


def test_get_users():
    response = app.test_client().get('/api/London/50/')
    data = json.loads(response.data.decode())

    assert response.content_type, "application/json"
    assert response.status_code == 200
    assert data["success"] is True


def test_get_users_required_data():
    response = app.test_client().get('/api/London/50/')
    data = json.loads(response.data.decode())
    test_email = "mboam3q@thetimes.co.uk"
    test_first_name = "Mechelle"

    assert test_email in data["data"][0]["email"]
    assert test_first_name in data["data"][0]["first_name"]
    assert data["success"] is True


def test_get_users_no_result():
    response = app.test_client().get('/api/Never/1/')
    data = json.loads(response.data.decode())

    assert response.content_type, "application/json"
    assert response.status_code == 200
    assert data[0]["success"] is True


def test_get_users_no_distance():
    response = app.test_client().get('/api/London//')

    assert response.content_type, "application/json"
    assert response.status_code == 404


def test_get_users_no_city():
    response = app.test_client().get('/api//50/')

    assert response.content_type, "application/json"
    assert response.status_code == 404

