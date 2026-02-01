from time import sleep
nome = input("Qual é o seu nome?\n ")
print(f"Olá, seja bem-vinda(o) {nome}")

idade = int(input("Qual é a sua idade?\n"))

if idade >= 20:
    print(f"Sério? Calma idoso(a) de: {idade}")
else:
    print(f"Sério? Calma bebê de: {idade}")

peso = float(input("Qual é o seu peso?\n "))

if peso >= 70:
    print(f"Aloko! Vai com calma, com o {peso} kg, vai mudar a órbita da Terra!")
else:
    print(f"Aloko! Vai com calma raquítico(a), com esse {peso} kg você faz força para ficar de pé.")

altura = float(input("Qual é a sua altura? "))


if altura >= 1.80:
    print(f"Sério? Você está alto(a) em! Medindo essa altura: {altura} m, vai alcançar a Lua.")
else:
    print(f"Temos uma espécie de anão aqui! Com a altura de {altura} m, já é quase um anão.")
sleep(2)
