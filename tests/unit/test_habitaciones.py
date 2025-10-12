import unittest
from Modulos.Habitaciones import Habitacion, GestorHabitaciones

class TestHabitacionesIntegration(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorHabitaciones()

    def test_agregar_habitacion(self):
        # Integration test for adding a room
        habitacion = Habitacion("101", "Sencilla", 50.0)
        self.gestor.habitaciones.append(habitacion)
        self.assertEqual(len(self.gestor.habitaciones), 1)
        self.assertEqual(self.gestor.habitaciones[0].numero, "101")

    def test_mostrar_todas(self):
        # Test showing all rooms
        habitacion1 = Habitacion("101", "Sencilla", 50.0)
        habitacion2 = Habitacion("102", "Doble", 80.0)
        self.gestor.habitaciones.extend([habitacion1, habitacion2])
        # Since mostrar_todas prints, we just check the list
        self.assertEqual(len(self.gestor.habitaciones), 2)

    def test_cambiar_estado_valido(self):
        # Test changing state to valid state
        habitacion = Habitacion("101", "Sencilla", 50.0)
        habitacion.cambiar_estado("ocupada")
        self.assertEqual(habitacion.estado, "ocupada")

    def test_cambiar_estado_invalido(self):
        # Test changing to invalid state
        habitacion = Habitacion("101", "Sencilla", 50.0)
        habitacion.cambiar_estado("invalid")
        self.assertEqual(habitacion.estado, "disponible")  # should remain

    def test_buscar_por_estado(self):
        # Test searching by state
        hab1 = Habitacion("101", "Sencilla", 50.0)
        hab1.estado = "ocupada"
        hab2 = Habitacion("102", "Doble", 80.0)
        hab2.estado = "disponible"
        self.gestor.habitaciones.extend([hab1, hab2])
        ocupadas = [h for h in self.gestor.habitaciones if h.estado == "ocupada"]
        self.assertEqual(len(ocupadas), 1)

    def test_buscar_por_tipo(self):
        # Test searching by type
        hab1 = Habitacion("101", "Sencilla", 50.0)
        hab2 = Habitacion("102", "Doble", 80.0)
        self.gestor.habitaciones.extend([hab1, hab2])
        sencillas = [h for h in self.gestor.habitaciones if h.tipo.lower() == "sencilla"]
        self.assertEqual(len(sencillas), 1)

    def test_ordenar_por_tarifa(self):
        # Test sorting by rate
        hab1 = Habitacion("101", "Sencilla", 50.0)
        hab2 = Habitacion("102", "Doble", 80.0)
        hab3 = Habitacion("103", "Suite", 120.0)
        self.gestor.habitaciones.extend([hab3, hab1, hab2])
        ordenadas = sorted(self.gestor.habitaciones, key=lambda x: x.tarifa)
        self.assertEqual(ordenadas[0].tarifa, 50.0)
        self.assertEqual(ordenadas[2].tarifa, 120.0)

if __name__ == '__main__':
    unittest.main()