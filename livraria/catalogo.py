class Catalogo:

    def __init__(self, repositorio):
        self.repositorio = repositorio

    def buscar_por_titulo(self, titulo):
        return self.repositorio.buscar_por_titulo(titulo)

    def buscar_por_autor(self, autor):
        return self.repositorio.buscar_por_autor(autor)

    def filtrar_por_genero(self, genero):
        return self.repositorio.filtrar_por_genero(genero)

    def consultar_estoque(self, titulo):
        return self.repositorio.consultar_estoque(titulo)

    def listar_lancamentos(self):
        return self.repositorio.listar_lancamentos()