# Lista de fruta
frutas = ['Maracuja', 'Maçã', 'Laranja', 'Banana', 'Uva', 'Abacaxi']

# exibe lista e os indices
for i in range(len(frutas)):
    print(f'Frutas de indice {i}: {frutas[i]},')

# usuario informa o indice do item 
indice = int(input('Informe o indice do item que deseja separar: '))

#separa o item 
fruta = frutas.pop(indice)

#exibe o item separado
print(fruta)