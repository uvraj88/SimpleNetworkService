#!/usr/bin/python
# coding: utf8
import json
import requests
import requests_mock

from src.services.here_api import hereApi
from src.services.google_api import googleApi
from src.sns_api import SNSApi
from src.helper import Helper

location = 'Vancouver International Airport (YVR), 3211 Grant McConachie Way, Richmond, BC V7B 0A4, Canada'
lat = 49.196712
long = -123.1902671

snsApi = SNSApi()
hereApi = hereApi()
googleApi = googleApi()

def test_snsApi():
    data = hereApi.form_params(lat, long)
    hereurl = Helper.build_url(hereApi._base_url, extra_params=data)

    data_file = 'results/hereError.json'
    with requests_mock.Mocker(real_http=True) as mocker, open(data_file, 'r') as input:
        mocker.register_uri('GET', hereurl, text=input.read())
        response = snsApi.resolve_to_address(lat, long)
        assert response == 'Vancouver International Airport (YVR), 3211 Grant McConachie Way, Richmond, BC V7B 0A4, Canada'

def test_snsApi_hereFailure_404():
    data = hereApi.form_params(lat, long)
    hereurl = Helper.build_url(hereApi._base_url, extra_params=data)

    with requests_mock.Mocker(real_http=True) as mocker:
        mocker.register_uri('GET', hereurl, text='Not Found', status_code=404)
        response = snsApi.resolve_to_address(lat, long)
        assert response == 'Vancouver International Airport (YVR), 3211 Grant McConachie Way, Richmond, BC V7B 0A4, Canada'

def test_snsApi_googleFailure():
    heredata = hereApi.form_params(lat, long)
    hereurl = Helper.build_url(hereApi._base_url, extra_params=heredata)

    googledata = googleApi.form_params(lat, long)
    googleurl = Helper.build_url(googleApi._base_url, extra_params=googledata)

    data_file = 'results/googleError.json'
    with requests_mock.Mocker(real_http=True) as mocker, open(data_file, 'r') as input:
        mocker.register_uri('GET', hereurl, text='Not Found', status_code=404)
        mocker.register_uri('GET', googleurl, text=input.read())
        response = snsApi.resolve_to_address(lat, long)
        assert response == 'Geocode Fetching Failed!'

def test_snsApi_googleFailure_404():
    heredata = hereApi.form_params(lat, long)
    hereurl = Helper.build_url(hereApi._base_url, extra_params=heredata)

    googledata = googleApi.form_params(lat, long)
    googleurl = Helper.build_url(googleApi._base_url, extra_params=googledata)

    with requests_mock.Mocker(real_http=True) as mocker:
        mocker.register_uri('GET', hereurl, text='Not Found', status_code=404)
        mocker.register_uri('GET', googleurl, text='Not Found', status_code=404)
        response = snsApi.resolve_to_address(lat, long)
        assert response == 'Geocode Fetching Failed!'
