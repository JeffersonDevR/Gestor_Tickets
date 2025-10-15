import unittest
<<<<<<< HEAD
from unittest.mock import patch, MagicMock
=======
from unittest.mock import patch
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)
from main import HotelApp
from Modulos.Clientes import Cliente

class TestHotelApp(unittest.TestCase):

    def setUp(self):
        """
        Prepara un estado limpio para cada prueba.
        """
        Cliente.clientes_registrados = []
        self.app = HotelApp()
<<<<<<< HEAD
        self.cliente_prueba = Cliente.registrar_cliente("Test User", 12345, "test@example.com", "555-1234")
        if self.cliente_prueba:
            self.app.reservas.crear_reserva(self.cliente_prueba.nombre, "101", "15/10/2025", "14:00")

    @patch('builtins.input', side_effect=['1', '2', '2', '202', 'Suite', '600', '4', '5', '3'])
    @patch('Modulos.Habitaciones.GestorHabitaciones.agregar_habitacion')
    def test_admin_crear_habitacion(self, mock_agregar, mock_input):
        """
        Prueba el flujo de admin para crear una nueva habitación.
        """
        self.app.menu_principal()
        mock_agregar.assert_called_once()

    @patch('builtins.input', side_effect=['1', '3', '2', '12345', '102', '16/10/2025', '10:00', '3', '5', '3'])
    @patch('Modulos.Reservas.Reservas.crear_reserva')
    def test_admin_crear_reserva(self, mock_crear_reserva, mock_input):
        """
        Prueba el flujo de admin para crear una reserva para un cliente.
        """
        self.app.menu_principal()
        mock_crear_reserva.assert_called_with("Test User", "102", "16/10/2025", "10:00")

    @patch('builtins.input', side_effect=['2', '1', '12345', '4', '1', 'efectivo', '5', '3'])
    def test_cliente_pagar_reservacion(self, mock_input):
        """
        Prueba el flujo de cliente para pagar una reservación.
        """
        with patch.object(self.app, 'realizar_pago') as mock_realizar_pago:
            self.app.menu_principal()
            mock_realizar_pago.assert_called_with(150.0)
=======

    @patch('builtins.input', side_effect=['2', '2', 'New User', '54321', 'new@example.com', '5554321', '3'])
    @patch('Modulos.Clientes.Cliente.registrar_cliente')
    def test_flujo_registro_y_salida(self, mock_registrar, mock_input):
        """
        Prueba el flujo de admin para crear una nueva habitación.
        """
        self.app.menu_principal()
        mock_agregar.assert_called_once()

    @patch('builtins.input', side_effect=['1', '3', '2', '12345', '102', '16/10/2025', '10:00', '3', '5', '3'])
    @patch('Modulos.Reservas.Reservas.crear_reserva')
    def test_admin_crear_reserva(self, mock_crear_reserva, mock_input):
        """
        Prueba el flujo de admin para crear una reserva para un cliente.
        """
        self.app.menu_principal()
        mock_crear_reserva.assert_called_with("Test User", "102", "16/10/2025", "10:00")

    @patch('builtins.input', side_effect=['2', '1', '12345', '4', '1', 'efectivo', '5', '3'])
    def test_cliente_pagar_reservacion(self, mock_input):
        """
        Prueba el flujo de cliente para pagar una reservación.
        """
        self.app.menu_principal()
        # Verifica que se muestre el mensaje de bienvenida correcto.
        mock_print.assert_any_call("\n--- Bienvenido, Admin ---")
>>>>>>> 25806a2 (feat: Implement main menu and refactor Pagos module)

if __name__ == '__main__':
    unittest.main()