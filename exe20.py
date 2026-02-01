from time import sleep
#saudação
nome = str(input("Seja bem vindo a mais um dia de estudos kkkkkkk Qual é o seu nome?\n"))
print(f"Muito bem {nome} vamos para a primeira atividade do dia!")
print("Hoje vamos pegar qual quer número que você digitar e redondar ele")
print("Atente-se de sempre usar ponto e utilizar no minimo 3 casas após o ponto")

#Recolher número
numero = float(input("Digite um número"))

#saida
print(f"Convertendo o número {numero} arredondando para {numero.__floor__()}")
print(f"Muito obrigado {nome} até a proxima")
sleep(20)
