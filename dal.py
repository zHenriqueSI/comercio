from models import *


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open('files/categorias.txt', 'a') as txt:
            txt.writelines(f'{categoria.categoria}\n')

    @classmethod
    def ler(cls):
        with open('files/categorias.txt', 'r') as txt:
            cls.categorias = list(map(lambda x: x.strip('\n'), txt.readlines()))

        categorias_instances = [Categoria(x) for x in cls.categorias]

        return categorias_instances


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('files/vendas.txt', 'a') as txt:
            txt.writelines(f'{venda.produto_vendido.nome};{str(venda.produto_vendido.preco)};'
                           f'{venda.produto_vendido.categoria};{venda.vendedor};{venda.comprador};'
                           f'{str(venda.quantidade_vendida)};{venda.data}')
            txt.writelines('\n')

    @classmethod
    def ler(cls):
        with open('files/vendas.txt', 'r') as txt:
            vendas = list(map(lambda x: x.strip('\n').split(';'), txt.readlines()))

        if len(vendas) > 0:
            vendas_instances = [Venda(Produto(venda[0], venda[1], venda[2]), venda[3], venda[4], int(venda[5]), venda[6]) for venda in vendas]
        else:
            vendas_instances = []

        return vendas_instances


class DaoEstoque:
    @classmethod
    def salvar(cls, estoque: Estoque):
        with open('files/estoques.txt', 'a') as txt:
            txt.writelines(f'{estoque.produto.nome};{estoque.produto.preco};{estoque.produto.categoria};{estoque.quantidade}')
            txt.writelines('\n')

    @classmethod
    def ler(cls):
        with open('files/estoques.txt', 'r') as txt:
            estoques = list(map(lambda x: x.strip('\n').split(';'), txt.readlines()))

        estoques_instances = [Estoque(Produto(estoque[0], float(estoque[1]), estoque[2]), int(estoque[3])) for estoque in estoques]

        return estoques_instances


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('files/fornecedores.txt', 'a') as txt:
            txt.writelines(f'{fornecedor.nome};{fornecedor.cnpj};{fornecedor.telefone};{fornecedor.categoria}')
            txt.writelines('\n')

    @classmethod
    def ler(cls):
        with open('files/fornecedores.txt', 'r') as txt:
            fornecedores = list(map(lambda x: x.strip('\n').split(';'), txt.readlines()))

        fornecedores_instances = [Fornecedor(fornecedor[0], fornecedor[1], fornecedor[2], fornecedor[3]) for fornecedor in fornecedores]

        return fornecedores_instances


class DaoCliente:
    @classmethod
    def salvar(cls, cliente: Cliente):
        with open('files/clientes.txt', 'a') as txt:
            txt.writelines(f'{cliente.nome};{cliente.cpf};{cliente.telefone};{cliente.email};{cliente.endereco}')
            txt.writelines('\n')

    @classmethod
    def ler(cls):
        with open('files/clientes.txt', 'r') as txt:
            clientes = list(map(lambda x: x.strip('\n').split(';'), txt.readlines()))

        clientes_instances = [Cliente(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]) for cliente in clientes]

        return clientes_instances


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('files/funcionarios.txt', 'a') as txt:
            txt.writelines(f'{funcionario.nome};{funcionario.cpf};{funcionario.telefone};{funcionario.email};{funcionario.endereco};{funcionario.modelo_trabalho}')
            txt.writelines('\n')

    @classmethod
    def ler(cls):
        with open('files/funcionarios.txt', 'r') as txt:
            funcionarios = list(map(lambda x: x.strip('\n').split(';'), txt.readlines()))

        funcionarios_instances = [Funcionario(funcionario[0], funcionario[1], funcionario[2], funcionario[3], funcionario[4], funcionario[5]) for funcionario in funcionarios]

        return funcionarios_instances
