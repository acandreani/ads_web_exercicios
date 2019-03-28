
def recebe_registro():
    a={}
    a["cpf"]=input("cpf:")
    a["idade"]=input("idade:")
    a["sexo"]=input("sexo:")
    a["estado"]=input("estado:")
    a["nome"]=input("nome:")
    return a

n=int(input("num. de registros: "))

contatos={}
while n>0:
    a=recebe_registro()
    contatos[a["cpf"]]=a
    print("\n")
    n=n-1

b=input("busca por cpf :")

print(contatos[b])
