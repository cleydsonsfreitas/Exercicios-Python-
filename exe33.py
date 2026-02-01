from time import sleep

#Entrada
nome = str(input("Salveeeeeeeeeeeee qual é o seu nome?\n"))
print(f"{nome} vamos imaginar que você está numa estrada")
print("Nela você esta a certa velocidade que jaja você vai defini-la")
print("O limite da estrada é de 80 Km/h")
print("Caso estiver acima da velocidade será multado")

#Dados
velocidade = int(input("Qual é a sua velocidade?\n"))

#Conta caso seja multado
resultado = (velocidade - 80) * 7

if velocidade > 80:
    print("Cara, vai com calma se não você morre")
    print("infelizmente terei que te multar e a multa é 7 reais por cada  velocidade acima do permitido")
    print(f"{nome} Tenha mais consciencia, sua multa é de {resultado}")

else:
    print(f"Parabens pela consciencia {nome} por mais motoristas como você!!!")

#Saída
print(f"Muito obrigado felas até a proxima {nome}")
sleep(20)