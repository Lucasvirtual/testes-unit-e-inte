import unittest
import re

class Cliente:
    def __init__(self, nome, email, telefone, id):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.id = id

def is_valid_email(email):
    """
    Verifica se o email fornecido é válido.
    Retorna True se o email for válido e False caso contrário.
    """
    # Expressão regular para validar o formato do email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Verifica se o email corresponde ao padrão definido pela expressão regular
    return bool(re.match(pattern, email))


class UnitTestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Lucas", "lucas@email.com", "75992492224", 1)

    # Não pode ficar vazio
    def test_nome(self):
        self.assertGreaterEqual(len(self.cliente.nome), 1)

    def test_valid_email(self):
        # Teste com um email válido
        self.assertTrue(is_valid_email(self.cliente.email))

    def test_telefone(self):
        self.assertEqual(len(self.cliente.telefone), 11)


class IntegrationTestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Lucas", "lucas@email.com", "75992492224", 1)

    # Não pode ficar vazio
    def test_cliente(self):
        self.assertGreaterEqual(len(self.cliente.nome), 1)
        self.assertTrue(is_valid_email(self.cliente.email))
        self.assertEqual(len(self.cliente.telefone), 11)

if __name__ == '__main__':
    unittest.main()