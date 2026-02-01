import time

# Entrada String
nome = str(input("Olá, seja bem vindo,qual é p seu nome?\n"))
print(f"Seja bem vindo {nome}, é um prazer ter você aqui conosco\n")

# Entrada Inteiros
idade = int(input("Qual é a sua idade?\n"))

if idade >= 18:
    print(f"Puxa {nome}, tu já pode ser preso cara\n")
else:
    print(f"Puxa {nome}, tu é menor de idade, sai daqui seu inseto\n")

# Explicação
print(f"{nome} chega de interrogatórios,")
time.sleep(1)
print("Hoje eu estou voltando a estudar programação")
time.sleep(1)
print("Infelizmente você foi a minha cobaia")
time.sleep(1)
print("Eu estou pegando as entradas simples de variáveis e criando interação com você")
time.sleep(1)
print("Não ache que acabou, eu vou precisar de você")
time.sleep(1)
print("Vou precisar que você digite dois números, aí vou fazer todas as operações básicas e te dar uma lista\n")


numero1 = float(input(f"{nome} me fale um número\n"))
print(f"{nome} boa\n")

numero2 = float(input(f"{nome} me fala um segundo número\n"))
print("Muito bem")

# Equações básicas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Vamos lá, em uma contagem de 5 segundos sua lista é gerada\n")
print("conte comigo")

# Laço simples (exatamente como você fez)
for i in range(5, -1, -1):
    print(i)
    time.sleep(1)

# Saída
print(f"| Soma é igual a: {soma}|")
print(f"| Subtração é igual a: {subtracao}|")
print(f"| Multiplicação é igual a: {multiplicacao}|")
print(f"| Divisão é igual a: {divisao}|")
print(f"Muito obrigado por participar {nome}, até a próxima!")

time.sleep(5)