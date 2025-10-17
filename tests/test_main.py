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
        self.cliente_prueba = Cliente.registrar_cliente("Test User", 12345, "test@example.com", "555-1234")
        if self.cliente_prueba:
            self.app.reservas.crear_reserva(self.cliente_prueba, "101", "15/10/2025", "14:00")

    @patch('builtins.input', side_effect=['1', '2', '2', '202', 'Suite', '600', '4', '5', '3'])
    @patch('Modulos.Habitaciones.GestorHabitaciones.agregar_habitacion')
    async def test_admin_crear_habitacion(self, mock_agregar, mock_input):
        """
        Prueba el flujo de admin para crear una nueva habitación.
        """
        await self.app.menu_principal()
        mock_agregar.assert_called_once()

    @patch('builtins.input', side_effect=['1', '3', '2', '12345', '102', '16/10/2025', '10:00', '5', '5', '3'])
    @patch('Modulos.Reservas.GestorReservas.crear_reserva')
    async def test_admin_crear_reserva(self, mock_crear_reserva, mock_input):
        """
        Prueba el flujo de admin para crear una reserva para un cliente.
        """
        await self.app.menu_principal()
        mock_crear_reserva.assert_called_with(self.cliente_prueba, "102", "16/10/2025", "10:00")

    @patch('builtins.input', side_effect=['2', '1', '12345', '7', '1', 'efectivo', '8', '3'])
    async def test_cliente_pagar_reservacion(self, mock_input):
        """
        Prueba el flujo de cliente para pagar una reservación.
        """
        self.app.gestor_habitaciones.habitaciones.append(MagicMock(numero="101", tarifa=150.0))
        self.app.reservas.lista_reservas.append(MagicMock(cliente=self.cliente_prueba, habitacion=self.app.gestor_habitaciones.habitaciones[0]))

        with patch.object(self.app, 'realizar_pago', new_callable=AsyncMock) as mock_realizar_pago:
            await self.app.menu_principal()
            mock_realizar_pago.assert_awaited_with(150.0)

    @patch('builtins.input', side_effect=['2', '1', '12345', '3', '101', '20/10/2025', '12:00', 's', 'efectivo', '8', '3'])
    async def test_cliente_crear_reserva_y_pagar(self, mock_input):
        """
        Prueba el flujo de cliente para crear una reserva y pagarla inmediatamente.
        """
        self.app.gestor_habitaciones.habitaciones.append(MagicMock(numero="101", tarifa=200.0, estado="disponible"))

        with patch.object(self.app, 'realizar_pago', new_callable=AsyncMock) as mock_realizar_pago:
            await self.app.menu_principal()
            mock_realizar_pago.assert_awaited_with(200.0)

    @patch('builtins.input', side_effect=['2', '1', '12345', '6', '1', '8', '3'])
    async def test_cliente_cancelar_reserva(self, mock_input):
        """
        Prueba el flujo de cliente para cancelar una reserva.
        """
        habitacion = MagicMock(numero="101", tarifa=150.0)
        self.app.gestor_habitaciones.habitaciones.append(habitacion)
        self.app.reservas.lista_reservas.append(MagicMock(cliente=self.cliente_prueba, habitacion=habitacion))

        with patch.object(self.app.reservas, 'cancelar_reserva') as mock_cancelar:
            await self.app.menu_principal()
            mock_cancelar.assert_called_with("101")

    @patch('builtins.input', side_effect=['2', '1', '12345', '5', '1', '21/10/2025', '13:00', '102', '8', '3'])
    async def test_cliente_modificar_reserva(self, mock_input):
        """
        Prueba el flujo de cliente para modificar una reserva.
        """
        habitacion1 = MagicMock(numero="101", tarifa=150.0)
        habitacion2 = MagicMock(numero="102", tarifa=200.0, estado="disponible")
        self.app.gestor_habitaciones.habitaciones.extend([habitacion1, habitacion2])
        self.app.reservas.lista_reservas.append(MagicMock(cliente=self.cliente_prueba, habitacion=habitacion1, fecha="20/10/2025", hora="12:00"))

        with patch.object(self.app.reservas, 'modificar_reserva') as mock_modificar:
            await self.app.menu_principal()
            mock_modificar.assert_called_with("101", nueva_fecha="21/10/2025", nueva_hora="13:00", nueva_habitacion_numero="102")

if __name__ == '__main__':
    unittest.main()