import unittest
from ej1 import Cliente

class TestCliente(unittest.TestCase):

    def test_ingresar_20(self):
        cliente = Cliente("ejemplo")
        cliente.ingresar_20()
        self.assertEqual(cliente.saldo, 1300)

    def test_ingresar_50(self):
        cliente = Cliente("ejemplo")
        cliente.ingresar_50()
        self.assertEqual(cliente.saldo, 1100)

    def test_ingresar_100(self):
        cliente = Cliente("ejemplo")
        cliente.ingresar_100()
        self.assertEqual(cliente.saldo, 4100)

    def test_retirar_20(self):
        cliente = Cliente("ejemplo")
        
        cliente.retirar_20()
        self.assertEqual(cliente.saldo, 3980)

    def test_retirar_50(self):
        cliente = Cliente("ejemplo")
        
        cliente.retirar_50()
        self.assertEqual(cliente.saldo, 3950)

    def test_retirar_100(self):
        cliente = Cliente("ejemplo")
        
        cliente.retirar_100()
        self.assertEqual(cliente.saldo, 3900)

if __name__ == '__main__':
    unittest.main()