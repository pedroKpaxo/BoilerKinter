

import json

from sqlalchemy import Column, Integer, String
from shapely.geometry import Polygon


class BaseModel(object):
    """Bse class for all models"""
    id = Column(Integer, primary_key=True)

    def dict_list(self):
        return [(k, v) for k, v in self.__dict__.items()]


class GeometricObject(BaseModel):
    """Base class for geometric objects"""

    GEOMETRIA = Column(String, nullable=False)

    @property
    def load_geometry(self) -> list[float, float]:
        """Returns the loaded list of cords from the string"""
        return json.loads(self.GEOMETRIA)

    @property
    def as_polygon(self) -> Polygon:
        P = Polygon(self.load_geometry)
        SP = [t[::-1] for t in P.exterior.coords]
        return Polygon(SP)

    @property
    def area(self):
        return self.as_polygon.area

    @property
    def centroid(self):
        x, y = self.as_polygon.centroid.xy
        return (x[0], y[0])

    @property
    def invert_geometry(self):
        return [t[::-1] for t in self.as_polygon.exterior.coords]
