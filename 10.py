from time import sleep
#inicio
nome = input("Salve Salve rapaziada, quale é o teu nome?\n")
print(f"boa meu rei, {nome} me parece um nome importante")
print("Hoje vamos descobri o dobro, triplo e a raiz quadrada de um número de sua escolha\n")

#recebendo_o_valor
valor01 = int(input("Digite um valor ai pa nois"))

#conta
dobro = valor01 * 2
triplo = valor01 * 3
raiz = pow(valor01, 0.5)

print(f"O dobro é {dobro}")
print(f"O triplo é {triplo}")
print(f"A raiz é {raiz:.2f}")

print("Muito obrigado até a proxima")

sleep(20)