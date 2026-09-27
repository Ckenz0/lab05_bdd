from behave import given, when, then

from livraria.catalogo import Catalogo
from livraria.repositorio import RepositorioLivros


@given("que existem livros cadastrados no catálogo")
def step_livros_cadastrados(context):

    livros = [
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "genero": "Distopia",
            "estoque": 3,
            "lancamento": False
        },
        {
            "titulo": "A Revolução dos Bichos",
            "autor": "George Orwell",
            "genero": "Distopia",
            "estoque": 2,
            "lancamento": False
        },
        {
            "titulo": "O Hobbit",
            "autor": "J.R.R. Tolkien",
            "genero": "Fantasia",
            "estoque": 5,
            "lancamento": False
        },
        {
            "titulo": "O Novo Reino",
            "autor": "Ana Silva",
            "genero": "Fantasia",
            "estoque": 4,
            "lancamento": True
        }
    ]

    repositorio = RepositorioLivros(livros)

    context.catalogo = Catalogo(repositorio)


@when('eu buscar pelo título "{titulo}"')
def step_buscar_titulo(context, titulo):
    context.resultado = context.catalogo.buscar_por_titulo(titulo)


@then('o livro "{titulo}" deve ser retornado')
def step_verificar_livro(context, titulo):
    assert len(context.resultado) == 1
    assert context.resultado[0]["titulo"] == titulo


@when('eu buscar pelo autor "{autor}"')
def step_buscar_autor(context, autor):
    context.resultado = context.catalogo.buscar_por_autor(autor)


@then("devem ser retornados {quantidade:d} livros")
def step_quantidade_livros(context, quantidade):
    assert len(context.resultado) == quantidade


@then("nenhum livro deve ser retornado")
def step_nenhum_livro(context):
    assert context.resultado == []


@when('eu consultar a disponibilidade do livro "{titulo}"')
def step_consultar_estoque(context, titulo):
    context.resultado = context.catalogo.consultar_estoque(titulo)


@then("devem ser informados {quantidade:d} exemplares disponíveis")
def step_verificar_estoque(context, quantidade):
    assert context.resultado == quantidade


@when('eu filtrar os livros pelo gênero "{genero}"')
def step_filtrar_genero(context, genero):
    context.resultado = context.catalogo.filtrar_por_genero(genero)


@then('devem ser retornados apenas livros do gênero "{genero}"')
def step_verificar_genero(context, genero):

    assert len(context.resultado) > 0

    for livro in context.resultado:
        assert livro["genero"] == genero


@when("eu consultar os lançamentos da semana")
def step_consultar_lancamentos(context):
    context.resultado = context.catalogo.listar_lancamentos()


@then("deve ser retornado {quantidade:d} lançamento")
def step_verificar_lancamentos(context, quantidade):
    assert len(context.resultado) == quantidade