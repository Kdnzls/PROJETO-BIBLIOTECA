
listarEmprestimo = []
def emprestimo():
    while True:
        id = int(input("Digite o id do empréstimo:"))
        disponivel = input("O livro está disponível?\n(s/n):")

        if not consultaId(id):
            listarEmprestimo.append(emp)
        else:
          print("Id do empréstimo já está cadastrado!") 

        #Dicionário dos livros
        emp = {"id":id,"disponivel":disponivel}
        
        continuar = input("Desejas cadastrar mais algum empréstimo?\n(s/n):")
        if continuar.lower() != "s":
            break
            print("Cadastro completo")


def listaEmprestimo():
   for l in listarEmprestimo:
    print("______________________")
    print(l["id"])
    print(l["disponivel"])
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    



#Função para verificar se o Id é igual
def consultaId(id):
   for l in listarEmprestimo:
      if l["id"]==id:
         return True
      