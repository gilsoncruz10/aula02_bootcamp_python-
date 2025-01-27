
# #### try-except e if

# 4a. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
try:
    numero_01 = int(input("Inserir um numero inteiro: "))
    numero_02 = int(input("Inserir outro numero inteiro: "))
    resultado = numero_01 // numero_02
    print(f"O resultado da divisão entre {numero_01} e {numero_02} é {resultado}.")
    print(f"Ou seja: {numero_01} / {numero_02} = {resultado}")
except ZeroDivisionError as e:
    print("Não é possível dividir por zero. Tente outro divisor.")
    print(e)
except ValueError as e:
    print("Você não inseriu um dado válido.")
    print(e)
except KeyboardInterrupt as e:
    print("Acho que você não quis digitar isso.")
    print(e)
else:
    print("Divisão realizada com sucesso!")
finally:
    print("O importante é tentar!!!!")
'''


# ##### IF ISISNTANCE

# 4b. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero1 = input("Insira um número: ")
if isinstance(numero1, int):
    print("a variável é um inteiro")
else:
    print("a variável não é um inteiro")