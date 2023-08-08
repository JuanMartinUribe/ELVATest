import googlemaps
from typing import List


class GoogleMapsController:
    def __init__(self, API_KEY: str) -> None:
        self.gmaps_client = googlemaps.Client(key=API_KEY)

    def get_coordinates(self, address: str) -> List:
        geocode_result = self.gmaps_client.geocode(address)
        location = geocode_result = geocode_result[0].get("geometry").get("location")
        longitude, latitude = location.get("lng"), location.get("lat")
        return [longitude, latitude]
