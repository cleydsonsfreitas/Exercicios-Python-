from time import sleep
#Entrada com o usuário
print("Olá, hoje vamos criar um código que lê seu nome e a partir dele geraremos algumas informações")
print("Para isso vou precisar da sua colaboração")

#Coletagem de dados
nome = str(input("Qual o seu nome completo?\n ")).upper().strip()


#Resultado
print(f"O seu nome tem {nome.count("A")} letras A")
print(f"A primeira letra a fica na posição {nome.find("A")+1} ")
print(f"Aultima letra a fica na posição {nome.rfind("A")+1} ")

sleep(20)