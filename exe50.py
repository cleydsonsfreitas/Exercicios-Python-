from time import sleep
import random

#entrada
nome = str(input("Fala felas, qual é o seu nome?\n"))
print(f"{nome} vamos jogar Jokenpo?")
print("você digita pedra or papel or tisoura")
print("Vamos lá")

#dados
mao = str(input("Você escolhe pedra, papel ou tesoura?\n"))

lista = ["pedra", "papel", "tesoura"]

escolha = random.choice(lista)

print(f"Minha escolha é {escolha}")

sleep(20)