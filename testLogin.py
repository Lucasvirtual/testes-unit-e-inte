import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestLogin(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_login_sucesso(self, mock_stdout):
        with patch('builtins.input', side_effect=['admin', 'admin']):
            self.assertTrue(main.login())
            self.assertEqual(mock_stdout.getvalue(), 'Login successful!\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_login_falha(self, mock_stdout):
        with patch('builtins.input', side_effect=['admin', 'senha_incorreta']):
            self.assertFalse(main.login())
            self.assertEqual(mock_stdout.getvalue(), 'Invalid username or password.\n')

if __name__ == '__main__':
    unittest.main()
