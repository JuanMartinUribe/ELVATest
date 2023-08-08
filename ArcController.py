from typing import List
from shapely.geometry import Point, Polygon
import requests


class ArcController:
    def __init__(self, url) -> None:
        self.data = requests.get(url).json().get("features")

    def coords_to_neighborhood(self, longitude: int, latitude: int) -> str:
        for neighborhood in self.data:
            try:
                coords = neighborhood.get("geometry").get("coordinates")[0]
            except ValueError as e:
                print("This feature coordinates array is not parsed properly", e)
                continue
            polygon_vertices = [tuple(coord) for coord in coords]
            point_coords = (longitude, latitude)
            is_inside_polygon = ArcController._is_point_inside_polygon(
                polygon_vertices, point_coords
            )
            if is_inside_polygon:
                return neighborhood.get("properties").get("NAME")
        return ""

    @staticmethod
    def _is_point_inside_polygon(vortices: List, point_coords: List) -> bool:
        polygon = Polygon(vortices)
        point = Point(point_coords)
        return point.within(polygon)
