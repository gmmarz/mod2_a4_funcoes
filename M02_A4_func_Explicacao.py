#Aula de funções
#Quando for necessário passar alguma informação para a função, este valor é chamado de argumento da função.

#Exemplo de um exemplo para saudar
def saudar(nome):
    print("Bem vindo")
    print('Welcome')
    print('Bien venue')

nome = input('Digite seu nome: ')
saudar(nome)
frase = input('Digite uma frase: ')

#Dicas funções
#Nomeclatura - preferencialmente ter nomes verbais, que indicam bem o que a função está fazendo
#A função deve ter sua responsabilidade.
#Caso a validação dos dados esteja dentro da funcionalidade da função a validação pode ser feita na função