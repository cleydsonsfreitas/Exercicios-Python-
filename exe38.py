from time import sleep

#Entrada
nome = str(input("Fala fruto do capitalismo, qual é o seu nome?\n"))
print(f"hoje vamos calcular seu aumento de salário")
print("Para salários acima de 1.250 terá um aumento de 10%")
print("Para salários abaixo de 1.250 terá um aumento de 15%")

#dados
salario = int(input("Qual o valor do sue salário?\n"))

#Contas
aumento1 = salario * 10/100 + salario
aumento2 = salario * 15/100 + salario

if salario > 1250:
    print(f"Seu aumento será de 10% ficando {aumento1}")
else:
    print(f"Seu aumento será de 15% ficando {aumento2}")

#Saída
print(f"{nome} espero que tenha gostado do seu novo salário, se não mude de emprego e faça faculdade")

sleep(20)