from time import sleep
import random
#Entrada
nome = str(input("Qual é o seu nome Professor(a)?\n"))
print(f"{nome} hoje vamos ajudar você a escolher a ordem de apresentção dos seus 4 alunos")

#Coletagem de dados
grupo01 = str(input("Digite o nome do grupo 1:\n"))
grupo02 = str(input("Digite o nome do grupo 2:\n"))
grupo03 = str(input("Digite o nome do grupo 3:\n"))
grupo04 = str(input("Digite o nome do grupo 4:\n"))


#Resulado
alunos_a_ser_escolhido = [grupo01, grupo02, grupo03, grupo04]
resultado = random.sample(grupos_a_ser_escolhido,4)

#Saída
print(f"A ordem de apresentação é  {resultado}")
print(f"Até a próxima {nome}")
sleep(20)