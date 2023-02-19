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
            print("========== Categorias ==========")
            for categoria_instance in categorias_instances:
                print(categoria_instance.categoria)
                print("-"*32)


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
                print(f"Produto '{nome}' cadastrado com sucesso!")
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
            if quantidade_vendida < estoque_instance.quantidade:
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

    @classmethod
    def gerar_relatorio(cls):
        vendas_instances = DaoVenda.ler()
        if len(vendas_instances) > 0:
            relatorio_dic = {}
            for venda_instance in vendas_instances:
                if venda_instance.produto_vendido.nome in relatorio_dic.keys():
                    relatorio_dic[venda_instance.produto_vendido.nome] += venda_instance.quantidade_vendida
                else:
                    relatorio_dic[venda_instance.produto_vendido.nome] = venda_instance.quantidade_vendida

            print("========== Produtos ==========")
            for key, value in relatorio_dic.items():
                print(f"Produto: {key}")
                print(f"Número de vendas: {value}")
                print("-"*30)

        else:
            print("Erro ao gerar relatório! Não há vendas cadastradas!")

    @classmethod
    def mostrar_vendas(cls, data_inicio, data_fim):
        vendas_instances = DaoVenda.ler()
        data_inicio = datetime.strptime(data_inicio, "%d-%m-%Y")
        data_fim = datetime.strptime(data_fim, "%d-%m-%Y")
        if len(vendas_instances) > 0:
            vendas_selecionadas = list(filter(lambda x: datetime.strptime(x.data, "%d-%m-%Y") >= data_inicio 
                                                    and datetime.strptime(x.data, "%d-%m-%Y") <= data_fim, vendas_instances))
            print("========== Vendas  ==========")
            for venda in vendas_selecionadas:
                print(f"Nome: {venda.produto_vendido.nome}\n"
                      f"Preço: {venda.produto_vendido.preco}\n"
                      f"Categoria: {venda.produto_vendido.categoria}\n"
                      f"Vendedor: {venda.vendedor}\n"
                      f"Comprador: {venda.comprador}\n"
                      f"QTDE Vendida: {venda.quantidade_vendida}\n"
                      f"Data da venda: {venda.data}")
                print("-"*30)


class ControllerFornecedor:
    @classmethod
    def cadastrar_fornecedor(cls, nome, cnpj, telefone, categoria):
        fornecedores_instances = DaoFornecedor.ler()
        categorias_instances = DaoCategoria.ler()
        busca_cnpj = list(filter(lambda x: x.cnpj == cnpj, fornecedores_instances))
        busca_telefone = list(filter(lambda x: x.telefone == telefone, fornecedores_instances))
        busca_categoria = list(filter(lambda x: x.categoria == categoria, categorias_instances))
        if len(busca_cnpj) > 0:
            print(f"Falha ao cadastrar o fornecedor '{nome}'! O cnpj já existe!")
        elif len(busca_telefone) > 0:
            print(f"Falha ao cadastrar o fornecedor '{nome}'! O telefone já existe!")
        elif len(busca_categoria) == 0:
            print(f"Falha ao cadastrar o fornecedor '{nome}'! A categoria '{categoria}' ainda não foi cadastrada!")
        else:
            DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            print(f"A o cadastro do fornecedor '{nome}' foi realizado com com sucesso!")

    @classmethod
    def alterar_fornecedor(cls, cnpj_alterar, novo_nome, novo_cnpj, novo_telefone, nova_categoria):
        fornecedores_instances = DaoFornecedor.ler()
        categorias_instances = DaoCategoria.ler()
        busca_cnpj_alterar = list(filter(lambda x: x.cnpj == cnpj_alterar, fornecedores_instances))
        busca_cnpj_novo = list(filter(lambda x: x.cnpj == novo_cnpj, fornecedores_instances))
        busca_categoria = list(filter(lambda x: x.categoria == nova_categoria, categorias_instances))
        busca_telefone = list(filter(lambda x: x.telefone == novo_telefone, fornecedores_instances))
        if len(busca_cnpj_alterar) == 0:
            print(f"Falha ao alterar o fornecedor '{cnpj_alterar}'! Não há nenhum fornecedor com esse cnpj!")
        elif len(busca_cnpj_novo) > 0:
            print(f"Falha ao alterar o fornecedor '{cnpj_alterar}'! O novo cnpj '{novo_cnpj}' já existe!")
        elif len(busca_telefone) > 0:
            print(f"Falha ao alterar o fornecedor '{cnpj_alterar}'! O telefone já existe!")
        elif len(busca_categoria) == 0:
            print(f"Falha ao alterar o fornecedor '{cnpj_alterar}'! A categoria '{nova_categoria}' ainda não foi cadastrada!")
        else:
            fornecedores_instances = list(map(lambda x: Fornecedor(novo_nome, novo_cnpj, novo_telefone, nova_categoria) if(x.cnpj == cnpj_alterar) else(x), fornecedores_instances))
            with open('files/fornecedores.txt', 'w') as txt:
                for fornecedor_instance in fornecedores_instances:
                    txt.writelines(f"{fornecedor_instance.nome};{fornecedor_instance.cnpj};{fornecedor_instance.telefone};{fornecedor_instance.categoria}")
                    txt.writelines("\n")
            print(f"O fornecedor '{cnpj_alterar}' foi alterado com sucesso!")

    @classmethod
    def remover_fornecedor(cls, cnpj_remover):
        fornecedores_instances = DaoFornecedor.ler()
        busca_cnpj = list(filter(lambda x: x.cnpj == cnpj_remover, fornecedores_instances))
        if len(busca_cnpj) == 0:
            print(f"Falha ao remover o fornecedor '{cnpj_remover}'! Não há nenhum fornecedor com esse cnpj!")
        else:
            fornecedores_instances = list(filter(lambda x: x.cnpj != cnpj_remover, fornecedores_instances))
            with open('files/fornecedores.txt', 'w') as txt:
                for fornecedor_instance in fornecedores_instances:
                    txt.writelines(f"{fornecedor_instance.nome};{fornecedor_instance.cnpj};{fornecedor_instance.telefone};{fornecedor_instance.categoria}")
                    txt.writelines("\n")
            print(f"O fornecedor '{cnpj_remover}' foi removido com sucesso!")

    @classmethod
    def mostrar_fornecedores(cls):
        fornecedores_instances = DaoFornecedor.ler()
        if len(fornecedores_instances) == 0:
            print("A lista de fornecedores está vazia!")
        else:
            print("========== Fornecedores  ==========")
            for fornecedor_instance in fornecedores_instances:
                print(f"Nome: {fornecedor_instance.nome}\n"
                      f"CNPJ: {fornecedor_instance.cnpj}\n"
                      f"Telefone: {fornecedor_instance.telefone}\n"
                      f"Categoria: {fornecedor_instance.categoria}")
                print("-"*30)


