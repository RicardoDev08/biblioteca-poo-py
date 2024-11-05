from livros import Livros
from usuario import Usuario
from biblioteca import Biblioteca
import mysql.connector

conexao = mysql.connector.connect(
    host='10.28.1.227',
    user='root',
    password='suporte',
    database='biblioteca'
)
cursor = conexao.cursor()

# cursor.execute('insert into livro(titulo,autor,genero,status_livro,codigo) values ("O Pequeno Principe","Ricardo","conto","Disponível",123);')
# conexao.commit()

# cursor.execute('delete from livro where id_livro=5;')
# conexao.commit()

# cursor.execute('update livro set  status_livro = "Indisponível" where id_livro= 2;')
# conexao.commit()

cursor.execute('select titulo from livro ;')
resultado=cursor.fetchall()
for i in resultado:
    print(resultado)

# print(vars(rafaela))

rafaela = Usuario('Rafaela','01223839020','67940028922')

dom_casmurro = Livros('Dom Casmurro','Machado de Assís','romance',1)
antares = Livros('Incidente em Antares','Érico Veríssimo','Ficção distópica',2)
poliana = Livros('Poliana','Eleanor H. Porter','Literatura infantil',3)
monica = Livros('Almanacão Da Turma Da Mônica','Maurício de Souza','Literatura infantil',4)

# print(vars(dom_casmurro))

# rafaela.pegar_emprestado(dom_casmurro)
# rafaela.pegar_emprestado(antares)
# rafaela.pegar_emprestado(monica)
# rafaela.pegar_emprestado(poliana)

# dom_casmurro.emprestar_livro(rafaela)
# antares.emprestar_livro(rafaela)
# monica.emprestar_livro(rafaela)
# poliana.emprestar_livro(rafaela)

#Metodo emprestar substitui as 8 linhas anteriores
Biblioteca.emprestar(rafaela, [dom_casmurro, poliana, monica, antares] )

# print(poliana.status)
# print(rafaela.lista_livros)
#print(vars(rafaela))
# print(vars(dom_casmurro))

saraiva = Biblioteca()

# print(dir(saraiva))
print(di)