import unittest
from Modulos.Habitaciones import Habitacion, GestorHabitaciones

class TestHabitacionesIntegration(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorHabitaciones()
        # Limpiando habitaciones
        self.gestor.habitaciones.clear()

    def test_agregar_habitacion(self):
        # Test for anadir una habitacion
        habitacion = Habitacion("101", "Sencilla", 50.0)
        self.gestor.habitaciones.append(habitacion)
        self.assertEqual(len(self.gestor.habitaciones), 1)
        self.assertEqual(self.gestor.habitaciones[0].numero, "101")

    def test_mostrar_todas(self):
        # Test mostrar todas las habitaciones
        habitacion1 = Habitacion("101", "Sencilla", 50.0)
        habitacion2 = Habitacion("102", "Doble", 80.0)
        self.gestor.habitaciones.extend([habitacion1, habitacion2])
        # Mostrar la lista completa
        self.assertEqual(len(self.gestor.habitaciones), 2)

    def test_cambiar_estado_valido(self):
        # Test de cambio de estado de una habitacion
        habitacion = Habitacion("101", "Sencilla", 50.0)
        habitacion.cambiar_estado("ocupada")
        self.assertEqual(habitacion.estado, "ocupada")

    def test_cambiar_estado_invalido(self):
        # Test de cambiar a un estado invalido
        habitacion = Habitacion("101", "Sencilla", 50.0)
        habitacion.cambiar_estado("invalid")
        self.assertEqual(habitacion.estado, "disponible")  

    def test_buscar_por_estado(self):
        # Test de bsucar por estado
        hab1 = Habitacion("101", "Sencilla", 50.0)
        hab1.estado = "ocupada"
        hab2 = Habitacion("102", "Doble", 80.0)
        hab2.estado = "disponible"
        self.gestor.habitaciones.extend([hab1, hab2])
        ocupadas = [h for h in self.gestor.habitaciones if h.estado == "ocupada"]
        self.assertEqual(len(ocupadas), 1)

    def test_buscar_por_tipo(self):
        # Test de buscar por tipo
        hab1 = Habitacion("101", "Sencilla", 50.0)
        hab2 = Habitacion("102", "Doble", 80.0)
        self.gestor.habitaciones.extend([hab1, hab2])
        sencillas = [h for h in self.gestor.habitaciones if h.tipo.lower() == "sencilla"]
        self.assertEqual(len(sencillas), 1)

    def test_ordenar_por_tarifa(self):
        # Test de organizar por tarifa
        hab1 = Habitacion("101", "Sencilla", 50.0)
        hab2 = Habitacion("102", "Doble", 80.0)
        hab3 = Habitacion("103", "Suite", 120.0)
        self.gestor.habitaciones.extend([hab3, hab1, hab2])
        ordenadas = sorted(self.gestor.habitaciones, key=lambda x: x.tarifa)
        self.assertEqual(ordenadas[0].tarifa, 50.0)
        self.assertEqual(ordenadas[2].tarifa, 120.0)

    def test_get_habitaciones_disponibles(self):
        # Test de obtener habitaciones disponibles
        hab1 = Habitacion("101", "Sencilla", 50.0)
        hab2 = Habitacion("102", "Doble", 80.0)
        hab2.estado = "ocupada"
        self.gestor.habitaciones.extend([hab1, hab2])
        disponibles = self.gestor.get_habitaciones_disponibles()
        self.assertIn("101", disponibles)
        self.assertNotIn("102", disponibles)

    def test_ocupar_habitacion(self):
        # Test de ocupar una habitacion
        hab = Habitacion("101", "Sencilla", 50.0)
        self.gestor.habitaciones.append(hab)
        result = self.gestor.ocupar_habitacion("101")
        self.assertTrue(result)
        self.assertEqual(hab.estado, "ocupada")

    def test_liberar_habitacion(self):
        # Test de liberar una habitacion
        hab = Habitacion("101", "Sencilla", 50.0)
        hab.estado = "ocupada"
        self.gestor.habitaciones.append(hab)
        result = self.gestor.liberar_habitacion("101")
        self.assertTrue(result)
        self.assertEqual(hab.estado, "disponible")

if __name__ == '__main__':
    unittest.main()