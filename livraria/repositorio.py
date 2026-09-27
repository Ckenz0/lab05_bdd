class RepositorioLivros:

    def __init__(self, livros=None):
        self.livros = livros or []

    def buscar_por_titulo(self, titulo):

        return [
            livro
            for livro in self.livros
            if livro["titulo"].lower() == titulo.lower()
        ]

    def buscar_por_autor(self, autor):

        return [
            livro
            for livro in self.livros
            if livro["autor"].lower() == autor.lower()
        ]

    def consultar_estoque(self, titulo):

        livros_encontrados = self.buscar_por_titulo(titulo)

        if not livros_encontrados:
            return 0

        return livros_encontrados[0]["estoque"]

    def filtrar_por_genero(self, genero):

        return [
            livro
            for livro in self.livros
            if livro["genero"].lower() == genero.lower()
        ]

    def listar_lancamentos(self):

        return [
            livro
            for livro in self.livros
            if livro["lancamento"]
        ]