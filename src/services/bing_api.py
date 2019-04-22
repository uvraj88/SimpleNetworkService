import logging
class bingApi(object):
    """Base class for Bing Search,
    which is used to fetch address using Bing.
    """

    def __init__(self, config, timeout=None):
        """Returns a Api instance.
        Args:
          config (array): Json object to fetch keys.
          timeout (int): Timeout limit for requests.
        """
        self.__set_credentials(config)
        self.__set_timeout(timeout)
        self._base_url = 'http://dev.virtualearth.net/REST/v1/Locations/'

    def __set_credentials(self, config):
        """Setter for credentials.
        Args:
          config (array): Json object to fetch keys.
        """
        self.app_key = config['bing'][0]

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
        data = {'': "{0},{1}".format(lat,long),
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
        if json['resourceSets'] != None and len(json['resourceSets'])>0 and json['resourceSets'][0]['estimatedTotal']>=1:
            self._address = json['resourceSets'][0]['resources'][0]['address']
            return self._address.get('formattedAddress')
        else:
            logging.error("Problem with JSON Response, Json Dump %s, fetched using %s!", json, self._getName())
            self._address = None
            return None

    def _getName(self):
        """Getter for API location provider service.
        """
        return 'BING'
