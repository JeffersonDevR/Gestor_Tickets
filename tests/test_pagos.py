import unittest
import asyncio
from Modulos.Pagos import GestorDePagos, PagoEnEfectivo, PagoConTarjeta

class TestPagos(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.gestor_pagos = GestorDePagos()

    async def test_pago_en_efectivo_exitoso(self):
        pago = PagoEnEfectivo(monto=100.0)
        self.assertTrue(await self.gestor_pagos.realizar_pago(pago))
        self.assertEqual(pago.estado, "completado")

    async def test_pago_con_tarjeta_exitoso(self):
        pago = PagoConTarjeta(monto=200.0, numero_tarjeta="1234567812345678", cvv="123")
        self.assertTrue(await self.gestor_pagos.realizar_pago(pago))
        self.assertEqual(pago.estado, "completado")

    def test_pago_con_tarjeta_invalida(self):
        with self.assertRaises(ValueError):
            PagoConTarjeta(monto=100.0, numero_tarjeta="invalido", cvv="123")

    def test_pago_con_tarjeta_invalida(self):
        # Probamos que un pago con datos de tarjeta inválidos es rechazado.
        with self.assertRaises(ValueError):
            PagoConTarjeta(monto=100.0, numero_tarjeta="invalido", cvv="123")

if __name__ == '__main__':
    unittest.main()