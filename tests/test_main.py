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

    @patch('builtins.input', side_effect=['2', '2', 'Test User', '12345', 'test@example.com', '1234567890', '3'])
    def test_flujo_registro_y_salida(self, mock_input):
        """
        Prueba el flujo: Cliente -> Registrar -> Llenar datos -> Salir.
        """
        with patch('main.Cliente.registrar_cliente') as mock_registrar:
            self.app.menu_principal()
            mock_registrar.assert_called_with('Test User', 12345, 'test@example.com', 1234567890)

    @patch('builtins.input', side_effect=['1', '1', '1', '4', '3'])
    @patch('builtins.print')
    def test_flujo_admin_ver_clientes(self, mock_print, mock_input):
        """
        Prueba el flujo: Admin -> Clientes -> Ver todos -> Volver -> Salir.
        """
        self.app.menu_principal()
        # Verifica que la información del cliente 'Admin' se haya impreso.
        # Se busca en los argumentos de cada llamada a 'print'.
        found = any("Cliente: Admin" in str(call.args[0]) for call in mock_print.call_args_list if call.args)
        self.assertTrue(found, "La información del cliente Admin no se encontró en la salida de print.")

    @patch('builtins.input', side_effect=['2', '1', '0', '4', '3'])
    @patch('builtins.print')
    def test_flujo_login_y_cierre_sesion(self, mock_print, mock_input):
        """
        Prueba el flujo: Cliente -> Login -> ID 0 (Admin) -> Cerrar sesión -> Salir.
        """
        self.app.menu_principal()
        # Verifica que se muestre el mensaje de bienvenida correcto.
        mock_print.assert_any_call("\n--- Bienvenido, Admin ---")

if __name__ == '__main__':
    unittest.main()