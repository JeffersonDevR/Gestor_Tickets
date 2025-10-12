import unittest
from Modulos.Clientes import Cliente

class TestClientesIntegration(unittest.TestCase):

    def setUp(self):
        # Clear the class list before each test
        Cliente.clientes_registrados.clear()

    def test_registrar_cliente_exitoso(self):
        # Integration test for registering a new client
        cliente = Cliente.registrar_cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        self.assertIsNotNone(cliente)
        self.assertEqual(len(Cliente.clientes_registrados), 1)
        self.assertEqual(cliente.nombre, "Juan Perez")
        self.assertEqual(cliente.n_identificacion, 123456789)

    def test_registrar_cliente_duplicado(self):
        # Test registering a duplicate client
        Cliente.registrar_cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        cliente2 = Cliente.registrar_cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        self.assertIsNone(cliente2)
        self.assertEqual(len(Cliente.clientes_registrados), 1)

    def test_registrar_multiples_clientes(self):
        # Test registering multiple clients
        Cliente.registrar_cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        Cliente.registrar_cliente("Maria Lopez", 987654321, "maria@example.com", 3007654321)
        self.assertEqual(len(Cliente.clientes_registrados), 2)

    def test_cliente_str(self):
        # Test the string representation
        cliente = Cliente("Juan Perez", 123456789, "juan@example.com", 3001234567)
        expected = "Cliente: Juan Perez||\nIdentificación: 123456789|| Correo electrónico: juan@example.com|| Número de contacto: 3001234567"
        self.assertEqual(str(cliente), expected)

if __name__ == '__main__':
    unittest.main()