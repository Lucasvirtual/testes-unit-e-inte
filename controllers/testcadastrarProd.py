import unittest

class Produto:
    def __init__(self, nome, custo, categoria, estoque=0, id = None):
        self.nome = nome
        self.custo = custo
        self.categoria = categoria
        self.estoque = estoque
        self.id = id

class TestProduto(unittest.TestCase):

    def setUp(self):
        self.produto = Produto("Caneta", 1, "ACESSÓRIO", 26, 1)

    #produto tem que ter pelo menos 1 caracter
    def test_cadastrar_produto(self):
        self.assertGreaterEqual(len(self.produto.nome), 1)

    #preco nao pode ser menor que 0
    def test_preco(self):
        self.assertGreaterEqual(len(str(self.produto.custo)), 1)
        self.assertLess(0, self.produto.custo)

    #categoria deve ser igual
    def test_criar_produto(self):
        produto = Produto('Teste', 10.0, 'Categoria')
        self.assertEqual(produto.categoria, "Categoria")


class TestProdutoIntegracao(unittest.TestCase):

    def setUp(self):
        self.produto = Produto("Caneta", 1, "ACESSÓRIO", 26, 1)
        self.assertGreaterEqual(len(self.produto.nome), 1)
        self.assertGreaterEqual(len(str(self.produto.custo)), 1)
        self.assertLess(0, self.produto.custo)
        produto = Produto('Teste', 10.0, 'Categoria')
        self.assertEqual(produto.categoria, "abc")

if __name__ == '__main__':
    unittest.main()