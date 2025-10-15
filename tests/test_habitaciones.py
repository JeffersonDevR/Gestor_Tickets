import unittest
from Modulos.Habitaciones import GestorHabitaciones, Habitacion

class TestHabitaciones(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba para tener un gestor limpio.
        self.gestor = GestorHabitaciones()

    def test_agregar_habitacion_exitosa(self):
        # Probamos que se puede agregar una habitación nueva.
        self.gestor.agregar_habitacion("301", "Sencilla", 120.0)
        self.assertEqual(len(self.gestor.habitaciones), 1)
        self.assertEqual(self.gestor.habitaciones[0].numero, "301")

    def test_agregar_habitacion_duplicada(self):
        # Probamos que no se puede agregar una habitación con un número ya existente.
        self.gestor.agregar_habitacion("302", "Doble", 220.0)
        self.gestor.agregar_habitacion("302", "Suite", 450.0)  # Intentamos agregar otra con el mismo número.
        self.assertEqual(len(self.gestor.habitaciones), 1)

    def test_cambiar_estado_habitacion(self):
        # Probamos que el estado de una habitación se puede cambiar correctamente.
        self.gestor.agregar_habitacion("303", "Sencilla", 130.0)
        habitacion = self.gestor.habitaciones[0]
        habitacion.cambiar_estado("ocupada")
        self.assertEqual(habitacion.estado, "ocupada")

    def test_buscar_por_estado(self):
        # Probamos la búsqueda de habitaciones por estado.
        self.gestor.agregar_habitacion("401", "Sencilla", 150.0)
        self.gestor.agregar_habitacion("402", "Doble", 250.0)
        self.gestor.habitaciones[1].cambiar_estado("ocupada")
        disponibles = self.gestor.buscar_por_estado("disponible")
        ocupadas = self.gestor.buscar_por_estado("ocupada")
        self.assertEqual(len(disponibles), 1)
        self.assertEqual(disponibles[0].numero, "401")
        self.assertEqual(len(ocupadas), 1)
        self.assertEqual(ocupadas[0].numero, "402")

    def test_ordenar_por_tarifa(self):
        # Probamos que las habitaciones se ordenan correctamente por su tarifa.
        self.gestor.agregar_habitacion("501", "Suite", 500.0)
        self.gestor.agregar_habitacion("502", "Sencilla", 150.0)
        self.gestor.agregar_habitacion("503", "Doble", 250.0)
        ordenadas = self.gestor.ordenar_por_tarifa()
        self.assertEqual(ordenadas[0].tarifa, 150.0)
        self.assertEqual(ordenadas[1].tarifa, 250.0)
        self.assertEqual(ordenadas[2].tarifa, 500.0)

if __name__ == '__main__':
    unittest.main()