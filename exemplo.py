class ContextoSimples:

    def __enter__(self):
        print("Iniciar conexao")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando conexao com seguranca")

with ContextoSimples() as cs:
    print("Execucoes no banco de dados")