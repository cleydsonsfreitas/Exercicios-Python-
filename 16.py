from time import sleep
#Saudação
nome = input("Errei e fui muleke, na verdade esse é o penultimo kkkkkkkk qual é o seu nome?")
print(f"Muito bem {nome} jaja iremos descansar")
print("vamos calcular o desconto em cima do valor que você escolher")

#Cliente escolhe valor
produto = int(input("Qual é o preço do seu produto?"))

#conta
resultado =  produto * 5/100
print(f"Seu desconto foi de {resultado} reais")

resultado02 = produto - resultado
print(f"Logo seu novo preço é de: {resultado02} reais")

sleep(20)

