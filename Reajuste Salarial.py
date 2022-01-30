Funcionário = str(input('Digite o nome do Funcionário: '))

sal = float(input(f'Digite o salário de {Funcionário} R$: '))

porcentagem = int(input('Digite a Porcentagem em que o Salário Recebera o aumento: '))

novosal = sal + (sal * porcentagem /100)

print(f'{Funcionário} que recebia {sal} Reais, com o aumento de {porcentagem}% agora ganha {novosal}')
input('Pressione Enter para encerrar o programa')
exit()