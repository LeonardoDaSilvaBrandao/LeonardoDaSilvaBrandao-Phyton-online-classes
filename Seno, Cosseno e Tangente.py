from math import sin, cos, tan, radians
an = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(an))
print(f'O angulo de {an} tem o Seno de {seno}')
cosseno = cos(radians(an))
print(f'O angulo de {an} tem o cosseno de {cosseno}')
tangente = tan(radians(an))
print(f'O angulo de {an} tem o tangente de {tangente}')
input('Pressione ENTER para fechar o programa.')