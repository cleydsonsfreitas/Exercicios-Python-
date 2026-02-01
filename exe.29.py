from time import sleep
#Entrada
ola = str(input("Tudo bem com você?\n"))
print("Hoje vamos descobrir se seu nome tem Santos")

#Dado
nome = str(input("Qual é o seu nome completo?\n")).strip()
print("Santos" in nome)
sleep(20)