from time import sleep
#Entrada
nome = str(input("Salve, qual é o seu nome?\n"))
print(f"{nome} hoje vamos ler seu nome completo e ver algumas variações dele, preparado?")

#Dados
nome_completo = str(input("Como é o seu nome completo?\n"))

#Transformando dados
print(f"Seu nome com todas as letra Minuscula fica {nome_completo.upper()}")
print(f"Seu nome com todas as letra Maiuscula fica {nome_completo.lower()}")
print(f"Seu nome completo tem {len(nome_completo.strip())}")
print(f"Seu primeiro nome que é {nome} e tem {len(nome.strip())} de caracteres. ")

sleep(20)