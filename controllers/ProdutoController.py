import mysql

from entities.Produto import Produto
from repositories.ProdutoRepository import ProdutoRepository

class ProdutoController:

    @staticmethod
    def exibir_menu():
        try:
            print('---------- MENU ----------')
            print('1 - CADASTRAR PRODUTO')
            print('2 - LISTAR TODOS OS PRODUTOS ')
            print('3 - BUSCAR PRODUTO')
            print('4 - EXCLUIR PRODUTO')
            print('5 - COMPRAR PRODUTO')
            print('6 - CADASTRAR CLIENTE')
            print('7 - SAIR DO PROGRAMA')
            opcao = int(input('Digite o número da operação desejada: '))
            if opcao == 1:
                ProdutoController.cadastrar_produto()
            elif opcao == 2:
                ProdutoController.listar_produtos()
            elif opcao == 3:
                ProdutoController.buscar_produto()
            elif opcao == 4:
                ProdutoController.excluir_produto()
            elif opcao == 5:
                ProdutoController.comprar()
            elif opcao == 6:
                ProdutoController.cadastrar_cliente()
            elif opcao == 7:
                return False
            else:
                raise ValueError('Opção inválida')
        except ValueError as erro:
            print(erro)
        return True



    @staticmethod
    def cadastrar_produto():
        '''
        Método estático que deve solicitar ao usuário os dados necessários para cadastrar um Produto, em seguida
        deverá solicitar que o repositorio realize a insersão do produto no banco de dados. Este método deverá fazer
        o tratamento de exceções geradas pela entrada inconsistente de dados pelo usuário (basta exibir o texto da
        exceção).
        '''
        nome = input('Informe o nome do produto: ')
        custo = float(input('Informe o custo do produto: '))
        categoria = input('Informe a categoria do produto: ')
        prod = Produto(nome, custo, categoria)
        ProdutoRepository.create(prod)
        print('\nProduto cadastrado com sucesso\n\n')

    @staticmethod
    def listar_produtos():
        '''
        Método estático que deve solicitar que o repositorio realize uma consulta de todos os Produtos cadastrados
        no banco de dados. Listando cada produto e seu respectivo indice na lista de produtos recebida pelo repositorio.
        '''
        produtos = ProdutoRepository.listar()
        for i, item in enumerate(produtos):
            print(f'{i} --- {item}')
        print('\n\n')

    @staticmethod
    def buscar_produto():
        '''
        Método estático que deve solicitar ao usuário o nome de um Produto e solicitar que o repositorio realize uma
        consulta no banco de dados para buscar as informações deste produto. Em seguida, deve exibir ao usuário,
        as opções de ADICIONAR AO ESTOQUE e de REMOVER DO ESTOQUE, que, atraves do repositorio, adicionam ou remover
        quantidades do estoque daquele produto buscado. Este método deverá fazer o tratamento de exceções geradas pela
        entrada inconsistente de dados pelo usuário (basta exibir o texto da exceção).
        '''
        busca = input('Informe o nome do produto que deseja buscar: ')
        resultado = ProdutoRepository.buscar(busca.upper())
        if len(resultado) == 0:
            print('Produto não encontrado')
        else:
            produto = resultado[0]
            acao = 0
            while acao != 3:
                print(f'\n\n\nResultado --- {produto}\n')
                print('-----OPÇÕES DO PRODUTO----')
                print('1 - ADICIONAR AO ESTOQUE')
                print('2 - REMOVER DO ESTOQUE')
                print('3 - RETORNAR AO MENU PRINCIPAL')
                acao = int(input('Informe o numero da opção desejada: '))
                if acao == 1:
                    adc = int(input('Quantidade a ser adicionada: '))
                    produto.alterar_estoque(adc)
                    print(produto.id)
                    ProdutoRepository.update(produto)
                    print(f'{adc} unidades adicionada ao estoque do produto {produto.nome}')
                elif acao == 2:
                    rmv = int(input('Quantidade a ser removida: '))
                    produto.alterar_estoque(rmv, True)
                    ProdutoRepository.update(produto)
                    print(f'{adc} unidades removidas do estoque do produto {produto.nome}')
                elif acao == 3:
                    break
                else:
                    print('Opcao inválida')

    @staticmethod
    def excluir_produto():
        '''
        Método estático que deve solicitar ao usuario o nome de um Produto, pedir que o repositorio busque por este
        produtro no banco, e caso o produto exista no banco de dados, deverá realize a remoção do produto no banco de
        dados. Este método deverá fazer o tratamento de exceções geradas através entrada inconsistente de dados pelo
        usuário (basta exibir o texto da exceção).
        '''
        busca = input('Informe o nome do produto que deseja excluir: ')
        resultado = ProdutoRepository.buscar(busca.upper())
        if len(resultado) == 0:
            print('Produto não encontrado')
        else:
            produto = resultado[0]
            ProdutoRepository.delete(produto)
            print(f'O produto {produto.nome} foi excluido')


    @staticmethod
    def comprar():
        '''
        Método estático que permite selecionar um produto a partir do menu de produtos cadastrados,
        solicita a quantidade a ser comprada e atualiza o estoque do produto, bem como exibe o preço total da compra.
        '''
        produtos = ProdutoRepository.listar()
        if len(produtos) == 0:
            print('Não há produtos cadastrados.')
            return

        # Exibe os produtos cadastrados
        print('Produtos disponíveis:')
        for i, item in enumerate(produtos):
            print(f'{i} --- {item}')

        try:
            # Solicita a seleção do produto a ser comprado
            index = int(input('Selecione o produto que deseja comprar: '))
            produto = produtos[index]
            print(f'Selecionado: {produto}')

            # Solicita a quantidade a ser comprada
            qtd = int(input('Digite a quantidade que deseja comprar: '))
            if qtd <= 0:
                raise ValueError('Quantidade inválida')

            # Verifica se há estoque suficiente
            if produto.estoque < qtd:
                print('Não há estoque suficiente para essa compra.')
                return

            # Atualiza o estoque e exibe o preço total da compra
            produto.alterar_estoque(qtd, True)
            ProdutoRepository.update(produto)
            print(f'Compra realizada com sucesso! Preço total: R${qtd * produto.custo:.2f}')

        except (ValueError, IndexError) as erro:
            print(f'Erro ao realizar compra: {erro}')

    @staticmethod
    def cadastrar_cliente():
        nome = input("Digite o nome completo do cliente: ")
        email = input("Digite o email do cliente: ")
        telefone = input("Digite o telefone do cliente: ")

        conexao = ProdutoController.__criar_conexao()
        cursor = conexao.cursor()
        comando = f'INSERT INTO clientes (nome, email, telefone) VALUES ("{nome}", "{email}", "{telefone}");'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()

        print("Cliente cadastrado com sucesso!")


    @staticmethod
    def __criar_conexao():
        return mysql.connector.connect(host='localhost', user='root', password='root', database='prova')


def comprar():
    return None


def cadastrar_cliente():
    return None