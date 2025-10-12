import unittest
from datetime import datetime
from Modulos.Pagos import PagoEnEfectivo, PagoConTarjeta

class TestPagosIntegration(unittest.TestCase):

    def test_pago_en_efectivo_valido(self):
        # Integration test for cash payment
        pago = PagoEnEfectivo(100.0, datetime.now())
        self.assertTrue(pago.validate())
        self.assertTrue(pago.process())
        self.assertEqual(pago.status, "completed")

    def test_pago_en_efectivo_invalido(self):
        # Test invalid cash payment (negative amount)
        pago = PagoEnEfectivo(-50.0, datetime.now())
        self.assertFalse(pago.validate())
        self.assertFalse(pago.process())
        self.assertEqual(pago.status, "pending")

    def test_pago_con_tarjeta_valido(self):
        # Integration test for card payment
        pago = PagoConTarjeta(200.0, datetime.now(), "12345678901234567890123456", "123")
        self.assertTrue(pago.validate())
        self.assertTrue(pago.process())
        self.assertEqual(pago.status, "completed")

    def test_pago_con_tarjeta_invalido_card_length(self):
        # Test invalid card number length
        pago = PagoConTarjeta(200.0, datetime.now(), "1234567890123456", "123")  # too short
        self.assertFalse(pago.validate())
        self.assertFalse(pago.process())
        self.assertEqual(pago.status, "pending")

    def test_pago_con_tarjeta_invalido_cvv_length(self):
        # Test invalid CVV length
        pago = PagoConTarjeta(200.0, datetime.now(), "12345678901234567890123456", "12")  # too short
        self.assertFalse(pago.validate())
        self.assertFalse(pago.process())
        self.assertEqual(pago.status, "pending")

if __name__ == '__main__':
    unittest.main()
