from datetime import datetime

#Lista de Alunos
listarAluno = []

#Função de Cadastro de Alunos
def cadastrarAluno():
 
    while True:

        #Informações que serão pedidas e adicionadas
        id = int(input("Digite o id do aluno:"))
        nome = input("Digite o nome do aluno:")
        dataNascimento = input("Digite a data de nascimento do aluno:")
        dataCadastro = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        #Dicionário dos alunos
        aluno = {"id":id,"nome":nome,"dataNascimento":dataNascimento,"dataCadastro":dataCadastro}

        #Puxando a função "consultaId" para verificar se o id é igual 
        if not consultaId(id):
            listarAluno.append(aluno)
        else:
           print("Id já está cadastrado!")
        
        #Comando para cadastrar mais de um aluno
        continuar = input("Desejas cadastrar mais algum aluno? (s/n)?")
        if continuar.lower() != "s":
            break
        print("Cadastro completo!")

#Função para verificar se o Id é igual
def consultaId(id):
   for l in listarAluno:
      if l["id"]== id:
         return True
      
#Função para exibir as informações adicionadas na lista     
def listaAluno():
   for l in listarAluno:
      print("______________________")
      print(l["id"])
      print(l["nome"])
      print(l["dataNascimento"])
      print(l["dataCadastro"])
      print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    