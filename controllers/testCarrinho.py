import unittest

class Carrinho:
    def __init__(self, nome):
        self.nome = nome

class TestCarrinho(unittest.TestCase):

    def setUp(self):
        self.Carrinho = Carrinho("asddsad")
    #nome nao pode ser vazio
    def test_cadastrar_produto(self):
        self.assertGreaterEqual(len(self.Carrinho.nome), 1)
