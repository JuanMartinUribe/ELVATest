from typing import List
from ArcController import ArcController
from GoogleMapsController import GoogleMapsController
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
ADDRESS = "1300 SE Stark Street, Portland, OR 97214"

if __name__ == "__main__":
    gmaps_controller = GoogleMapsController(API_KEY)
    longitude, latitude = gmaps_controller.get_coordinates(ADDRESS)

    arc_controller = ArcController()
    neighborhood = arc_controller.coords_to_neighborhood(longitude, latitude)

    print(
        f"The coordinates for the given address {ADDRESS} are longitude:{longitude} latitude:{latitude}"
    )
    print(
        f"The initial neighborhood for the given coordinates lng:{longitude} lat:{latitude} is {neighborhood}"
    )

    def get_next_neighborhood(init_neighborhood:str, address:str) -> List:
        lng, lat = gmaps_controller.get_coordinates(address)
        neighborhood = arc_controller.coords_to_neighborhood(lng, lat)

        if neighborhood != init_neighborhood:
            return [neighborhood, address]
        else:
            adress_arr = address.split(" ")
            street_number = str(int(adress_arr[0]) + 100)
            nxt_adress = f'{street_number} {" ".join(adress_arr[1:])}'
            return get_next_neighborhood(init_neighborhood, nxt_adress)

    next_neighborhood, next_address = get_next_neighborhood(neighborhood, ADDRESS)
    print(
        f"By incrementing the street number, the first address to be outside {neighborhood} is: {next_address} in the neighborhood: {next_neighborhood}"
    )
