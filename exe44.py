from time import sleep
#entrada
nome = str(input("Qual é o seu nome aluno?\n"))
print("Vamos calcular sua média e ver sua situação")

#Dados
nota1 = int(input("Qual é a sua nota 01?\n"))
nota2 = int(input("Qual é a sua nota 02?\n"))

#conta
conta = (nota1 + nota2) /2

if conta < 5:
    print(f"{nome} muito otário você ta reprovado")
elif conta >= 5 and conta < 6.9:
    print(f"{nome} como você consegue? ta de recuperação")
elif conta >= 7:
    print(f"Parábens fera, tu foi aprovado")

print("Tamo junto caraí até aproxima")
sleep(20)