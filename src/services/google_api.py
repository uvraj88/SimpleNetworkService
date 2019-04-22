import logging
class googleApi(object):
    """Base class for Google Search,
    which is used to fetch address using Google.
    """

    def __init__(self, config, timeout=None):
        """Returns a Api instance.
        Args:
          config (array): Json object to fetch keys.
          timeout (int): Timeout limit for requests.
        """
        self.__set_credentials(config)
        self.__set_timeout(timeout)
        self._base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def __set_credentials(self, config):
        """Setter for credentials.
        Args:
          config (array): Json object to fetch keys.
        """
        self.app_key = config['google'][0]

    def __set_timeout(self, timeout):
        """Setter for timeout.
        Args:
          timeout (int): timeout for rest api.
        """
        self._timeout = timeout if timeout else 20

    def form_params(self, lat, long):
        """Form Url params given lat and long
        Args:
          lat (float): latitude of a location
          long (float): longitude of a location
        """
        data = {'latlng': "{0},{1}".format(lat,long),
                'key': self.app_key}
        return data

    def address(self, json):
        """Gets address from given Json.
        Model is based on service provider response format.
        Args:
          lat (float): latitude of a location
          long (float): longitude of a location
        Returns:
          A human readable address or None.
        """
        if json['results'] != None and len(json['results'])>0:
            self._address = json['results'][0]
            return self._address.get('formatted_address')
        else:
            logging.error("Problem with JSON Response, Json Dump %s, fetched using %s!", json, self._getName())
            self._address = None
            return None

    def _getName(self):
        """Getter for API location provider service.
        """
        return 'GOOGLE'
