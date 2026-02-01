from time import sleep

#entrada
nome = str(input("Qual é o seu nome?\n"))
print(f"{nome} hoje vamos ajudar você a calcular a prestação mensal da sua casa e ver se aprovaremos o seu emprestimo")

#dados
casa = float(input("Qual o valor da casa em interesse?\n "))
salario = float(input("Qual o valor do seu salário?\n"))
anos = float(input("Em quantos anos você presente pagar?\n"))

#Função
parte1 = salario * 30/100
parte2 = parte1 * anos
parte3 = casa / parte2


if  parte3 > parte1:
    print(f"{nome} para a sua segurança resolvemos não liberar o esse emprestimo para você! Até a próxima")
else:
    print(f"{nome} parabens, seu impreestimo foi liberado")

#Saída
print(f"{nome} foi um prazer atender você, ate parça")

sleep(20)