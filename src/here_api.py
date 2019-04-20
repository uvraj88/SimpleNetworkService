class hereApi(object):
    """ Base class from which all wrappers inherit."""

    def __init__(self,
                 app_id=None,
                 app_code=None,
                 timeout=None):
        """Returns a Api instance.
        Args:
          app_id (str):
            App Id taken from HERE Developer Portal.
          app_code (str):
            App Code taken from HERE Developer Portal.
          timeout (int):
            Timeout limit for requests.
        """

        self.__set_credentials(app_id, app_code)
        self._base_url = 'https://reverse.geocoder.api.here.com/6.2/reversegeocode.json'
        if timeout:
            self._timeout = timeout
        else:
            self._timeout = 20

    def __set_credentials(self,
                          app_id,
                          app_code):
        """Setter for credentials.
        Args:
          app_id (str):
            App Id taken from HERE Developer Portal.
          app_code (str):
            App Code taken from HERE Developer Portal.
        """
        self._app_id = app_id
        self._app_code = app_code
