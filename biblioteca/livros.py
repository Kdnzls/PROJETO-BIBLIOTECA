from datetime import datetime

#Lista de Livros
listarLivros = []

#Função de Cadastro de Livros
def cadastrarLivro():

    while True:

        #Informações que serão pedidas e adicionadas
        id = int(input("Digite o id do livro:"))
        nome = input("Digite o nome do livro:")
        autor = input("Digite o nome do autor:")
        dataCadastro = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        dataAtualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        #Dicionário dos livros
        livro = {"id":id,"nome":nome,"autor":autor,"disponivel":True,"dataCadastro":dataCadastro,"dataAtualizacao":dataAtualizacao}
        
        #Puxando a função "consultaId" para verificar se o id é igual 
        if not consultaId(id):
            listarLivros.append(livro)
        else:
          print("Id do livro já está cadastrado!") 

        #Comando para cadastrar mais de um livro
        continuar = input("Desejas cadastrar mais algum livro? (s/n)?")
        if continuar.lower() != "s":
         break
         print("Cadastro completo!")

#Função para verificar se o Id é igual
def consultaId(id):
   for l in listarLivros:
      if l["id"]==id:
         return True
      
 #Função para exibir as informações adicionadas em lista
def listaLivro():
   for l in listarLivros:
    print("______________________")
    print(l["id"])
    print(l["nome"])
    print(l["autor"])
    print(l["dataCadastro"])
    print(l["dataAtualizacao"])
    if l["disponivel"]:
       print("disponível")
    else:
       print("indisponível")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    