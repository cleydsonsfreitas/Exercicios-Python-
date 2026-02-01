from time import sleep 
import time 

#Entrada 
nome = str(input("Olá, qual é o seu nome?\n"))
print(f"{nome} sejá bem vindo ao nosso sistema de calculo de imposto.")

#recolhimento 
print(f"{nome} Primeiro preciso saber sua localidade")
localidade = str(input("Digite: \n[1]China\n[2]Alemanha\n[3]Estados unidos\n "))

if localidade == "1":
    print("中文： 你住在中国，真是太神奇了！中国人口这么多")

elif localidade == "2":
    print("Wissen Sie, dass Deutschland das zweitgrößte Bierkonsumland der Welt ist? Das ist doch beeindruckend!")

elif localidade == "3":
    print("top, did you know that the united states likes nuclear war?")


#Produto
print(f"{nome} agora precisamos saber qual o produto que você deseja importar")
produto = str(input("Digite: \n[1]Carro\n[2]Informática\n[3]Perfume\n[4]Roupas\n"))


#China
if localidade == "1" and produto == "1":
    print("A taxa de exportação desse produto é do valor é de 2%")

elif localidade == "1" and produto == "2":
    print("A taxa de exportação desse produto é do valor é de 4%")

elif localidade == "1" and produto == "3":
    print("A taxa de exportação desse produto é do valor é de 6%")

elif localidade == "1" and produto == "4":
    print("A taxa de exportação desse produto é do valor é de 8%")


#Alemanha
if localidade == "2" and produto == "1":
    print("A taxa de exportação desse produto é do valor é de 10%")

elif localidade == "2" and produto == "2":
    print("A taxa de exportação desse produto é do valor é de 5%")

elif localidade == "2" and produto == "3":
    print("A taxa de exportação desse produto é do valor é de 15%")

elif localidade == "2" and produto == "4":
    print("A taxa de exportação desse produto é do valor é de 20%")


#Estados Unidos
if localidade == "3" and produto == "1":
    print("Esse produto é isento de taxação")

elif localidade == "3" and produto == "2":
    print("A taxa de exportação desse produto é do valor é de 3%")

elif localidade == "3" and produto == "3":
    print("A taxa de exportação desse produto é do valor é de 5%")

elif localidade == "3" and produto == "4":
    print("A taxa de exportação desse produto é do valor é de 7%")


#Valor do produto  a ser taxado
valor = int(input("Digite o valor do produto\n"))

#Contas
c1 = (valor * 2/100) + valor 
c2 = (valor * 4/100) + valor
c3 = (valor * 6/100) + valor
c4 = (valor * 8/100) + valor

a1 = (valor * 10/100) + valor 
a2 = (valor * 5/100) + valor 
a3 = (valor * 15/100) + valor 
a4 = (valor * 20/100) + valor 


e1 = valor * 1
e2 = (valor * 3/100) + valor 
e3 = (valor * 5/100) + valor 
e4 = (valor * 7/100) + valor 


#codigo de espera 
print(f"{nome} vamos analisar seu produto e informar o novo valor...................")
time.sleep(10)


#China
if localidade == "1" and produto == "1":
    print(f"Seu produto ficou no valor de: {c1}")

elif localidade == "1" and produto == "2":
    print(f"Seu produto ficou no valor de: {c2}")

elif localidade == "1" and produto == "3":
    print(f"Seu produto ficou no valor de: {c3}")

elif localidade == "1" and produto == "4":
    print(f"Seu produto ficou no valor de: {c4}")


#Alemanha
if localidade == "2" and produto == "1":
    print(f"Seu produto ficou no valor de: {a1}")

elif localidade == "2" and produto == "2":
    print(f"Seu produto ficou no valor de: {a2}")

elif localidade == "2" and produto == "3":
    print(f"Seu produto ficou no valor de: {a3}")

elif localidade == "2" and produto == "4":
    print(f"Seu produto ficou no valor de: {a4}")


#Estados Unidos
if localidade == "3" and produto == "1":
    print(f"Esse produto não sofre taxação ele vai manter o valor de: {e1}")

elif localidade == "3" and produto == "2":
    print(f"Seu produto ficou no valor de: {e2}")

elif localidade == "3" and produto == "3":
    print(f"Seu produto ficou no valor de: {e3}")

elif localidade == "3" and produto == "4":
    print(f"Seu produto ficou no valor de: {e4}")


#Saida
print(f"Muito obrigado {nome} até a próxima")

sleep(10)
