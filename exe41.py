from time import sleep

#entrada
nome = str(input("Qual é o seu nome?\n"))
print(f"{nome} jaja vamos fazer as converções escolhidas por você")


#dados
recolhimento = int(input(f"{nome} escolhe qual converção você quer fazer. Digite:\n 1 para Binário\n 2 para octal\n 3 para hexadecimal\n"))
numero = int(input("Digite o numero inteiro\n"))

#Contas
numero_binario = bin(numero)
numero_octal = oct(numero)
numero_hexadecimal = hex(numero)

#Funções
if recolhimento == 1:
    print(f"Seu número em binario é igual a {numero_binario}")
elif recolhimento == 2:
    print(f"Seu número em octa é igual a {numero_octal}")
elif recolhimento == 3:
    print(f"Seu número em hexadecimal é igual a {numero_hexadecimal}")

#Saída
print(f"{nome} espero ter ajudado meu mano")

sleep(20)