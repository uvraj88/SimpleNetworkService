import logging
class hereApi(object):
    """Base class for HERE Search,
    which is used to fetch address using HERE.
    """

    def __init__(self, config, timeout=None):
        """Returns a Api instance.
        Args:
          config (array): Json object to fetch keys.
          timeout (int): Timeout limit for requests.
        """
        self.__set_credentials(config)
        self.__set_timeout(timeout)
        self._base_url = 'https://reverse.geocoder.api.here.com/6.2/reversegeocode.json'

    def __set_credentials(self, config):
        """Setter for credentials.
        Args:
          config (array): Json object to fetch keys.
        """
        self._app_id = config['here'][0]
        self._app_code = config['here'][1]

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
        Returns:
          A human readable address or None.
        """
        data = {'mode': 'retrieveAddresses',
                'prox': "{0},{1}".format(lat,long),
                'app_id': self._app_id,
                'app_code': self._app_code}
        return data

    def address(self, json):
        """Gets address from given Json.
        Model is based on service provider response format.
        Args:
          lat (float): latitude of a location
          long (float): longitude of a location
        """
        if json['Response'] != None and json['Response']['View'] != None and len(json['Response']['View'])>0:
            location = json['Response']['View'][0]['Result'][0]['Location']
            self._address = location.get('Address')
            return self._address.get('Label')
        else:
            logging.error("Problem with JSON Response, Json Dump %s, fetched using %s!", json, self._getName())
            self._address = None
            return None

    def _getName(self):
        """Getter for API location provider service.
        """
        return 'HERE'