class ControllerCliente:
    @classmethod
    def cadastrar_cliente(cls, nome, cpf, telefone, email, endereco):
        clientes_instances = DaoCliente.ler()
        busca_cpf = list(filter(lambda x: x.cpf == cpf, clientes_instances))
        busca_telefone = list(filter(lambda x: x.telefone == telefone, clientes_instances))
        busca_email = list(filter(lambda x: x.email == email, clientes_instances))
        if len(busca_cpf) > 0:
            print(f"Falha ao cadastrar o cliente '{cpf}'! O cpf já existe!")
        elif len(busca_telefone) > 0:
            print(f"Falha ao cadastrar o cliente '{cpf}'! O telefone já existe!")
        elif len(busca_email) > 0:
            print(f"Falha ao cadastrar o cliente '{cpf}'! O email já existe!")
        else:
            DaoCliente.salvar(Cliente(nome, cpf, telefone, email, endereco))
            print(f"O cadastro do cliente '{cpf}' foi realizado com com sucesso!")

    @classmethod
    def alterar_cliente(cls, cpf_alterar, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco):
        clientes_instances = DaoCliente.ler()
        busca_cpf_alterar = list(filter(lambda x: x.cpf == cpf_alterar, clientes_instances))
        busca_cpf_novo = list(filter(lambda x: x.cpf == novo_cpf, clientes_instances))
        busca_telefone = list(filter(lambda x: x.telefone == novo_telefone, clientes_instances))
        busca_email = list(filter(lambda x: x.email == novo_email, clientes_instances))
        if len(busca_cpf_alterar) == 0:
            print(f"Falha ao alterar o cliente '{cpf_alterar}'! Não há nenhum cliente com esse cpf!")
        elif len(busca_cpf_novo) > 0:
            print(f"Falha ao alterar o cliente '{cpf_alterar}'! O novo cpf '{novo_cpf}' já existe!")        
        elif len(busca_telefone) > 0:
            print(f"Falha ao alterar o cliente '{cpf_alterar}'! O telefone '{novo_telefone}' já existe!")
        elif len(busca_email) > 0:
            print(f"Falha ao alterar o cliente '{cpf_alterar}'! O email '{novo_email}' já existe!")
        else:
            clientes_instances = list(map(lambda x: Cliente(novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco) if(x.cpf == cpf_alterar) else(x), clientes_instances))
            with open('files/clientes.txt', 'w') as txt:
                for cliente_instance in clientes_instances:
                    txt.writelines(f"{cliente_instance.nome};{cliente_instance.cpf};{cliente_instance.telefone};{cliente_instance.email};{cliente_instance.endereco}")
                    txt.writelines("\n")
            print(f"O cliente '{cpf_alterar}' foi alterado com sucesso!")

    @classmethod
    def remover_cliente(cls, cpf_remover):
        clientes_instances = DaoCliente.ler()
        busca_cpf = list(filter(lambda x: x.cpf == cpf_remover, clientes_instances))
        if len(busca_cpf) == 0:
            print(f"Falha ao remover o cliente '{cpf_remover}'! Não há nenhum cliente com esse cpf!")
        else:
            clientes_instances = list(filter(lambda x: x.cpf != cpf_remover, clientes_instances))
            with open('files/clientes.txt', 'w') as txt:
                for cliente_instance in clientes_instances:
                    txt.writelines(f"{cliente_instance.nome};{cliente_instance.cpf};{cliente_instance.telefone};{cliente_instance.email};{cliente_instance.endereco}")
                    txt.writelines("\n")
            print(f"O cliente '{cpf_remover}' foi removido com sucesso!")

    @classmethod
    def mostrar_clientes(cls):
        clientes_instances = DaoCliente.ler()
        if len(clientes_instances) == 0:
            print("A lista de clientes está vazia!")
        else:
            print("========== Clientes  ==========")
            for cliente_instance in clientes_instances:
                print(f"Nome: {cliente_instance.nome}\n"
                      f"CPF: {cliente_instance.cpf}\n"
                      f"Telefone: {cliente_instance.telefone}\n"
                      f"Email: {cliente_instance.email}\n"
                      f"Endereço: {cliente_instance.endereco}")
                print("-"*30)
