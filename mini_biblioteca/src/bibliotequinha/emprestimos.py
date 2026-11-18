from .livros import Livro
from .usuarios import Usuario

class Emprestimo:

    
    def __init__(self,livro: Livro, usuario: Usuario):

        self.livro = livro
        if self.livro.disponivel == False:
            raise ValueError("Livro indisponível")

        self.usuario = usuario
        self.ativo = True
        
    
    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True