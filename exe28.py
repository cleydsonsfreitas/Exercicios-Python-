from time import sleep

#Entrada
nome = str(input("Fala fela da puta, qual é o seu nome?\n"))
print(f"{nome} hoje o exercicio é simples, você tem que acertar o nome de uma cidade")

#Dados
print("Dica")
print("A cidade é um time de futebol com 3 libertadores")
recolher_dado = str(input("Digite um nome de cidade com a primeira letra maiuscula, caso acerte é 1 caso contrario 0\n")).strip()

#Resultado
print( recolher_dado[:6].upper() == "Santos")

sleep(20)''