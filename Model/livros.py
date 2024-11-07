class Livros():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro

        self.status = "Disponivel"
        self.usuario = None

<<<<<<< HEAD:Model/livros.py
    def emprestar_livro(self, usuario):
        if self.status != 'Disponivel':
            return       

        self.usuario = usuario.nome
        self.status = 'Emprestado'
        
    def devolver_livro(self):
        if self.status != 'Emprestado':
            return 'Não pode ser devolvido!'
        
        self.usuario = None
        self.status = 'Disponivel'

    def create(self):
        return f'insert into livro(titulo,autor,genero,status_livro,cod_livro) values ("{self.titulo}","{self.autor}","{self.genero}","{self.cod_livro}");'
=======
    def create(self):
        return 'insert into livro(titulo, autor, genero) values()'


>>>>>>> 13d68ccfed77228671eb132260a324f58a48e037:livros.py
    
    def read(self,cod_livro):
        return f'select * titulo from livro where cod_livro = 4 {self.cod_livro};'
    
    # def delete(self):
    #     return f'delete from livro where titulo= "Dom Casmurgo";'
  
    
    # def update(self):
    #     return f'update livro set autor = "Ricardo" where autor= Machado de Assis;'
