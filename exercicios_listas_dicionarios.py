# Exercícios de Listas e Dicionários

# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista_numeros = range(1,11)
for num in lista_numeros:
    print(f'{num}^2 = {num**2}')
print()

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista = ["Python", "Java", "C++", "JavaScript"]
lista.remove('C++')
lista.append('Ruby')
print(lista)
print()

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.
from typing import Dict, Any
livro: Dict[str, Any] = {'titulo': 'Factfullness', 'autor': 'Ronaldo Fenômeno', 'ano': 2017}
for col in livro:
    print(f'{col}: {livro[col]}')
print()

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Solução oficial
string = 'ROnaldo fenomeno'
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem
print(contar_caracteres(string.lower()))

# Solução alternativa
dicionario_contagem_caracteres = {}
for char in string.lower():
    if char not in dicionario_contagem_caracteres:
        dicionario_contagem_caracteres[char] = 1
    else:
        dicionario_contagem_caracteres[char] += 1
print(dicionario_contagem_caracteres)
print()

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
dicionario_precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# Solução oficial
preco_total = sum(dicionario_precos[item] for item in lista_compras)
print(preco_total)

# Solução alternativa
preco_total = 0
for item in lista_compras:
    if item in dicionario_precos.keys():
        preco_total += dicionario_precos[item]
print(preco_total)