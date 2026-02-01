from time import sleep
import random
#Entrada
nome = str(input("Qual é o seu nome Professor(a)?\n"))
print(f"{nome} hoje vamos ajudar você a escolher um dos seus 4 alunos para apagar o quadro")

#Coletagem de dados
aluno01 = str(input("Digite o nome do aluno 1:\n"))
aluno02 = str(input("Digite o nome do aluno 2:\n"))
aluno03 = str(input("Digite o nome do aluno 3:\n"))
aluno04 = str(input("Digite o nome do aluno 4:\n"))


#Resulado
alunos_a_ser_escolhido = [aluno01, aluno02, aluno03, aluno04]
resultado = random.choice(alunos_a_ser_escolhido)

#Saída
print(f"Parábens seu aluno escolhido para apagar o quadro é {resultado}")
print(f"Até a próxima {nome}")
sleep(20)
