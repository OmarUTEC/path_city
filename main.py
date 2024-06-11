from models import Ciudad
from coordenadas import CoordenadasCSV, CoordenadasAPI, CoordenadasMock
from calculadora_distancia import CalculadoraDistancia

def main():
    ciudad1 = Ciudad("Peru", "Lima")
    ciudad2 = Ciudad("Chile", "Santiago")

    # Para CoordenadasAPI
    servicio_api = CoordenadasAPI()
    coord1_api = servicio_api.obtener_coordenadas(ciudad1)
    coord2_api = servicio_api.obtener_coordenadas(ciudad2)

    # Para CoordenadasCSV
    servicio_csv = CoordenadasCSV()
    coord1_csv = servicio_csv.obtener_coordenadas(ciudad1)
    coord2_csv = servicio_csv.obtener_coordenadas(ciudad2)

    if coord1_api and coord2_api:
        distancia_api = CalculadoraDistancia.calcular_distancia(coord1_api, coord2_api)
        print(f"La distancia entre {ciudad1.nombre_ciudad} y {ciudad2.nombre_ciudad} (API) es: {distancia_api:.2f} km")
    else:
        print("No se pudieron obtener las coordenadas de una o ambas ciudades (API).")

    if coord1_csv and coord2_csv:
        distancia_csv = CalculadoraDistancia.calcular_distancia(coord1_csv, coord2_csv)
        print(f"La distancia entre {ciudad1.nombre_ciudad} y {ciudad2.nombre_ciudad} (CSV) es: {distancia_csv:.2f} km")
    else:
        print("No se pudieron obtener las coordenadas de una o ambas ciudades (CSV).")

if __name__ == "__main__":
    main()
