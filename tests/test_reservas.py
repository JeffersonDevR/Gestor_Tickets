import unittest
from datetime import datetime
from Modulos.Clientes import Cliente
from Modulos.Habitaciones import GestorHabitaciones
from Modulos.Reservas import GestorReservas

class TestReservas(unittest.TestCase):

    def setUp(self):
        # Configuramos un entorno limpio para cada prueba.
        Cliente.clientes_registrados = []
        self.cliente = Cliente.registrar_cliente("Test User", 98765432, "test.user@email.com", "555-9876")
        self.gestor_habitaciones = GestorHabitaciones()
        self.gestor_habitaciones.agregar_habitacion("201", "Suite", 480.0)
        self.gestor_reservas = GestorReservas(self.gestor_habitaciones)

    def test_crear_reserva_exitosa(self):
        # Probamos que se puede crear una reserva de forma exitosa.
        fecha_inicio = datetime(2024, 10, 1)
        fecha_fin = datetime(2024, 10, 5)
        reserva = self.gestor_reservas.crear_reserva(self.cliente, "201", fecha_inicio, fecha_fin)
        self.assertIsNotNone(reserva)
        self.assertEqual(len(self.gestor_reservas.reservas), 1)
        self.assertEqual(reserva.habitacion.estado, "ocupada")
        self.assertIn(reserva, self.cliente.historial_de_reservas)

    def test_crear_reserva_habitacion_no_disponible(self):
        # Probamos que no se puede crear una reserva para una habitación que no está disponible.
        self.gestor_habitaciones.habitaciones[0].cambiar_estado("ocupada")
        fecha_inicio = datetime(2024, 11, 1)
        fecha_fin = datetime(2024, 11, 5)
        reserva = self.gestor_reservas.crear_reserva(self.cliente, "201", fecha_inicio, fecha_fin)
        self.assertIsNone(reserva)
        self.assertEqual(len(self.gestor_reservas.reservas), 0)

    def test_cancelar_reserva(self):
        # Probamos que una reserva puede ser cancelada correctamente.
        fecha_inicio = datetime(2024, 12, 1)
        fecha_fin = datetime(2024, 12, 5)
        reserva = self.gestor_reservas.crear_reserva(self.cliente, "201", fecha_inicio, fecha_fin)

        self.gestor_reservas.cancelar_reserva(reserva)
        self.assertEqual(reserva.estado, "cancelada")
        self.assertEqual(reserva.habitacion.estado, "disponible")

if __name__ == '__main__':
    unittest.main()