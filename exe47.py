from time import sleep

#Entrada
nome = str(input("Qual é o seu nome?\n"))
print(f"{nome} hoje vamos calcular seu imc e mostrar sua classificação")

#Dados
peso = float(input("Qual é o seu peso?\n"))
altura = float(input("Qual é a sua altura?\n"))

#Conta
imc = peso / (altura * altura)

#funções
if imc < 18.5:
    print("Amigão tu tem comer, tu ta abaixo do peso")

elif imc >=18.5 and 25:
    print("Tu ta no peso dahora para tu irmao")

elif imc >=25 and 30:
    print("Tu ta engordando, fica em alerta")

elif imc >=30 and 40:
    print("Filha ta gordo pra porra já")

elif imc >=40:
    print("Vai se cuidar tais carlo")
