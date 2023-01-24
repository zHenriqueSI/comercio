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
                    print(f"Categoria '{categoria.categoria}' removida com sucesso!")
                    break

            with open('files/categorias.txt', 'w') as txt:
                for categoria in categorias_instances:
                    txt.writelines(f'{categoria.categoria}\n')

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
