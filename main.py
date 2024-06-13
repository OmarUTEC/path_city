from models import Ciudad
from coordenadas import CoordenadasCSV, CoordenadasAPI, CoordenadasMock
from calculadora_distancia import CalculadoraDistancia

def ciudades_mas_cercanas(ciudad1, ciudad2, ciudad3):
    # Obtener coordenadas de las ciudades
    servicio = CoordenadasAPI()  # Puedes cambiar el servicio aquí
    coord1 = servicio.obtener_coordenadas(ciudad1)
    coord2 = servicio.obtener_coordenadas(ciudad2)
    coord3 = servicio.obtener_coordenadas(ciudad3)

    # Calcular todas las distancias
    distancias = [
        (ciudad1, ciudad2, CalculadoraDistancia.calcular_distancia(coord1, coord2)),
        (ciudad1, ciudad3, CalculadoraDistancia.calcular_distancia(coord1, coord3)),
        (ciudad2, ciudad3, CalculadoraDistancia.calcular_distancia(coord2, coord3))
    ]

    # Encontrar las dos distancias más cortas
    distancias.sort(key=lambda x: x[2])  # Ordenar por distancia
    return distancias[0][:2]

def main():
    ciudad1 = Ciudad("Peru", "Lima")
    ciudad2 = Ciudad("Colombia", "Bogotá")
    ciudad3 = Ciudad("Argentina", "Buenos Aires")

    ciudad_cercana1, ciudad_cercana2 = ciudades_mas_cercanas(ciudad1, ciudad2, ciudad3)

    print(f"Las dos ciudades más cercanas son {ciudad_cercana1.nombre_ciudad}, {ciudad_cercana1.nombre_pais} y {ciudad_cercana2.nombre_ciudad}, {ciudad_cercana2.nombre_pais}")

if __name__ == "__main__":
    main()
