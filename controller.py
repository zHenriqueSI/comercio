from models import *
from dal import *
from datetime import datetime


class ControllerCategoria:
    @classmethod
    def cadastrar(cls, categoria: Categoria):
        categoria_exite = False
        categorias_instances = DaoCategoria.ler()
        for categoria_instance in categorias_instances:
            if categoria.categoria == categoria_instance.categoria:
                categoria_exite = True
                print(f"Falha ao cadastrar a categoria '{categoria.categoria}'! Esta categoria já existe!")
        if not categoria_exite:
            DaoCategoria.salvar(categoria)
            print(f"Categoria '{categoria.categoria}' cadatrada com sucesso!")

    @classmethod
    def remover(cls, categoria: Categoria):
        # TODO: mudar categoria removida para 'sem categoria' no estoque
        categorias_instances = DaoCategoria.ler()
        categoria_remover = list(filter(lambda x: x.categoria == categoria.categoria, categorias_instances))
        if len(categoria_remover) > 0:
            categoria_remover = categoria_remover[0].categoria
            for i, categoria in enumerate(categorias_instances):
                if categoria_remover == categoria.categoria:
                    categorias_instances.pop(i)
                    break

            with open('files/categorias.txt', 'w') as txt:
                for categoria in categorias_instances:
                    txt.writelines(f'{categoria.categoria}\n')
                    print(f"Categoria '{categoria.categoria}' removida com sucesso!")

        else:
            print(f"Falha ao remover a categoria '{categoria.categoria}'! Esta categoria não existe!")

    @classmethod
    def mudar_nome(cls, categoria: Categoria, nova_categoria: Categoria):
        # TODO: mudar também o nome da categoria no estoque
        categorias_instances = DaoCategoria.ler()
        categoria_mudar = list(filter(lambda x: x.categoria == categoria.categoria, categorias_instances))
        if len(categoria_mudar) > 0:
            if categoria.categoria == nova_categoria.categoria:
                print(f"Falha ao mudar o nome da categoria '{categoria.categoria}'! O novo nome não pode ser igual ao antigo!")
            else:
                categoria_mudar = categoria_mudar[0].categoria
                categorias_instances = list(map(lambda x: nova_categoria if(x.categoria == categoria_mudar) else (x), categorias_instances))
                print(f"O nome da categoria '{categoria.categoria}' foi alterado para '{nova_categoria.categoria}' com sucesso!")

            with open('files/categorias.txt', 'w') as txt:
                for categoria in categorias_instances:
                    txt.writelines(f'{categoria.categoria}\n')

        else:
            print(f"Falha ao mudar o nome da categoria '{categoria.categoria}'! Esta categoria não existe!")

    @classmethod
    def mostrar_categorias(cls):
        categorias_instances = DaoCategoria.ler()
        if len(categorias_instances) > 0:
            for categoria_instance in categorias_instances:
                print(categoria_instance.categoria)


