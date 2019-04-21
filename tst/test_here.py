#!/usr/bin/python
# coding: utf8
import json
import requests
import requests_mock

from src.services.here_api import hereApi
from src.sns_api import SNSApi
from src.helper import Helper

location = 'Grant McConachie Way, Richmond, BC V7B, Canada'
lat = 49.196712
long = -123.1902671

snsApi = SNSApi()
hereApi = hereApi()

def test_snsApi():
    response = snsApi.resolve_to_address(lat, long)
    assert response == 'Grant McConachie Way, Richmond, BC V7B, Canada'

def test_hereApi():
    data = hereApi.form_params(lat, long)
    url = Helper.build_url(hereApi._base_url, extra_params=data)

    data_file = 'results/hereMock.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        response = requests.get(url, timeout=hereApi._timeout)

    assert response.status_code == 200
