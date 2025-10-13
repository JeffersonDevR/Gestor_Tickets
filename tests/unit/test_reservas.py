import unittest
from Modulos.Reservas import Reservas, gestor_habitaciones


class TestReservasIntegration(unittest.TestCase):

    def setUp(self):
        self.reservas = Reservas()
        # Reset gestor habitaciones
        gestor_habitaciones.habitaciones.clear()
        # Add test rooms
        from Modulos.Habitaciones import Habitacion
        gestor_habitaciones.habitaciones.extend([
            Habitacion("001", "Sencilla", 50.0),
            Habitacion("002", "Doble", 80.0),
            Habitacion("003", "Suite", 150.0),
            Habitacion("004", "Sencilla", 50.0),
            Habitacion("005", "Doble", 80.0)
        ])

    def test_crear_reserva_exitosa(self):
        # Test de crear una reserva exitosa
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.assertEqual(len(self.reservas.lista_reservas), 1)
        self.assertEqual(self.reservas.lista_reservas[0]["cliente"], "Juan Perez")
        self.assertNotIn("001", gestor_habitaciones.get_habitaciones_disponibles())

    def test_crear_reserva_habitacion_no_disponible(self):
        # Test de crear reserva en habitacion no disponible
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.crear_reserva("Maria Lopez", "001", "2023-10-02", "11:00")
        self.assertEqual(len(self.reservas.lista_reservas), 1)  # Only one added

    def test_modificar_reserva(self):
        # Test modificar una reserva existente
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.modificar_reserva("Juan Perez", "002", "2023-10-02", "11:00")
        reserva = self.reservas.lista_reservas[0]
        self.assertEqual(reserva["habitacion"], "002")
        self.assertEqual(reserva["fecha"], "2023-10-02")
        self.assertIn("001", gestor_habitaciones.get_habitaciones_disponibles())
        self.assertNotIn("002", gestor_habitaciones.get_habitaciones_disponibles())

    def test_cancelar_reserva(self):
        # Test cancelar una reserva existente
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.cancelar_reserva("Juan Perez")
        self.assertEqual(len(self.reservas.lista_reservas), 0)
        self.assertIn("001", gestor_habitaciones.get_habitaciones_disponibles())

    def test_mostrar_reservas(self):
        # Test mostrar todas las reservas
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.crear_reserva("Maria Lopez", "002", "2023-10-02", "11:00")
        self.assertEqual(len(self.reservas.lista_reservas), 2)

if __name__ == '__main__':
    unittest.main()