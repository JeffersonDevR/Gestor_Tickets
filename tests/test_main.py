import unittest
from unittest.mock import patch, MagicMock, AsyncMock
from main import HotelApp
from Modulos.Clientes import Cliente

class TestHotelApp(unittest.IsolatedAsyncioTestCase):

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
    async def test_admin_crear_habitacion(self, mock_agregar, mock_input):
        """
        Prueba el flujo de admin para crear una nueva habitación.
        """
        await self.app.menu_principal()
        mock_agregar.assert_called_once()

    @patch('builtins.input', side_effect=['1', '3', '2', '12345', '102', '16/10/2025', '10:00', '3', '5', '3'])
    @patch('Modulos.Reservas.Reservas.crear_reserva')
    async def test_admin_crear_reserva(self, mock_crear_reserva, mock_input):
        """
        Prueba el flujo de admin para crear una reserva para un cliente.
        """
        await self.app.menu_principal()
        mock_crear_reserva.assert_called_with("Test User", "102", "16/10/2025", "10:00")

    @patch('builtins.input', side_effect=['2', '1', '12345', '5', '1', 'efectivo', '6', '3'])
    async def test_cliente_pagar_reservacion(self, mock_input):
        """
        Prueba el flujo de cliente para pagar una reservación.
        """
        with patch.object(self.app, 'realizar_pago', new_callable=AsyncMock) as mock_realizar_pago:
            await self.app.menu_principal()
            mock_realizar_pago.assert_awaited_with(150.0)

if __name__ == '__main__':
    unittest.main()