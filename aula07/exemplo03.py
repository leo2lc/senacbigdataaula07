lista_numeros = []

for n in range(5):
    num = input('Informe o número: ')
    lista_numeros.append(num)

print(lista_numeros[0])
lista_numeros[0] = 22  # Altera o valor do índice zero
lista_numeros.pop() # Deleta o último ou o penúltimo se colocar -2 ou uma posição específica
lista_numeros.remove(30) # Deleta um valor específico
# del lista_numeros[0] # Deleta uma posição específica, mas esse não é um método da lista
lista_numeros.clear()
print(lista_numeros)