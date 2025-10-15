import unittest
from unittest.mock import patch
from main import HotelApp
from Modulos.Clientes import Cliente

class TestHotelApp(unittest.TestCase):

    def setUp(self):
        """
        Prepara un estado limpio para cada prueba.
        """
        Cliente.clientes_registrados = []
        self.app = HotelApp()
        # Pre-registrar un cliente para pruebas de login y pago
        self.cliente_prueba = Cliente.registrar_cliente("Test User", 12345, "test@example.com", "555-1234")
        if self.cliente_prueba:
            self.app.reservas.crear_reserva(self.cliente_prueba.nombre, "101", "15/10/2025", "14:00")

    @patch('builtins.input', side_effect=['2', '2', 'New User', '54321', 'new@example.com', '5554321', '3'])
    @patch('Modulos.Clientes.Cliente.registrar_cliente')
    def test_flujo_registro_y_salida(self, mock_registrar, mock_input):
        """
        Prueba el flujo: Cliente -> Registrar -> Llenar datos -> Salir.
        """
        self.app.menu_principal()
        mock_registrar.assert_called_with('New User', 54321, 'new@example.com', 5554321)

    @patch('builtins.input', side_effect=['1', '4', '1', '250.50', 'efectivo', '4', '5', '3'])
    @patch('builtins.print')
    def test_admin_procesar_pago(self, mock_print, mock_input):
        """
        Prueba el flujo de admin: Admin -> Pagos -> Procesar Pago -> Volver -> Salir.
        """
        self.app.menu_principal()
        mock_print.assert_any_call("Pago en efectivo de $250.50 procesado exitosamente.")

    @patch('builtins.input', side_effect=['2', '1', '12345', '4', '1', '5', '3'])
    def test_cliente_pagar_reservacion(self, mock_input):
        """
        Prueba el flujo: Cliente -> Login -> Pagar -> Seleccionar Reserva -> Cerrar Sesión -> Salir.
        """
        with patch.object(self.app, 'realizar_pago') as mock_realizar_pago:
            self.app.menu_principal()
            # Verifica que se llamó a realizar_pago con la tarifa de la habitación 101 (150.0)
            mock_realizar_pago.assert_called_with(150.0)

if __name__ == '__main__':
    unittest.main()