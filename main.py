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

    def get_next_neighborhood(init_neighborhood, address):
        lng, lat = gmaps_controller.get_coordinates(address)
        neighborhood = arc_controller.coords_to_neighborhood(lng, lat)

        if neighborhood != init_neighborhood:
            return neighborhood
        else:
            adress_arr = address.split(" ")
            street_number = str(int(adress_arr[0]) + 100)
            nxt_adress = f'{street_number} {" ".join(adress_arr[1:])}'
            return get_next_neighborhood(init_neighborhood, nxt_adress)

    next_neighborhood = get_next_neighborhood(neighborhood, ADDRESS)
    print(next_neighborhood)
