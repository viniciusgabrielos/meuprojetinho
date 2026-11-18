class Livro:
    def __init__(self, livro: str, autor: str,codigo:str):
        self.livro = livro
        self.autor=autor
        self.codigo=codigo
        self.disponivel = True