Real = float(input('Digite um valor em Reais para conversão: '))

DO = (Real * 5.40)

EU = (Real * 6.11)

Op = int(input('Digite 1 para fazer a conversão em dolar e 2 para fazer a conversão em Euro: '))

if Op==1:
    print(f'{Real} Reais Equivale a {DO} Dólares')
    input('Pressione enter para encerrar o programa')
    exit()

elif Op==2:
    print(f'{Real} Reais equivale a {EU} Euros')
    input('Pressione enter para encerrar o programa.')
    exit()

else:
    print('Esta opção é inválida.')
    input('Pressione Enter para encerrar o programa.')
    exit()