from time import sleep
#Entrada
print("Salve cachorro caramelo, vamos analisar seu nome")

#Dados
nome = str(input("Qual é o seu nome completo?\n")).strip().split()
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu ultimo nome é {nome[len(nome)-1]}")
sleep(20)