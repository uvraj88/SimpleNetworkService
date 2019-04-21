from sns_api import SNSApi
snsApi = SNSApi()
def resolve(lat, long):
    """Resolve Rest endpoint to resolve latlng to an address"""
    response = snsApi.resolve_to_address(lat, long)
    return response
