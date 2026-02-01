from time import sleep

#entrada
nome = str(input("Fala felas, qual é o seu nome?\n"))
print(f"{nome} vamos jogar Jokenpo?")
print("você digita Pedra or papel or tisoura")
print("Vamos lá")

#dados
mao = str(input("Você escolhe pedra, papel ou tesoura?\n"))

#função
if mao == "pedra":
    print(f"Eu escolho papel")

elif mao == "papel":
    print("Eu escolho tesoura")

elif mao == "tesoura":
    print("Eu escolho pedra")

print(f"{nome} foi bom jogar com você")

sleep(20)