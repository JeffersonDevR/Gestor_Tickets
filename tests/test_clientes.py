import unittest
from Modulos.Clientes import Cliente

class TestClientes(unittest.TestCase):

    def setUp(self):
        # Este método se ejecuta antes de cada prueba.
        # Limpiamos la lista de clientes para asegurar que las pruebas sean independientes.
        Cliente.clientes_registrados = []

    def test_registrar_cliente_exitoso(self):
        # Probamos que un cliente puede ser registrado exitosamente.
        cliente = Cliente.registrar_cliente("Juan Perez", 12345678, "juan.perez@email.com", "555-1234")
        self.assertIsNotNone(cliente)
        self.assertEqual(len(Cliente.clientes_registrados), 1)
        self.assertEqual(Cliente.clientes_registrados[0].nombre, "Juan Perez")

    def test_registrar_cliente_duplicado(self):
        # Probamos que no se puede registrar un cliente con un número de identificación ya existente.
        Cliente.registrar_cliente("Juan Perez", 12345678, "juan.perez@email.com", "555-1234")
        cliente_duplicado = Cliente.registrar_cliente("Otro Nombre", 12345678, "otro@email.com", "555-5678")
        self.assertIsNone(cliente_duplicado)
        self.assertEqual(len(Cliente.clientes_registrados), 1)

    def test_actualizar_info_cliente_existente(self):
        # Probamos que la información de un cliente existente puede ser actualizada.
        Cliente.registrar_cliente("Ana Gomez", 87654321, "ana.gomez@email.com", "555-8765")
        actualizado = Cliente.actualizar_info_cliente(87654321, nuevo_nombre="Ana G. Lopez", nuevo_correo="ana.lopez@email.com")
        self.assertTrue(actualizado)
        cliente_actualizado = Cliente.clientes_registrados[0]
        self.assertEqual(cliente_actualizado.nombre, "Ana G. Lopez")
        self.assertEqual(cliente_actualizado.correo, "ana.lopez@email.com")

    def test_actualizar_info_cliente_inexistente(self):
        # Probamos que no se puede actualizar la información de un cliente que no existe.
        actualizado = Cliente.actualizar_info_cliente(99999999, nuevo_nombre="Fantasma")
        self.assertFalse(actualizado)

if __name__ == '__main__':
    unittest.main()