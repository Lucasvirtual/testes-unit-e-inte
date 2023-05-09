class Produto:
    def __init__(self, nome, custo, categoria, estoque=0, id = None):
        self._nome = nome.upper()
        self._custo = custo
        self._categoria = categoria.upper()
        self._estoque = estoque
        self.__id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome != '':
            self._nome = novo_nome.upper()
        else:
            raise ValueError('Nome de produto inválido')

    @property
    def custo(self):
        return self._custo

    @custo.setter
    def custo(self, novo_custo):
        if novo_custo >= 0.0:
            self._custo = novo_custo
        else:
            raise ValueError('Valor de custo inválido')

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria.upper()

    def consultar_estoque(self):
        return self._estoque

    def alterar_estoque(self, quantidade, remover=False):
        if quantidade > 0:
            if remover:
                if quantidade <= self._estoque:
                    self._estoque -= quantidade
                else:
                    raise ValueError('Estoque insuficiente')
            else:
                self._estoque += quantidade
        else:
            raise ValueError('Quantidade inválida')

    @property
    def id(self):
        return self.__id


    def __str__(self):
        return f'Produto: {self.nome} - Custo: R$ {self.custo} - Categoria: {self.categoria} - Estoque: {self.consultar_estoque()} unidades'


