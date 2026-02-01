from time import sleep
#entrada
nome = str(input("Qual é o seu nome atleta?\n"))
print(f"{nome} vamos descobrir qual é a sua categoria")

#Dados
idade = int(input("Qual é o seu nao de nascimento?\n"))

#Conta
conta = 2024 - idade

#Funções
if conta < 9:
    print("Sua categoria é mirim")

elif conta > 9 and conta <= 14:
    print("Sua categoria é infantil")

elif conta > 14 and conta <= 19:
    print("Sua categoria é junior")

elif conta > 19 and conta <= 20:
    print("Sua categoria é sênior")

elif conta > 20:
    print("Sua categoria é a master")

print("Valeu fera")
sleep(20)