class ControllerEstoque:
    @classmethod
    def cadastrar_produto(cls, nome, preco, categoria: Categoria, quantidade):
        estoques_instances = DaoEstoque.ler()
        categorias_instances = DaoCategoria.ler()
        busca_instancia_produto = list(filter(lambda x: x.produto.nome == nome, estoques_instances))
        busca_instancia_categoria = list(filter(lambda x: x.categoria == categoria.categoria, categorias_instances))
        if len(busca_instancia_produto) == 0:
            if len(busca_instancia_categoria) > 0:
                estoque = Estoque(Produto(nome, preco, categoria.categoria), quantidade)
                DaoEstoque.salvar(estoque)
                print(f"Produto '{nome}' cadastrado com sucesso!'")
            else:
                print(f"Falha ao cadastrar o produto '{nome}'! A categoria {categoria.categoria} não existe!")
        else:
            print(f"Falha ao cadastrar o produto '{nome}'! Este produto já está cadastrado!")

    @classmethod
    def remover_produto(cls, nome):
        estoques_instances = DaoEstoque.ler()
        produto_remover = list(filter(lambda x: x.produto.nome == nome, estoques_instances))
        if len(produto_remover) > 0:
            produto_remover = produto_remover[0].produto.nome
            for i, estoque_instance in enumerate(estoques_instances):
                if estoque_instance.produto.nome == produto_remover:
                    estoques_instances.pop(i)
                    break
            with open('files/estoques.txt', 'w') as txt:
                for estoque_instance in estoques_instances:
                    txt.writelines(f"{estoque_instance.produto.nome};{estoque_instance.produto.preco};{estoque_instance.produto.categoria};{estoque_instance.quantidade}")
                    txt.writelines('\n')
            print(f"Produto '{nome}' removido com sucesso!")

        else:
            print(f"Falha ao remover o produto '{nome}'! O produto {nome} não existe!")

    @classmethod
    def alterar_produto(cls, nome, novo_nome, novo_preco, nova_categoria: Categoria, nova_quantidade):
        estoques_intances = DaoEstoque.ler()
        categorias_intances = DaoCategoria.ler()
        produto_mudar = list(filter(lambda x: x.produto.nome == nome, estoques_intances))
        categoria_mudar = list(filter(lambda x: x.categoria == nova_categoria.categoria, categorias_intances))

        if len(produto_mudar) > 0:
            if len(categoria_mudar) > 0:
                produto_mudar = list(filter(lambda x: x.produto.nome == novo_nome, estoques_intances))
                if len(produto_mudar) == 0:
                    estoques_intances = list(map(lambda x: Estoque(Produto(novo_nome, novo_preco, nova_categoria.categoria), nova_quantidade) if(x.produto.nome == nome) else (x), estoques_intances))
                    with open('files/estoques.txt', 'w') as txt:
                        for estoque_instance in estoques_intances:
                            txt.writelines(f'{estoque_instance.produto.nome};{estoque_instance.produto.preco};{estoque_instance.produto.categoria};{estoque_instance.quantidade}')
                            txt.writelines('\n')
                    print(f"Produto '{nome}' alterado com sucesso!")
                else:
                    print(f"Falha ao alterar o produto '{nome}'! O produto '{novo_nome}' já existe!")
            else:
                print(f"Falha ao alterar o produto '{nome}'! A categoria '{nova_categoria.categoria}' não existe!")

        else:
            print(f"Falha ao alterar o produto '{nome}'! Este produto não está cadastrado!")

    @classmethod
    def mostrar_produtos(cls):
        estoques_instances = DaoEstoque.ler()
        if len(estoques_instances) > 0:
            print("========== Produtos ==========")
            for estoque_instance in estoques_instances:
                print(f"Nome: {estoque_instance.produto.nome}")
                print(f"Preço: {estoque_instance.produto.preco}")
                print(f"Categoria: {estoque_instance.produto.categoria}")
                print(f"Quantidade: {estoque_instance.quantidade}")
                print("-"*30)

        else:
            print(f"Falha ao mostrar o estoque de produtos! Não há nenhuma produto cadastrado!")


class ControllerVenda:
    @classmethod
    def cadastrar_venda(cls, nome_produto, vendedor, comprador, quantidade_vendida):
        # TODO: verificar a existência do cliente e do vendedor
        estoques_instances = DaoEstoque.ler()
        busca_instancia_estoque = list(filter(lambda x: x.produto.nome == nome_produto, estoques_instances))
        if len(busca_instancia_estoque) > 0:
            estoque_instance = busca_instancia_estoque[0]
            if quantidade_vendida < int(estoque_instance.quantidade):
                venda_instance = Venda(estoque_instance.produto, vendedor, comprador, quantidade_vendida)
                DaoVenda.salvar(venda_instance)
                estoque_instance.quantidade = int(estoque_instance.quantidade) - int(quantidade_vendida)
                estoques_instances = list(map(lambda x: estoque_instance if(x.produto.nome == nome_produto) else(x), estoques_instances))
                with open('files/estoques.txt', 'w') as txt:
                    for estoque_instance in estoques_instances:
                        txt.writelines(f'{estoque_instance.produto.nome};{estoque_instance.produto.preco};{estoque_instance.produto.categoria};{estoque_instance.quantidade}')
                        txt.writelines('\n')
                print(f"A venda do produto '{nome_produto}' foi cadastrada com sucesso!")
            else:
                print(f"Falha ao cadastrar a venda do produto '{nome_produto}'! Não há estoque suficiente!")
        else:
            print(f"Falha ao cadastrar a venda do produto '{nome_produto}'! Este produto não existe!")


ControllerVenda.cadastrar_venda('Detergente YP', 'Henrique', 'Kennedy', 100)