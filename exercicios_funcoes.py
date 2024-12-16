# Exercícios de Funções

# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def calcular_soma(lista: list) -> int:
    return sum(lista)
numeros = [1, 2, 2323, 2, 3, 4, 5]
print(calcular_soma(numeros))
print()

# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def verificar_numero_primo(num: int) -> bool:
    if num < 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True
    else:
        return True
for i in range(1, 26):
    if verificar_numero_primo(i) == True:
        print(f'{i} é primo')
print()

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def inverter_string(s: str) -> str:
    return s[::-1]
print(inverter_string('ronaldo fenomeno'))
print()

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar 
# todas as combinações de pares na lista que somem ao número dado.
def combinacao_de_pares(lista_numeros: list, num: int) -> list:
    pares = []
    for i in range(len(lista_numeros)):
        for j in range(i + 1, len(lista_numeros)):
            if lista_numeros[i] + lista_numeros[j] == num:
                pares.append((lista_numeros[i], lista_numeros[j]))
    return pares
print(combinacao_de_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
print()

# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
def ordenar_chaves_dicionario(d: dict) -> list:
    lista_ordenada = list(d.keys())
    lista_ordenada.sort()
    return sorted(d.keys())
dicionario = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
print(ordenar_chaves_dicionario(dicionario))

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Testes para função 1
assert calcular_soma([1, 2, 3, 4, 5]) == 15
assert calcular_soma([]) == 0
assert calcular_soma([-1, 1]) == 0

# Testes para função 2
assert eh_primo(1) == True
assert eh_primo(4) == False
assert eh_primo(17) == True

# Testes para função 3
assert inverter_string("python") == "nohtyp"
assert inverter_string("") == ""
assert inverter_string("a") == "a"

# Testes para função 4
assert combinacao_de_pares([1, 2, 3, 4, 5], 7) == [(2, 5), (3, 4)]
assert combinacao_de_pares([1, 2, 3], 10) == []

# Testes para função 5
assert ordenar_chaves_dicionario({'c': 3, 'a': 1, 'b': 2}) == ['a', 'b', 'c']
assert ordenar_chaves_dicionario({}) == []