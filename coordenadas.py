import csv
import requests
from models import Coordenada

class CoordenadasCSV:
    def obtener_coordenadas(self, ciudad):
        with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['city'].lower() == ciudad.nombre_ciudad.lower() and row['country'].lower() == ciudad.nombre_pais.lower():
                    return Coordenada(float(row['lat']), float(row['lng']))
        return None

class CoordenadasAPI:
    def obtener_coordenadas(self, ciudad):
        url = f"https://nominatim.openstreetmap.org/search?q={ciudad.nombre_ciudad},{ciudad.nombre_pais}&format=json"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                lat = float(data[0]['lat'])
                lon = float(data[0]['lon'])
                return Coordenada(lat, lon)
        return None

class CoordenadasMock:
    def obtener_coordenadas(self, ciudad):
        # Devuelve coordenadas fijas
        return Coordenada(-12.0464, -77.0428)
