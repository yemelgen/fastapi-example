#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

import json
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

BASE_URL = '/v1.0/records'

def test_create_record():
    params = { 
        'date': '2023-04-08T14:26:33.009000',
        'name': 'temperature',
        'value': 33
    }
    response = client.post(BASE_URL, json=params)
    pytest.id = response.json()['record']['id']
    assert response.status_code == 200
    assert response.json()['record']['name'] == 'temperature'
    assert response.json()['record']['value'] == 33

def test_get_record():
    response = client.get( f'{BASE_URL}/{pytest.id}' )
    assert response.status_code == 200
    assert response.json()['record']['name'] == 'temperature'
    assert response.json()['record']['value'] == 33


def test_update_record():
    params = { 
        'date': '2023-04-08T14:26:33.009000',
        'name': 'temperature',
        'value': 44
    }
    response = client.put( f'{BASE_URL}/{pytest.id}', json=params )
    assert response.json()['record']['name'] == 'temperature'
    assert response.json()['record']['value'] == 44

def test_delete_record():
    data = { 'detail': 'Record deleted successfully' }
    response = client.delete( f'{BASE_URL}/{pytest.id}')
    assert response.status_code == 200
    assert response.json() == data
