class Biblioteca:
    @staticmethod
    def emprestar(livro, usuario):
        livro.emprestar_livro(usuario);
        usuario.pegar_emprestado(livro);        
    
    @staticmethod
    def devolver(livro, usuario):
        livro.devolver_livro(usuario)
        usuario.devolver_emprestimo(livro)

    @staticmethod
    def cadastrar_livro(livro):
        pass

    @staticmethod
    def cadastrar_usuario(usuario):
        pass