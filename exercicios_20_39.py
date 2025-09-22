#Verifique se o valor de num1 é menor igual a 100. 

num1:int = 100
num2: int = 89 

if num1 <= 100:
    print(f"O valor de num1 é menor ou igual a 100: {num1}")    
else:
    print(f"O valor de num1 é maior que 100: {num1}")


#21 Verifique se os valores de num1 e num2 são menores ou iguais a 100.


if num1 <= 100 and num2 <= 100:
    print(f"Os valores de num1 e num2 são menores ou iguais a 100: {num1} e {num2}")

else:
    print(f"Um dos valores é maior que 100: {num1} e {num2}")


#22 Verifique se os valores de num1 OU num2 são menores ou iguais a 100.

if num1 >= 100 or num2 >= 100:
    print(f"Os valores de num1 e num2 são menores ou iguais a 100: {num1} e {num2}")

else:
    print(f"Um dos valores é maior que 100: {num1} e {num2}")


#23 Verificar se um valor esta dentro de uma lista: 

num1: int = 20

lis1 = [10, 300, 50, 89, 34] 

if num1 in lis1:
    print(f"O valor {num1} está na lista {lis1}")
else:
    print(f"O valor {num1} não está na lista {lis1}")

# Teste: 

# nom: str = "Stephane"

nom = input("Digite seu nome: ")

nom = nom.capitalize()

print(nom)

list_convite = ["Ana", "Stephane", "Maria", "João"]

if nom in list_convite:
    print(f"{nom}, você está convidado(a) para a festa!")
else:
    print(f"{nom}, você não está convidado(a) para a festa.")



# Crie duas variaveis num1 e num2, com valores numericos digitiados pelo usuario. E caso o valor de num1 seja maior ou igual ao valor de num2, exiba a mensagem: "O valor de num1 é maior ou igual ao valor de num2". Caso contrario, exiba a mensagem: "O valor de num1 é menor que o valor de num2".

num1:int = int(input("Digite um valor numerico para num1: "))
num2:int = int(input("Digite um valor numerico para num2: "))


if num1 >= num2:
    print(f"O valor de num1 é maior ou igual ao valor de num2")

else: 
    print(f"O valor de num1 é menor que o valor de num2")




