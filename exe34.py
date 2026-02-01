from time import sleep

#Entrada
nome = str(input("Qual é o seu nome jovem\n"))
print("Vamos descobrir se o número digitado por você é par ou impar")

#Dados
numero_a_ser_analisado = int(input("Digite um número\n"))

if numero_a_ser_analisado % 2 == 0:
    print("Seu número é par")
else:
    print("Seu número é impar")

print(f"ate")
sleep(20)