#Biblioteca Digital

#Menu da biblioteca
from alunos import cadastrarAluno, listaAluno, listarAluno
from autores import cadastrarAutor, listaAutor, listarAutores
from livros  import cadastrarLivro, listaLivro, listarLivros

#Função para exibir o menu
def menu():
  while True:
    print("1. Cadastrar aluno ")
    print("2. Cadastrar autor ")
    print("3. Cadastrar livro ")
    print("4. Cadastrar emprestimo")
    print("5. Listar aluno ")
    print("6. Listar autor ")
    print("7. Listar livro ")
    print("8. Listar emprestimo")
    print("9. Exclusão")
    print("10. Sair ")

    #Variável para exibir e selecionar as funções
    op = int(input("Digite a opção desejada: "))

    #Selecionando as funções e puxando as funções 
    if op == 1:
      print("Cadastrar aluno")
      cadastrarAluno()
    elif op ==2:
      print("Cadastrar autor")
      cadastrarAutor()
    elif op ==3:
      print("Cadastrar livro")
      cadastrarLivro()
    elif op ==4:
      print("Cadastrar emprestimo")
    elif op ==5:
      print("Listar aluno")
      listaAluno()
    elif op ==6:
      print("Listar autor")
      listaAutor()
    elif op ==7:
       print("Listar livro")
       listaLivro()
    elif op ==8:
      print("Listar emprestimo")
    elif op ==9:
      print("Exclusão")
    elif op ==10:
      print("Saindo...")
      break
    else:
      print("Opção invalida")
menu()