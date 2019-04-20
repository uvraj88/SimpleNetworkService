import json
import requests
import logging

from here_api import hereApi
from helper import Helper
from error import GeocoderError
from models import GeocoderResponse

class GeocoderApi(hereApi):
    """A python interface into the Here Geocoder API"""

    def __init__(self,
                 app_id=None,
                 app_code=None,
                 timeout=None):
        """Returns a GeocoderApi instance.
        Args:
          app_id (str):
            App Id taken from HERE Developer Portal.
          app_code (str):
            App Code taken from HERE Developer Portal.
          timeout (int):
            Timeout limit for requests.
        """
        super(GeocoderApi, self).__init__(app_id, app_code, timeout)

    def __get(self, data):
        url = Helper.build_url(self._base_url, extra_params=data)
        logging.debug("Fetching Url %s", url)
        response = requests.get(url, timeout=self._timeout)
        try:
            json_data = json.loads(response.content.decode('utf8'))
            logging.debug("Fetched Json Data Dump %s", json_data)
            resolvedAddress = GeocoderResponse(json_data).address()
            logging.info("Resolved Address: %s", resolvedAddress)
            if resolvedAddress != None:
                return resolvedAddress
            else:
                logging.error("Geocode Fetching Failed!")
                return "Here Geocode Fetching Failed!"
        except ValueError as err:
            logging.error("Geocode Fetching Failed, %s", err)
            return "Here Geocode Fetching Failed!"

    def resolve_to_address(self, lat, long):
        """Geocodes given search text with in given boundingbox
        Args:
          lat (float)
          long (float)
        Returns:
          GeocoderResponse instance or Error"""

        data = {'mode': 'retrieveAddresses',
                'prox': "{0},{1}".format(lat,long),
                'app_id': self._app_id,
                'app_code': self._app_code}
        return self.__get(data)
