import unittest
from Modulos.Reservas import Reservas, habitaciones_disponibles


class TestReservasIntegration(unittest.TestCase):

    def setUp(self):
        self.reservas = Reservas()
        # Reset global list
        habitaciones_disponibles[:] = ["001", "002", "003", "004", "005"]

    def test_crear_reserva_exitosa(self):
        # Integration test for creating a reservation
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.assertEqual(len(self.reservas.lista_reservas), 1)
        self.assertEqual(self.reservas.lista_reservas[0]["cliente"], "Juan Perez")
        self.assertNotIn("001", habitaciones_disponibles)

    def test_crear_reserva_habitacion_no_disponible(self):
        # Test creating reservation for unavailable room
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.crear_reserva("Maria Lopez", "001", "2023-10-02", "11:00")
        self.assertEqual(len(self.reservas.lista_reservas), 1)  # Only one added

    def test_modificar_reserva(self):
        # Test modifying a reservation
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.modificar_reserva("Juan Perez", "002", "2023-10-02", "11:00")
        reserva = self.reservas.lista_reservas[0]
        self.assertEqual(reserva["habitacion"], "002")
        self.assertEqual(reserva["fecha"], "2023-10-02")
        self.assertIn("001", habitaciones_disponibles)
        self.assertNotIn("002", habitaciones_disponibles)

    def test_cancelar_reserva(self):
        # Test canceling a reservation
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.cancelar_reserva("Juan Perez")
        self.assertEqual(len(self.reservas.lista_reservas), 0)
        self.assertIn("001", habitaciones_disponibles)

    def test_mostrar_reservas(self):
        # Test showing reservations
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.crear_reserva("Maria Lopez", "002", "2023-10-02", "11:00")
        self.assertEqual(len(self.reservas.lista_reservas), 2)

if __name__ == '__main__':
    unittest.main()