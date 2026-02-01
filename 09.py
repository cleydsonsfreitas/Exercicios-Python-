from time import sleep
#Entrda
nome = input("Olá, tudo bem? Como é o seu nome?\n")
print(f"Muito bem {nome} vamos dar inicio\n")
print("Se chegou aqui é por algum motivo\n")
print("Hoje vamos descobrir  o antecessor de um numero e o seu sucessor\n")

#Valor
valor01 = int(input("Digite um valor"))

#conta
antecessor = valor01 - 1
sucessor = valor01 + 1

#resultado
print(f"O antecessor do número escolhido é {antecessor}\n")
print(f"O Sucessor do número escolhido é {sucessor}\n")
print("Muito obrigado e até a próxima")

sleep(20)