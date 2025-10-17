import unittest
from Modulos.Pagos import GestorDePagos, PagoEnEfectivo, PagoConTarjeta

class TestPagos(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba para tener un gestor de pagos limpio.
        self.gestor_pagos = GestorDePagos()

    def test_pago_en_efectivo_exitoso(self):
        # Probamos que un pago en efectivo se procesa correctamente.
        pago = PagoEnEfectivo(monto=100.0)
        resultado = self.gestor_pagos.realizar_pago(pago)
        self.assertTrue(resultado)
        self.assertEqual(pago.estado, "completado")
        self.assertIn(pago, self.gestor_pagos.pagos_procesados)

    def test_pago_con_tarjeta_exitoso(self):
        # Probamos que un pago con tarjeta válido se procesa correctamente.
        pago = PagoConTarjeta(monto=250.0, numero_tarjeta="1234567890123456", cvv="123")
        resultado = self.gestor_pagos.realizar_pago(pago)
        self.assertTrue(resultado)
        self.assertEqual(pago.estado, "completado")

    def test_pago_con_tarjeta_numero_invalido(self):
        # Probamos que un pago con un número de tarjeta inválido es rechazado.
        with self.assertRaises(ValueError):
            PagoConTarjeta(monto=300.0, numero_tarjeta="12345", cvv="123")

    def test_pago_con_tarjeta_cvv_invalido(self):
        # Probamos que un pago con un CVV inválido es rechazado.
        with self.assertRaises(ValueError):
            PagoConTarjeta(monto=350.0, numero_tarjeta="1234567890123456", cvv="12")

    def test_pago_con_monto_negativo(self):
        # Probamos que un pago con un monto negativo es rechazado.
        with self.assertRaises(ValueError):
            PagoEnEfectivo(monto=-50.0)

    def test_pago_con_tarjeta_invalida(self):
        # Probamos que un pago con datos de tarjeta inválidos es rechazado.
        with self.assertRaises(ValueError):
            PagoConTarjeta(monto=100.0, numero_tarjeta="invalido", cvv="123")

if __name__ == '__main__':
    unittest.main()