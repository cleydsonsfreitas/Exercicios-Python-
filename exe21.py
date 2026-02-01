from time import sleep
from math import sqrt

#Entrada
nome = str(input("Olá jovem, Qual é o seu nome?\n"))
print(f"Muito bem {nome} hoje vamos calcular o valor da hipotenusa de um número")
print("Para isso precisaremos que você digíte os valores para calcularmos")

#Colhendo dados
adj = float(input("Qual é o valor do cateto adjacente?"))
opt = float(input("Qual é o valor do cateto oposto?"))

#Conta
resultado = (opt**2) + (adj**2)
resultado02 = sqrt(resultado)

#Saída
print(f"Parabens o valor da Hipotenusa é igual a:  {resultado02:.3f}")

sleep(20)