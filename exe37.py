from time import sleep

#entrada
nome = str(input("Qual é o seu nome porra?\n"))
print("Hoje vamos precisar que você digite 3 números e vamos mostar o maior e o menor")

#Recolher dados
valor1 = int(input(" Digite um valor\n"))
valor2 = int(input(" Digite um valor\n"))
valor3 = int(input(" Digite um valor\n"))

#funcionalidade
valores = [valor1, valor2, valor3]
maior = max(valores)
menor = min(valores)

print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")

#Saida
print(f"{nome} até a proxima ")

sleep(20)
