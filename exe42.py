from time import sleep

#Entrada
nome = str(input("Qual é o seu nome?\n"))
print(f"{nome} hoje vamos comparar doi números inteiros escolhido por você")

#Dados
valor1 = int(input("digite o valor 1\n"))
valor2 = int(input("digite o valor 2\n"))


if valor1 > valor2:
    print("O primeiro valor é maior")

elif valor2 > valor1:
    print("O segundo número é maior")

elif valor1 == valor2:
    print(f"Não exite valor maior, os dois são iguais ")

#Saída
print("Muito obrigado")
sleep(20)