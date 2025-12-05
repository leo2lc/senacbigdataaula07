# Pegar as notas de 5 estudantes e 
# Verificar se cada um teve uma nota maior que 7 que é o mínimo para ser aprovado

lista_notas = []

for e in range(5):
    num = float(input('Digite a nota: '))
    lista_notas.append(num)

print(lista_notas)

for n in lista_notas:
    if n >= 70:
        print('Aprovado')
    else:
        print('Reprovado')
    print(n)

