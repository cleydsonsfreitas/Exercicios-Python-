from time import sleep
#Entrada
nome = str(input("Olá Jovem, estou com dificuldade nesse sexercio, você vai me ajuadr a fixar  o contéudo, Qula é o seu nome\n"))
print(f"Muito bem {nome} é um prazer receber a sua ajuda")

# Dados
numero = input("Escreva um número entre 0 e 9999:\n")

# Execução
print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar: {numero[0]}")
sleep(20)