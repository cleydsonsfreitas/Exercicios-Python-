from time import sleep
import math
#Entrada
nome = str(input("Olá jovem, qual é o seu nome?\n"))
print(f"{nome} hoje vamos pegar o angulo escolhido por você e mostrar seu seno, cosseno e tangente.")

#Dados
numero = int(input("Digite um ângulo em graus\n"))

#Resultado
angulo02 = numero * (math.pi / 180)
sen = math.sin(angulo02)
cos = math.cos(angulo02)
tan = math.tan(angulo02)

#Saida
print(f"O seno do númro {numero} é igual a {sen:.2f}")
print(f"O cossêno do númro {numero} é igual a {cos:.2f}")
print(f"A tangênte do númro {numero} é igual a {tan:.2f}")

sleep(20)
