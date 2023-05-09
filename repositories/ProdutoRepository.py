import mysql.connector
from entities.Produto import Produto
from repositories.Repository import Repository


class ProdutoRepository(Repository):
    @staticmethod
    def create(produto):
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()
        comando = f'INSERT INTO produto (nome, custo, categoria, estoque) VALUES ("{produto.nome}", {produto.custo}, "{produto.categoria}", {produto.consultar_estoque()});'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()



    @staticmethod
    def _read():
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()
        comando = 'SELECT * FROM produto;'
        cursor.execute(comando)
        resposta = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resposta

    @staticmethod
    def delete(produto):
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()
        comando = f'DELETE FROM produto WHERE produtoID="{produto.id}";'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def update(produto):
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()
        comando = f'UPDATE produto SET nome = "{produto.nome}", custo = {produto.custo}, ' \
                  f'categoria = "{produto.categoria}", estoque = {produto.consultar_estoque()} ' \
                  f'WHERE produtoID = {produto.id};'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def listar():
        dados = ProdutoRepository._read()
        produtos = []
        for id, nome, custo, categoria, estoque in dados:
            produtos.append(Produto(nome, custo, categoria, estoque))
        return produtos

    @staticmethod
    def buscar(nome_produto):
        conexao = ProdutoRepository.__criar_conexao()
        cursor = conexao.cursor()
        comando = f'SELECT * FROM produto WHERE nome = "{nome_produto}";'
        cursor.execute(comando)
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        produtos = []
        for id, nome, custo, categoria, estoque in dados:
            produtos.append(Produto(nome, custo, categoria, estoque, id))
        return produtos

    @staticmethod
    def __criar_conexao():
        return mysql.connector.connect(host='localhost', user='root', password='root', database='prova')


def create(produto):
    return None


def produtos():
    return None