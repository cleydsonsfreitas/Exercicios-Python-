from time import sleep
from math import sqrt, floor
entrada = str(input("Olá, tudo bem? Qual é o seu nome\n"))
print(f"Eai {entrada} vamos calcular a raiz quadrada de um número?")

numero = int(input("Digite um número\n"))

resultado = sqrt(numero)


print(f"Parabéns {entrada} a raiz quadrada do seu número é {resultado.__floor__()}")

sleep(20)