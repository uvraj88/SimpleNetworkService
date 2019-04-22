class GeocoderResponse():
    """Http Response builder for a particular API implementation"""

    def __init__(self, api, json_content):
        self.json_content = json_content
        self.api = api

    def address(self):
        """Gets address using Json.
        Returns:
          Returns a resolved address which is formatted.
        """
        return self.api.address(self.json_content)
