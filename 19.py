from time import sleep
#recepção
nome = input("Olá Cliente,como é o seu nome?\n")
print(f"Muito bom telo aqui {nome}.Vamos saber em quanto ficou a sua divida?")

#Dias alugado
dia = int(input("Quantos dias você ficou com o carro?\n"))
conta01 = dia * 60
print(f"Seu gasto por dia foi de: {conta01}")

#KM rodado
km = int(input("Quantos você andou com o carro?"))
conta02 = km * (15 / 100)
print(f"Seu gasto por Km foi de:{conta02}")

#saida
print("Como avisado anteriormente no dia da locação, o valor final da divida é a somatoria de dia + KM")
resultadofinal = conta01 + conta02
print(f" Sua divida é de: {resultadofinal}")
print("Foi um prazer lhe atender, ate a proxima")
sleep(20)