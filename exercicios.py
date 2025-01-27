
import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
'''
valor1 = int(input("digite valor 1: "))
valor2 = int(input("digite valor 2: "))
soma = valor1 + valor2
print(f"A soma é {soma}")
'''

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
'''
valor = int(input("insira um valor: "))
resto = valor % 5
print(f"O resto da divisão por 5 é {resto}")
'''

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
'''valor_1 =  int(input("insira o primeiro valor: "))
valor_2 =  int(input("insira o segundo valor: "))
multiplicacao = valor_1 * valor_2
print(f"O resultado da multiplicação é {multiplicacao}.")
'''

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)
'''

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''
numero = int(input("insira o primeiro numero: "))
quadrado = numero ** 2
print(f"O quadrado do número inserido é {quadrado}.")
'''

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''
num_1 = float(input("insira o primeiro número: "))
num_2 = float(input("insira o segundo número: "))
soma = num_1 + num_2
print(f"A soma dos números é {soma}.")
'''

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
'''
num_1 = float(input("insira o primeiro número: "))
num_2 = float(input("insira o segundo número: "))
media = (num_1 + num_2) / 2
print(f"A média dos números inseridos é {media}.")
'''

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
'''
numero = int(input("insira o numero: "))
potencia = int(input("insira a potencia: "))
resultado = numero ** potencia
print(f"O número {numero} elevado a potência {potencia} dá {resultado}.")
'''

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
'''
celsius = float(input("insira a temperatura em graus celsius (somente números): "))
fahr = (celsius * 9 / 5) + 32
print(f"A temperatura em fahrenheit é {fahr} oF")
'''

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
'''
nome = input("escreva seu nome: ")
caps = nome.upper()
print(f"seu nome em maiúsculas é {caps}.")
#print(f"seu nome em maiúsculas é {nome.upper()}.")
'''

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
'''
nome = input("insira seu nome completo: ")
minusc = nome.lower()
print(f"seu nome em minúsculas é {minusc}")
#print(f"seu nome em minúsculas é {nome.lower()}")
'''

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
'''
frase = input("escreva uma frase: ")
print(f'espacos inicial e final removidos na frase "{frase.strip()}."')
'''

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e,
# em seguida, imprima o dia, o mês e o ano separadamente.
'''
data = input("escreva a data no formato dd/mm/aaaa: ")
separado = data.split("/")
print(f"sua data é composta pelo dia {separado[0]}, mês {separado[1]} e ano {separado[2]}.")
'''
'''
# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")
'''

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''
frase_1 = input("escreva uma palavra: ")
frase_2 = input("escreva outra frase: ")
print(frase_1 + " " + frase_2)
'''

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#bole1 = input("insira um booleano: ")
#bole2= input("insira outro booleano: ")
#valor1 = bool(bole1)
#valor2 = bool(bole2)
#valor1 = bool(input("x: "))
#valor2 = True
#print(valor1, type(valor1))
#resultado =  (valor1 and valor2)
#print((valor1), type(bool(valor1)))
#print(valor2, type(valor2))
#print(f"o resultado de {bool(valor1)} AND {valor2} é: {resultado}.")
#print(resultado)

# Exemplo de entrada
'''
valor1 = False
valor2 = True
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)
'''

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
'''
valor1 = False
valor2 = False
resultado_OR = valor1 or valor2
print("Resultado do OR lógico:", resultado_OR)
'''


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

#     MÉTODO 1 DO GILSON:
'''
valor = input("insira um valor booleano: ")
# Converting string to boolean using eval
valor_bool = eval(valor)
valor_not_bool = not valor_bool
print("valor inserido:", valor_bool, type(valor_bool))
print("valor invertido:", valor_not_bool)
'''
'''
#     MÉTODO 2 DO GILSON (melhor opção):
valor = input("insira um valor booleano: ")
# Converting string to boolean using strip, lower and comparison with other string
valor_bool = valor.strip().lower() == "true"
valor_not_bool = not valor_bool
print("valor inserido:", valor_bool, type(valor_bool))
print("valor invertido:", valor_not_bool)
'''

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
'''
numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira outro número: "))
if numero1 == numero2:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")
'''

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira outro número: "))
print(f"Você digitou os números {numero1} e {numero2}.")
if numero1 != numero2:
    print("Os números são diferentes")
else:
    print("Os números são iguais")

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação