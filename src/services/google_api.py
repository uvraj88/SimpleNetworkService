import logging

class googleApi(object):
    """ Base class from which all wrappers inherit."""

    def __init__(self,
                 app_key=None,
                 timeout=None):
        """Returns a Api instance.
        Args:
          app_key (str):
            App key taken from Google Developer Portal.
          timeout (int):
            Timeout limit for requests.
        """

        self.__set_credentials(app_key)
        self.__set_timeout(timeout)
        self._base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def __set_credentials(self,
                          app_key):
        """Setter for credentials.
        Args:
          app_key (str):
            App key taken from HERE Developer Portal.
        """
        if app_key:
            self.app_key = app_key
        else:
            self.app_key = "AIzaSyDQGsu3Bm63atl0hGBarg0H2i0Z6mlo9mY"

    def __set_timeout(self,
                          timeout):
        if timeout:
            self._timeout = timeout
        else:
            self._timeout = 20

    def form_params(self, lat, long):
        """Geocodes given search text with in given boundingbox
        Args:
          lat (float)
          long (float)
        """

        data = {'latlng': "{0},{1}".format(lat,long),
                'key': self.app_key}
        return data

    def address(self, json):
        if json['results'] != None and len(json['results'])>0:
            self._address = json['results'][0]
            return self._address.get('formatted_address')
        else:
            logging.error("Problem with JSON Response, Json Dump %s, fetched using %s!", json, self._getName())
            self._address = None
            return None

    def _getName(self):
            return 'GOOGLE'
