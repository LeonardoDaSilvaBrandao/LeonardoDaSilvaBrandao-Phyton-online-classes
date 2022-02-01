from random import shuffle

n1 = str(input('Digite o primeiro item da lista: '))
n2 = str(input('Digite o segundo item da lista: '))
n3 = str(input('Digite o terceiro item da lista: '))
n4 = str(input('Digite o quarto item na lista: '))

lista = [n1, n2, n3, n4]
shuffle(lista)

print(f'A ordem gerada foi')
print(lista)