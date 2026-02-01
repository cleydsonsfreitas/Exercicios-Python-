from time import sleep

#Entrada
nome = str(input("Qual é o seu nome?\n"))
print(f"{nome} fiquei sabendo que você quer fazer uma viagem")
print("e quer calcular o valor da passagem né?")
print("Para distancia de ate 200 km sera cobrado 0,50 por KM ")
print("Para distancia de ate 200 km sera cobrado 0,45 por KM ")

#Dados
distancia = int(input("qual o valor que você vai percorrer?\n"))

#equação
resultado1 = distancia * 0.50
resultado2 = distancia * 0.45

if distancia <= 200:
    print(f"O valor da passagem é de {resultado1}")
else:
    print(f"O valor da passagem é de {resultado2}")

#Saída
print(f"{nome} muito obrigado por viajar com a nossa equipe")

sleep(20)