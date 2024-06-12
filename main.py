from models import Ciudad
from coordenadas import CoordenadasAPI
from calculadora_distancia import CalculadoraDistancia

def main():
    ciudad1 = Ciudad("Perú", "Lima")
    ciudad2 = Ciudad("Argentina", "Buenos Aires")
    ciudad3 = Ciudad("Uruguay", "Montevideo")

    ciudades = [ciudad1, ciudad2, ciudad3]

    servicio_api = CoordenadasAPI()
    coordenadas = []
    for ciudad in ciudades:
        coord = servicio_api.obtener_coordenadas(ciudad)
        if coord:
            coordenadas.append(coord)
        else:
            print(f"No se pudieron obtener las coordenadas para {ciudad.nombre_ciudad}, {ciudad.nombre_pais}")

    if len(coordenadas) < 2:
        print("No se pudieron obtener las coordenadas para al menos dos ciudades.")
        return

    distancias = []
    for i in range(len(coordenadas)):
        for j in range(i+1, len(coordenadas)):
            distancia = CalculadoraDistancia.calcular_distancia(coordenadas[i], coordenadas[j])
            distancias.append((distancia, ciudades[i], ciudades[j]))

    distancias.sort(key=lambda x: x[0])
    ciudad1, ciudad2 = distancias[0][1].nombre_ciudad, distancias[0][2].nombre_ciudad
    pais1, pais2 = distancias[0][1].nombre_pais, distancias[0][2].nombre_pais
    print(f"Las ciudades más cercanas son {ciudad1} ({pais1}) y {ciudad2} ({pais2})")

if __name__ == "__main__":
    main()