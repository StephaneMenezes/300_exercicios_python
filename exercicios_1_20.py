#01 Criar tres exercicios com tres tipos de dados diferentes, respeitando sua sintaxe. 

nome:str= "Heitor"
idade:int = 18
altura:float = 1.75


#02 Crie um comentário de no máximo uma linha:

#03 Quando criamos comentários assim o codigo ignora essa linha de codigo.

''' Quando criamos comentários assim, o codigo le mas entender que n há nada para executar.
Isso nos permite criar comentários maiores, sem prejudicar a leitura do codigo.'''

#04 Escreva um programa que mostra a mensagem Ölá Mundo!""

print("Olá Mundo!")

#05 Crie uma variavel nome e atribuia para a mesma um nome digitado pelo usuário:

nome:str = input("Digite seu nome: ")

#06 Exiba em uma tela o valor e o tipo do dado da variavel num1: Sendo num1 = 1987

num1:int = 1987
print(type(num1))

print(num1)

#07 Peça para o usuário digitar um número e exiba o tipo do dado que foi digitado:

num2:int = (input("Digite um número: "))
print(f"O número digitado foi: {num2}." )

#08 Peça para que o usuário digite um numero e depois converta para float e exiba em tela tanto o numero em si quanto o seu tipo de dados. 


num3:int = (input("Digite um número: "))

num3_float:float = float(num3)

print(f"O número digitado foi: {num3_float} e o tipo de dado é: {type(num3_float)}")

#09 Digite uma lista com 5 nomes de pessoas:

nomes:list[str] = ["H[elio", "Maria", "João", "Ana", "Pedro"]
print(nomes)

#10 Mostre o tamanho da lista nomes / o número de elementos da lista nomes: Mostre separadamente apenas o terceiro elemento dessa lista:

len_nomes:int = len(nomes)
print(len_nomes)
print(nomes[3])

#11 e 12 Some os valores das variaveis num1 e num2. Sendo num1 = 52 e num2 = 106. Mostre o resultado da soma em tela:

def somar_num(a:int, b:int)->int:
    soma = a + b 
    print(f"Resultado de soma: {soma}")

somar_num(52,106)

#13 Subtraia os valores das variaveis num1 e num2. Sendo num1 = 52 e num2 = 106. Mostre o resultado da subtração em tela:

def subtrair_num(a:int, b:int)->int:
    resultado = a - b 
    print(f"Resultado de soma: {resultado}")

subtrair_num(52,106)

#14 Multiplique os valores das variaveis num1 e num2. Sendo num1 = 52 e num2 = 106. Mostre o resultado da multiplicação em tela:
def multiplicar_num(a:int, b:int)->int:
    resultado = a * b 
    print(f"Resultado de soma: {resultado}")

multiplicar_num(52,106)

#14.1 Divida os valores das variaveis num1 e num2. Sendo num1 = 52 e num2 = 106. Mostre o resultado da divisão em tela:

def dividir_num(a:int, b:int)->int:
    resultado = a / b 
    print(f"Resultado de soma: {resultado}")

dividir_num(52,106)

#15 Eleve o numero 58 a 8 oitava potencia:

num_elevado:int = 58 ** 8
print(num_elevado)

#16 Escreva um programa que peça para o usuário digitar dois números e mostre a soma, subtração, multiplicação e divisão desses dois números:
num_operacoes_basicas_1:int = (int(input("Digite o primeiro número: ")))
num_operacoes_basicas_2:int = (int(input("Digite o segundo número: ")))

def operacoes(num_1:int, num_2:int)->int:
    soma = num_1 + num_2
    subtracao = num_1 - num_2
    multiplicacao = num_1 * num_2
    divisao = num_1 / num_2
    print(f"Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}, Divisão: {divisao}")

operacoes(num_operacoes_basicas_1, num_operacoes_basicas_2)

#17 Dadas duas variaveis num 1 e num2, verifique se o valor de num1 é maior que o valor de num2. 

num1:int = 100
num2:int = 89

def verificar_se_maior(num1:int, num2:int)-> bool:
    print(num1 > num2)

verificar_se_maior(num1, num2)


# 18 Verificar se os dois valores são iguais:

def verificar_se_igual(num1:int, num2:int)-> bool:
    print(num1 == num2)

verificar_se_igual(num1, num2)

#19 Verificar se os valores sao diferentes:

def verificar_se_diferente(num1:int, num2:int)-> bool:
    print(num1 != num2)

verificar_se_diferente(num1, num2)

#20 Verificar se o valor de num1 é menor ou igual ao valor de num2:

def verificar_se_menor_igual(num1:int, num2:int)-> bool:
    print(num1 <= num2)

verificar_se_menor_igual(num1, num2)


