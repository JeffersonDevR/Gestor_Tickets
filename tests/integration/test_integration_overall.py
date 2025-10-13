import unittest
from datetime import datetime
from Modulos.Clientes import Cliente
from Modulos.Reservas import Reservas, gestor_habitaciones
from Modulos.Pagos import PagoEnEfectivo

class TestOverallIntegration(unittest.TestCase):

    def setUp(self):
        # Limpiar datos previos
        Cliente.clientes_registrados.clear()
        gestor_habitaciones.habitaciones.clear()
        # Agregar algunas habitaciones para pruebas
        from Modulos.Habitaciones import Habitacion
        gestor_habitaciones.habitaciones.extend([
            Habitacion("001", "Sencilla", 50.0),
            Habitacion("002", "Doble", 80.0),
            Habitacion("003", "Suite", 150.0),
            Habitacion("004", "Sencilla", 50.0),
            Habitacion("005", "Doble", 80.0)
        ])
        self.reservas = Reservas()

    def test_full_flow_cliente_reserva_pago(self):
        # Prueba de integración: Registrar cliente, hacer reserva, procesar pago
        # 1. Registrar cliente
        cliente = Cliente.registrar_cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        self.assertIsNotNone(cliente)

        # 2. Crear reserva
        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.assertEqual(len(self.reservas.lista_reservas), 1)
        self.assertNotIn("001", gestor_habitaciones.get_habitaciones_disponibles())

        # 3. Procesar pago (asumiendo pago por la reserva)
        pago = PagoEnEfectivo(100.0, datetime.now())
        self.assertTrue(pago.process())
        self.assertEqual(pago.status, "completed")

    def test_multiple_clients_reservations(self):
        # Prueba con múltiples clientes y reservas
        Cliente.registrar_cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        Cliente.registrar_cliente("Maria Lopez", 987654321, "maria@example.com", 3007654321)

        self.reservas.crear_reserva("Juan Perez", "001", "2023-10-01", "10:00")
        self.reservas.crear_reserva("Maria Lopez", "002", "2023-10-02", "11:00")

        self.assertEqual(len(Cliente.clientes_registrados), 2)
        self.assertEqual(len(self.reservas.lista_reservas), 2)
        self.assertNotIn("001", gestor_habitaciones.get_habitaciones_disponibles())
        self.assertNotIn("002", gestor_habitaciones.get_habitaciones_disponibles())

    def test_client_validation_integration(self):
        # Prueba que las reservas y pagos requieren clientes
        # Esto prueba la integración con la lógica de main.py
        from Modulos.Clientes import Cliente

        # Inicialmente no hay clientes
        self.assertEqual(len(Cliente.clientes_registrados), 0)

        # Registrar un cliente
        cliente = Cliente.registrar_cliente("Test User", 111111111, "test@example.com", 3001111111)
        self.assertIsNotNone(cliente)
        self.assertEqual(len(Cliente.clientes_registrados), 1)

        # Ahora las reservas deberían funcionar
        self.reservas.crear_reserva("Test User", "001", "2023-10-01", "10:00")
        self.assertEqual(len(self.reservas.lista_reservas), 1)


if __name__ == '__main__':
    unittest.main()