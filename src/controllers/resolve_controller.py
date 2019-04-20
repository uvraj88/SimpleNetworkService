from geocoder_api import GeocoderApi

geocoderApi = GeocoderApi('66G2EC8SONOks4eiqzWv', 'B2I7--7yCJhmzW6w_MuIOQ')

def resolve(lat, long):
    response = geocoderApi.resolve_to_address(lat, long)
    return response
