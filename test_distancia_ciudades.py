import unittest
from models import Ciudad, Coordenada
from coordenadas import CoordenadasMock, CoordenadasAPI, CoordenadasCSV
from calculadora_distancia import CalculadoraDistancia
from main import ciudades_mas_cercanas

class TestDistanciaEntreCiudades(unittest.TestCase):

    def test_distancia_entre_ciudades_mock(self):
        ciudad1 = Ciudad("Mexico", "Mexico City")
        ciudad2 = Ciudad("Japan", "Tokyo")
        ciudad3 = Ciudad("Argentina", "Buenos Aires")

        servicio = CoordenadasMock()
        coord1 = servicio.obtener_coordenadas(ciudad1)
        coord2 = servicio.obtener_coordenadas(ciudad2)
        coord3 = servicio.obtener_coordenadas(ciudad3)

        distancia1 = CalculadoraDistancia.calcular_distancia(coord1, coord2)
        distancia2 = CalculadoraDistancia.calcular_distancia(coord1, coord3)
        distancia3 = CalculadoraDistancia.calcular_distancia(coord2, coord3)

        self.assertAlmostEqual(distancia1, 11274, delta=100)
        self.assertAlmostEqual(distancia2, 7387, delta=100)
        self.assertAlmostEqual(distancia3, 18374, delta=100)

    def test_ciudades_mas_cercanas(self):
        ciudad1 = Ciudad("Mexico", "Mexico City")
        ciudad2 = Ciudad("Japan", "Tokyo")
        ciudad3 = Ciudad("Argentina", "Buenos Aires")

        servicio = CoordenadasMock()
        ciudad_cercana1, ciudad_cercana2 = ciudades_mas_cercanas(ciudad1, ciudad2, ciudad3)

        self.assertIn(ciudad_cercana1, [ciudad1, ciudad2, ciudad3])
        self.assertIn(ciudad_cercana2, [ciudad1, ciudad2, ciudad3])

    def test_ciudad_no_existe(self):
        ciudad1 = Ciudad("Peru", "Lima")
        ciudad2 = Ciudad("Narnia", "Narnia")
        ciudad3 = Ciudad("Argentina", "Buenos Aires")

        servicio = CoordenadasMock()
        coord1 = servicio.obtener_coordenadas(ciudad1)
        coord2 = servicio.obtener_coordenadas(ciudad2)
        coord3 = servicio.obtener_coordenadas(ciudad3)

        self.assertIsNotNone(coord1)
        self.assertIsNone(coord2)
        self.assertIsNotNone(coord3)

    def test_misma_ciudad_dos_veces(self):
        ciudad1 = Ciudad("Peru", "Lima")
        ciudad2 = Ciudad("Peru", "Lima")
        ciudad3 = Ciudad("Argentina", "Buenos Aires")

        servicio = CoordenadasMock()
        coord1 = servicio.obtener_coordenadas(ciudad1)
        coord2 = servicio.obtener_coordenadas(ciudad2)
        coord3 = servicio.obtener_coordenadas(ciudad3)

        distancia1 = CalculadoraDistancia.calcular_distancia(coord1, coord2)
        self.assertEqual(distancia1, 0)

if __name__ == '__main__':
    unittest.main()
