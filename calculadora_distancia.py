import math
from models import Coordenada

class CalculadoraDistancia:
    @staticmethod
    def calcular_distancia(coord1, coord2):
        radio_tierra = 6371.0  # Radio de la tierra en kilómetros

        dlat = math.radians(coord2.latitud - coord1.latitud)
        dlon = math.radians(coord2.longitud - coord1.longitud)

        a = (math.sin(dlat / 2) ** 2 +
             math.cos(math.radians(coord1.latitud)) * math.cos(math.radians(coord2.latitud)) *
             math.sin(dlon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return radio_tierra * c
