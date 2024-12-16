# Exercicios intermediários e mais avançados

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com", "manager@example.com", "manager@example.com"]
emails_nao_duplicados = list(set(emails))
print(emails_nao_duplicados)
print()

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
lista_idades = [12, 15, 22, 29, 38, 44, 60, 75, 80, 99]
idades_mais_18 = [idade for idade in lista_idades if idade >= 18]
print(idades_mais_18)
print()

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Ronaldo", "idade": 32},
    {"nome": "Roberto", "idade": 38},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])
print(pessoas)
print()

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
conjunto_numerico = [23, 245, 2323, 2, 10, -230, 8]
media = round(sum(conjunto_numerico) / len(conjunto_numerico),2)
print(media)
print()

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
lista_valores = [23, 245, 2323, 2, 10, 0, -230, 8]
lista_pares = [num for num in lista_valores if num % 2 == 0]
lista_impares = [num for num in lista_valores if num % 2 != 0]
print(lista_pares)
print(lista_impares)
print()

# Exercícios com Dicionários

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]
produto_atualizado = 'Mouse'
novo_preco = 100
for item in produtos:
    if item['nome'] == produto_atualizado:
        item['preço'] = novo_preco
print(produtos)
print()

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}
# Solução oficial
dicionario_completo = {**dicionario1, **dicionario2}
print(dicionario_completo)

# Solução alternativa
dicionario_completo = dicionario1.copy()
for key, value in dicionario2.items():
    dicionario_completo[key] = value
print(dicionario_completo)
print()

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque_produtos = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
estoque_validos = {key: value for key, value in estoque_produtos.items() if value > 0}
print(estoque_validos)
print()

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
lista_chaves = list(dicionario.keys())
lista_valores = list(dicionario.values())
print(lista_chaves)
print(lista_valores)
print()

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
string = 'ronaldo fenomeno'
dicionario_contagem = {}
for caractere in string.lower():
    dicionario_contagem[caractere] = dicionario_contagem.get(caractere, 0) + 1
print(dicionario_contagem)