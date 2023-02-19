import controller

controller.ControllerGeral.criar_arquivos('categorias.txt', 'clientes.txt', 'estoques.txt', 'fornecedores.txt', 'funcionarios.txt', 'vendas.txt')


if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar [ Categorias ]\n"
                          "Digite 2 para acessar [ Estoque ]\n"
                          "Digite 3 para acessar [ Fornecedor ]\n"
                          "Digite 4 para acessar [ Cliente ]\n"
                          "Digite 5 para acessar [ Funcionario ]\n"
                          "Digite 6 para acessar [ Vendas ]\n"
                          "Digite 7 para gerar o relatorio de vendas\n"
                          "Digite 8 para sair\n"))

        if local == 1:
            cat = controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    categoria_cadastrar = input("Digite a categoria que deseja cadastrar: ")
                    cat.cadastrar_categoria(categoria_cadastrar)
                elif decidir == 2:
                    categoria_remover = input("Digite a categoria que deseja remover: ")
                    cat.remover_categoria(categoria_remover)
                elif decidir == 3:
                    categoria_alterar = input("Digite a categoria que deseja alterar: ")
                    nova_categoria = input("Digite a categoria para qual deseja alterar: ")
                    cat.alterar_nome_categoria(categoria_alterar, nova_categoria)
                elif decidir == 4:
                    cat.mostrar_categorias()
                else:
                    break

        elif local == 2:
            cat = controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para ver o estoque\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do produto: ")
                    preco = input("Digite o preco do produto: ")
                    categoria = input("Digite a categoria do produto: ")
                    quantidade = input("Digite a quantidade do produto: ")
                    cat.cadastrar_produto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto_remover = input("Digite o produto que deseja remover: ")
                    cat.remover_produto(produto_remover)
                elif decidir == 3:
                    nome_alterar = input("Digite o nome do produto que deseja alterar: ")
                    novo_nome = input("Digite o novo nome do produto: ")
                    novo_preco = input("Digite o novo preco do produto: ")
                    nova_categoria = input("Digite a nova categoria do produto: ")
                    nova_quantidade = input("Digite a nova quantidade do produto: ")
                    cat.alterar_produto(nome_alterar, novo_nome, novo_preco, nova_categoria, nova_quantidade)
                elif decidir == 4:
                    cat.mostrar_produtos()
                else:
                    break

        elif local == 3:
            cat = controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar fornecedores\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do fornecedor: ")
                    cnpj = input("Digite o cnpj do fornecedor: ")
                    telefone = input("Digite o telefone do fornecedor: ")
                    categoria = input("Digite a categoria do fornecedor: ")
                    cat.cadastrar_fornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    fornecedor_remover = input("Digite o cnpj do fornecedor que deseja remover: ")
                    cat.remover_fornecedor(fornecedor_remover)
                elif decidir == 3:
                    cnpj_alterar = input("Digite o cnpj do fornecedor que deseja alterar: ")
                    novo_nome = input('Digite o novo nome do fornecedor: ')
                    novo_cnpj = input('Digite o novo cnpj do fornecedor: ')
                    novo_telefone = input('Digite o novo telefone do fornecedor: ')
                    nova_categoria = input('Digite a nova categoria fornecida: ')
                    cat.alterar_fornecedor(cnpj_alterar, novo_nome, novo_cnpj, novo_telefone, nova_categoria)
                elif decidir == 4:
                    cat.mostrar_fornecedores()
                else:
                    break

        elif local == 4:
            cat = controller.ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar clientes\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do cliente: ")
                    cpf = input("Digite o cpf do cliente: ")
                    telefone = input("Digite o telefone do cliente: ")
                    email = input("Digite o email do cliente: ")
                    endereco = input("Digite o endereço do cliente: ")
                    cat.cadastrar_cliente(nome, cpf, telefone, email, endereco)
                elif decidir == 2:
                    cliente = input("Digite o cpf do cliente que deseja remover: ")
                    cat.remover_cliente(cliente)
                elif decidir == 3:
                    cpf_alterar = input("Digite o nome do cliente que deseja alterar: \n")
                    novo_nome = input("Digite o novo nome do cliente: \n")
                    novo_cpf = input("Digite o novo cpf do cliente: \n")
                    novo_telefone = input("Digite o novo telefone do cliente: \n")
                    novo_email = input("Digite o novo email do cliente: \n")
                    novo_endereco = input("Digite o novo endereço do cliente: \n")
                    cat.alterar_cliente(cpf_alterar, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco)
                elif decidir == 4:
                    cat.mostrar_clientes()
                else:
                    break

        elif local == 5:
            cat = controller.ControllerFuncionario()
            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionario\n"
                                    "Digite 2 para remover um funcionario\n"
                                    "Digite 3 para alterar um funcionario\n"
                                    "Digite 4 para mostrar funcionarios\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do funcionario: ")
                    cpf = input("Digite o cpf do funcionario: ")
                    telefone = input("Digite o telefone do funcionario: ")
                    email = input("Digite o email do funcionario: ")
                    endereco = input("Digite o endereço do funcionario: ")
                    modelo_trabalho = input("Digite o modelo de trabalho do funcionario: ")
                    cat.cadastrar_funcionario(nome, cpf, telefone, email, endereco, modelo_trabalho)
                elif decidir == 2:
                    funcionario_remover = input("Digite o cpf do funcionario que deseja remover: ")
                    cat.remover_funcionario(funcionario_remover)
                elif decidir == 3:
                    cpf_alterar = input("Digite o cpf do funcionario que deseja alterar: ")
                    novo_nome = input("Digite o novo nome do funcionario: ")
                    novo_cpf = input("Digite o novo cpf do funcionario: ")
                    novo_telefone = input("Digite o novo telefone do funcionario: ")
                    novo_email = input("Digite o novo email do funcionario: ")
                    novo_endereco = input("Digite o novo endereço do funcionario: ")
                    novo_modelo_trabalho = input("Digite o novo modelo de trabalho do funcionario: ")
                    cat.alterar_funcionario(cpf_alterar, novo_nome, novo_cpf, novo_telefone, novo_email, novo_endereco, novo_modelo_trabalho)

                elif decidir == 4:
                    cat.mostrar_funcionarios()
                else:
                    break

        elif local == 6:
            cat = controller.ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para realizar uma venda\n"
                                    "Digite 2 para ver as vendas\n"
                                    "Digite 3 para sair\n"))

                if decidir == 1:
                    nome = input('Digite o nome do produto: ')
                    vendedor = input('Digite o cpf do vendedor: ')
                    comprador = input('Digite o cpf do cliente: ')
                    quantidade = int(input('Digite a quantidade vendida: '))
                    cat.cadastrar_venda(nome, vendedor, comprador, quantidade)
                elif decidir == 2:
                    data_inicio = input("Digite a data de inicio no formato dia-mes-ano: ")
                    data_termino = input("Digite a data de termino no formato dia-mes-ano: ")
                    cat.mostrar_vendas(data_inicio, data_termino)
                else:
                    break

        elif local == 7:
            a = controller.ControllerVenda()
            a.gerar_relatorio()
        else:
            break
