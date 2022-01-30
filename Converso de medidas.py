medida = float(input('Digite uma distancia em metros: '))

dm = medida * 10

cm = medida * 100

mm = medida * 1000

dam = medida  / 10

hm = medida / 100

km = medida / 1000

print(f'{medida} metros equivale a {mm} milimetros \n {cm} centimetros \n {dm} Decimetros \n {dam} Decâmetros \n {hm} Hectômetros \n {km} Quilometros.')

input('Pressione Enter para fechar o programa')