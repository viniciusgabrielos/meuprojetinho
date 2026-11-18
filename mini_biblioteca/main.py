from src.bibliotequinha.emprestimos import Emprestimo
from src.bibliotequinha.livros import Livro
from src.bibliotequinha.usuarios import Usuario

usuario1 = Usuario("Jayr","1")
livro1 = Livro("As aventuras do garoto Jayr","Vinícius","1")
emprestimo1 = Emprestimo(livro1,usuario1)
emprestimo1.devolver()
print(f"Estado do livro: {emprestimo1.livro.disponivel}")

print(f"Estado do empréstimo: {emprestimo1.ativo}")
