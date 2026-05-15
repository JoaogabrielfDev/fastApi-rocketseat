#Pydantic => lib que valida e faz conversao de tipo feito em rust
from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    idade: int 
    ativo: bool = True


try:
    usuario = Usuario(nome = "Joao", idade=21)
    print(usuario)
    print(usuario.idade)
    print(type(usuario.idade))
except Exception as e:
    print("erro de validacao")
    print(e)