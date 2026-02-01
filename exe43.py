from time import sleep

#entrada
nome = str(input("Fala teu nome soldadinho?\n"))
print("hoje vamos descobrir como está a sua situalção com o exercito militar")

#Dados
idade = int(input(f"{nome} Qual é a sua idade aspira?\n"))

#Contas
resultado = idade - 18
resultado1 = 18 - idade

#funções
if idade < 18:
    print(f"Você ainda tem um tempinho ate se alistar falta {resultado1} para o seu alistamento obrigatorio")
elif idade > 18:
    print(f"Você jám passou da data burro e já faz {resultado} que você deveria se alistar")

else:
    print(f"Você está no tempo certo para alistamento, procure a junta mais próxima")

print("Até soldado")
sleep(20)
