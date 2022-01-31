from random import choice
n1 = str(input('Digite o primeiro item da lista: '))
n2 = str(input('Digite o segundo item da lista: '))
n3 = str(input('Digite o terceiro item da lista: '))
n4 = str(input('Digite o quarto item da lista: '))
lista = [n1, n2, n3, n4]
escolhido = choice (lista)
print(f'O item escolhido foi {escolhido}')