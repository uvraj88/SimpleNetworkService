import json
import logging
import requests

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

from services.here_api import hereApi
from services.google_api import googleApi
from services.bing_api import bingApi
from helper import Helper
from model import GeocoderResponse

class SNSApi():
    """A python Class which provides API's to fetch address
    using multiple provider interfaces."""

    def __init__(self):
        """Returns a SNSApi instance.
        """
        self.hereApi = hereApi(config)
        self.googleApi = googleApi(config)
        self.bingApi = bingApi(config)

    def __get(self, lat, long):
        """Getter for an an address based provider implementation.
        Args:
          lat (float): latitude of a location
          long (float): longitude of a location
        Returns:
          A human readable address or None.
        """
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
        """function to implement address getter and retry logic.
        Args:
          lat (float)
          long (float)
        Returns:
          A human readable address or Error"""

        # try initially with HERE API.
        self.currentProvider = self.hereApi
        response = self.__get(lat, long)

        if (response == None):
            #retry with google.
            self.currentProvider = self.googleApi
            response = self.__get(lat, long)
            #we can try further with bing, we can update later based on need.
            return response if response != None else "Geocode Fetching Failed!"
        else:
            return response
