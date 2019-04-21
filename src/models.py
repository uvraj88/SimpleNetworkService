class GeocoderResponse():
    def __init__(self, api, json_content):
        self.json_content = json_content
        self.api = api

    def address(self):
        return self.api.address(self.json_content)
