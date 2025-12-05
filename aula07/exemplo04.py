# Dicionário
# Estrutura chave e valor
# Símbolo {}

# notas = {} # Dicionário vazio
# notas['Matemática'] = 8.5
# notas['Português'] = 7.0
# notas['História'] = 9.2
# notas['Historia'] = 9.2 # é sensível a qualquer diferença até letras maiúscula e minúscula
# del notas['História']
# notas['Matemática'] = 8.0 # para alterar o valor
# notas['Geografia'] = 9.9 # adicionar, basta incluir um nome e atribuir um valor

# print(notas)

# Cadastro em Dicionários

livros = {}
lista_cadastro = [] 

for i in range(3):
    titulo = input('Informe o título: ')
    autor = input('Informe o autor: ')
    genero = input('Informe o genero: ')
    ano = int(input('Informe o ano: '))

    livros = {
        'Título': titulo,
        'Autor': autor,
        'Genero': genero,
        'ano': ano,     
    }

    lista_cadastro.append(livros)
    print(f'Livro {i + 1} cadastrado')