Preço = float(input('Digite o preço do Produto R$:'))

Desconto = int(input('Digite a porcentagem do desconto: '))

Resultado = Preço - (Preço * Desconto / 100)

print(f'O produto com desconto agora custa {Resultado:.2f}')
input('Pressione enter para fechar o programa')