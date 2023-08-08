from typing import List
from shapely.geometry import Point, Polygon
from dotenv import load_dotenv
import os
import requests


class ArcController:
    def __init__(self) -> None:
        load_dotenv()
        self.url = os.getenv("ARC_URL")
        self.data = requests.get(self.url).json()

    def coords_to_neighborhood(self, longitude: int, latitude: int) -> str:
        features = self.data.get("features")
        for feature in features:
            try:
                coords = feature.get("geometry").get("coordinates")[0]
            except ValueError as e:
                print('This feature coordinates array is not parsed properly',e)
                continue
            polygon_vertices = [tuple(coord) for coord in coords]
            point_coords = (longitude, latitude)
            is_inside_polygon = ArcController._is_point_inside_polygon(
                polygon_vertices, point_coords
            )
            if is_inside_polygon:
                return feature.get("properties").get("NAME")
        return ""

    @staticmethod
    def _is_point_inside_polygon(vertices: List, point_coords: List) -> bool:
        polygon = Polygon(vertices)
        point = Point(point_coords)
        return point.within(polygon)
