import json
import logging
import requests

from services.here_api import hereApi
from services.google_api import googleApi
from services.bing_api import bingApi
from helper import Helper
from models import GeocoderResponse

class SNSApi():
    """A python interface into the Here Geocoder API"""

    def __init__(self):
        """Returns a SNSApi instance.
        """
        self.hereApi = hereApi()
        self.googleApi = googleApi()
        self.bingApi = bingApi()

    def __get(self, lat, long):
        data = self.currentProvider.form_params(lat, long)
        url = Helper.build_url(self.currentProvider._base_url, extra_params=data)
        logging.debug("Fetching Url %s", url)
        response = requests.get(url, timeout=self.currentProvider._timeout)
        logging.debug("HTTP Request response %s", response.status_code)

        if (response.status_code != 200):
            #retry logic here.
            logging.error("Problem reaching API provider, Error %s!", response.status_code)
            return None

        try:
            json_data = json.loads(response.content.decode('utf8'))
            logging.debug("Received Response Dump %s", json_data)

            resolvedAddress = GeocoderResponse(self.currentProvider, json_data).address()
            logging.info("Resolved Address: %s", resolvedAddress)

            if resolvedAddress != None:
                return resolvedAddress
            else:
                logging.error("Geocode Fetching Failed!")
                return None
        except ValueError as err:
            logging.error("Geocode Fetching Failed, %s", err)
            return None


    def resolve_to_address(self, lat, long):
        """Geocodes given search text with in given boundingbox
        Args:
          lat (float)
          long (float)
        Returns:
          GeocoderResponse instance or Error"""
        self.currentProvider = self.hereApi

        response = self.__get(lat, long)

        if (response == None):
            #retry with google.
            self.currentProvider = self.googleApi
            response = self.__get(lat, long)
            return response if response != None else "Geocode Fetching Failed!"
        else:
            return response
