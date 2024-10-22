from biblioteca import Biblioteca
from livros import Livro
from usuario import Usuario

caique = Usuario("Caique Fernandes", "111.111.111-11", "67 99305-6767")

domCasmurro = Livro("Dom Casmurro", "Machado de Assis", "Romance", "231623817")
oPrincipe = Livro("O Principe", "Maquiavel", "Ficção", "8712374")
aRevolucaoDosBichos = Livro("A Revolução dos Bichos", "George Orwell", "Ficção", "7419842")

Biblioteca.emprestar(domCasmurro, caique)
Biblioteca.emprestar(oPrincipe, caique)
Biblioteca.emprestar(aRevolucaoDosBichos, caique)