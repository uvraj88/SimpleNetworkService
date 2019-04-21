from sns_api import SNSApi

snsApi = SNSApi()

def resolve(lat, long):
    response = snsApi.resolve_to_address(lat, long)
    return response
