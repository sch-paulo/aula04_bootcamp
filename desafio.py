# Desafio - Refatorar nosso código usando Dicionário, Type Hint e Funcões.
def verificar_e_adicionar_funcionario() -> dict:
    nome_bool: bool = False
    salario_bool: bool = False
    bonus_bool: bool = False
    adicionar_mais_funcionarios_bool: bool = True
    num_funcionario = 1
    dicionario = {}
    
    while adicionar_mais_funcionarios_bool:
        while nome_bool == False:
            # dicionario[f'funcionario_{num_funcionario}'] = {}
            nome: str = input('Qual o seu nome? ').strip().capitalize()
            if len(nome) == 0:
                print('Você não digitou nada')
            elif any(caracter.isdigit() for caracter in nome):
                resposta = input('Você inseriu dígitos no seu nome, tem certeza que está correto? (S/N) ').lower()
                if resposta == 's':
                    dicionario[f'funcionario_{num_funcionario}'] = {'nome': nome}
                    nome_bool = True
            else:
                dicionario[f'funcionario_{num_funcionario}'] = {'nome': nome}
                nome_bool = True

        while salario_bool == False and bonus_bool == False:
            try:
                salario: float = float(input('Qual o seu salário mensal? '))
                bonus: float = float(input('E o percentual do seu bônus recebido? '))
                if salario <= 0 or bonus <= 0:
                    print('O valor do salário e/ou bônus não pode ser zero ou negativo.')
                else:
                    dicionario[f'funcionario_{num_funcionario}']['salario'] = salario
                    dicionario[f'funcionario_{num_funcionario}']['percent_bonus'] = bonus
                    dicionario[f'funcionario_{num_funcionario}']['bonus'] = round(1000 + salario * bonus,2)
                    salario_bool = True
                    bonus_bool = True
            except ValueError:
                print('Insira um valor numérico.')
            except NameError:
                print('Insira um valor.')
        
        adicionar_mais_funcionarios = input('Deseja adicionar mais funcionários? (S/N) ').lower()
        if adicionar_mais_funcionarios == 's':
            nome_bool, salario_bool, bonus_bool = False, False, False
            num_funcionario += 1
        else:
            adicionar_mais_funcionarios_bool = False
    return dicionario
 
dicionario_funcionarios = verificar_e_adicionar_funcionario()
print(dicionario_funcionarios)