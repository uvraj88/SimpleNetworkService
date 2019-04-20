import json
import logging

class GeocoderResponse():
    def __init__(self, json_content):
        responseView = json_content['Response']['View']
        if json_content['Response'] != None and json_content['Response']['View'] != None and len(json_content['Response']['View'])>0:
            location = json_content['Response']['View'][0]['Result'][0]['Location']
            self._address = location.get('Address')
        else:
            logging.error("Problem with JSON Response, Json Dump %s!", json_content)
            self._address = None

    def address(self):
        if self._address!= None:
            return self._address.get('Label')
        else:
            logging.error("Problem with Response, cant parse response data properly.!")
            return None
