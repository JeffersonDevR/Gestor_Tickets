import unittest
from datetime import datetime
from Modulos.Clientes import Cliente
from Modulos.Reservas import Reservas, habitaciones_disponibles
from Modulos.Pagos import PagoEnEfectivo

class TestOverallIntegration(unittest.TestCase):

    def setUp(self):
        # Reset all global states
        Cliente.clientes_registrados.clear()
        habitaciones_disponibles[:] = ["001", "002", "003", "004", "005"]
        self.reservas = Reservas()

    def test_full_flow_cliente_reserva_pago(self):
        # Integration test: Register client, make reservation, process payment
        # 1. Register client
        cliente = Cliente.registrar_cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        self.assertIsNotNone(cliente)

        # 2. Create reservation
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.assertEqual(len(self.reservas.lista_reservas), 1)
        self.assertNotIn("001", habitaciones_disponibles)

        # 3. Process payment (assuming payment for the reservation)
        pago = PagoEnEfectivo(100.0, datetime.now())
        self.assertTrue(pago.process())
        self.assertEqual(pago.status, "completed")

    def test_multiple_clients_reservations(self):
        # Test multiple clients and reservations
        Cliente.registrar_cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        Cliente.registrar_cliente("Maria Lopez", 987654321, "maria@example.com", 3007654321)

        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.crear_reserva("Maria Lopez", "002", "2023-10-02", "11:00")

        self.assertEqual(len(Cliente.clientes_registrados), 2)
        self.assertEqual(len(self.reservas.lista_reservas), 2)
        self.assertNotIn("001", habitaciones_disponibles)
        self.assertNotIn("002", habitaciones_disponibles)

if __name__ == '__main__':
    unittest.main()