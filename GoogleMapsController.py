import googlemaps
from typing import List


class GoogleMapsController:
    def __init__(self, API_KEY: str) -> None:
        self.gmaps_client = googlemaps.Client(key=API_KEY)

    def get_coordinates(self, adress: str) -> List:
        geocode_result = self.gmaps_client.geocode(adress)
        location = geocode_result = geocode_result[0]["geometry"]["location"]
        longitude, latitude = location["lng"], location["lat"]
        return [longitude, latitude]
