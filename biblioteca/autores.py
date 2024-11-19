from datetime import datetime

#Lista de Autores
listarAutores = []

#Função de Cadastro de Autores
def cadastrarAutor():
    
    while True:

        #Informações que serão pedidas e adicionadas
        id = int(input("Digite o id do autor:"))
        nome = input("Digite o nome do autor:")
        dataNascimento =int(input("Digite a data de nascimento do autor:"))
        dataCadastro = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        #Dicionário dos autores
        autor = {"id":id,"nome":nome,"dataNascimento":dataNascimento,"dataCadastro":dataCadastro}

        #Puxando a função "consultaId" para verificar se o id é igual 
        if not consultaID(id):
            listarAutores.append(autor)
        else:
           print("Id do autor já cadastrado!")

         #Comando para cadastrar mais de um autor
        continuar = input("Desejas cadastrar mais algum autor? (s/n)?")
        if continuar.lower() != "s":
         break
    print("Cadastro completo!")

#Função para verificar se o Id é igual
def consultaID(id):
   for l in listarAutores:
      if l["id"]== id:
         return True

#Função para exibir as informações adicionadas na lista   
def listaAutor():
   for l in listarAutores:
      print("______________________")
      print(l["id"])
      print(l["nome"])
      print(l["dataNascimento"])
      print(l["dataCadastro"])
      print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    



