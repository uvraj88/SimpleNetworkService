import logging

class bingApi(object):
    """ Base class from which all wrappers inherit."""

    def __init__(self,
                 app_key=None,
                 timeout=None):
        """Returns a Api instance.
        Args:
          app_key (str):
            App key taken from baidu Developer Portal.
          timeout (int):
            Timeout limit for requests.
        """

        self.__set_credentials(app_key)
        self.__set_timeout(timeout)
        self._base_url = 'http://dev.virtualearth.net/REST/v1/Locations/'

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
            self.app_key = "AsGsYbid40e6fmCJ3-cpuscPsMKMBI7Rua_IinzIgt1Tod4Nm_zX7QKcRmA3_sgr"

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

        data = {'': "{0},{1}".format(lat,long),
                'key': self.app_key}
        return data

    def address(self, json):
        if json['Response'] != None and json['Response']['View'] != None and len(json['Response']['View'])>0:
            location = json['Response']['View'][0]['Result'][0]['Location']
            self._address = location.get('Address')
            return self._address.get('Label')
        else:
            logging.error("Problem with JSON Response, Json Dump %s, fetched using %s!", json, self._getName())
            self._address = None
            return None

    def _getName(self):
            return 'BING'
