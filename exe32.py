from time import sleep
import random

#Entrada
nome = str(input("Qual é o seu nome player\n"))
print(f"Muito bem {nome} Hoje vamos desafiar você contra o comptador")
print(f"O computado vai escolher um número entre 0 e 5 e você tem que adivinhar qual ele escolheu")
print(f"vamos ver quem ganha essa?")
numero = int(input("Escolha um número entre 0 e 5\n"))

#Resolução
lista = [0,1,2,3,4,5]
resultado = random.choice(lista)

if numero == resultado:
    print(f"Parabens {nome} você ganhou dessa vez")
else:
    print(f"Descepicionante cara {nome} mais sorte da próxima vez monkey")

#Saída
print(f"Muito obrigado meu parceiro até a proxima AAAAAA {nome} para de ser burro")

sleep(20)

