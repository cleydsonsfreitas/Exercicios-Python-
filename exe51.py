from time import sleep
import time
#entrada
nome = str(input("Qual é o seu nome?\n"))
print(f"{nome} imagine você numa praia esperando a virada do ano")
print("E o seus relogos quebraram e você tem que usar python para não estragar a virada de sua familia")
print("Vamos fazer uma contagem regressiva juntos?")
time.sleep(5)

#Conta
for contagem_regressiva in range(10, 0, -1):
    print(contagem_regressiva)
    time.sleep(1)

#Saída
print("Feliz ano novo seus porra!!!")
print(f"{nome} você salvou o ano novo")
sleep(20)


