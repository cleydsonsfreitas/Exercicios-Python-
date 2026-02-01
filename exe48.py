from time import sleep

#entrada
nome = str(input("Qual é o seu nome?\n"))
print("Vamos calcular o valor a ser pago por um produto")
print("Lembre sempre que o preço muda de acordo com a forma de pagamento escolhido por você")

#Dados
valor = float(input("Qual o valor a ser pago?\n"))
opcao_de_pagamento = int(input("Qual vai ser a forma de pagamento? Digite:\n 1- Dinheiro/cheque\n 2- Cartão\n 3- 2x no cartão\n 4- 3x no cartão\n"))

#contas
conta_dinheiro_cheque = valor - (valor * 10/100)
conta_cartao = valor - (valor * 5/100)
conta_2x_cartao = valor / 2
conta_3x_cartao = (valor + (valor * 20/100)) / 3

if opcao_de_pagamento == 1:
    print(f"Seu desconto vai ser de 10% e o pagamento vai ficar em: {conta_dinheiro_cheque}")

elif opcao_de_pagamento == 2:
    print(f"Seu desconto vai ser de 5% e o pagamento vai ficar em: {conta_cartao}")

elif opcao_de_pagamento == 3:
    print(f"O valor não vai ter acrescimo e nem desconto e ficara 2x de: {conta_2x_cartao}")

elif opcao_de_pagamento == 4:
    print(f"Vai ter um acrescimo de 20% porcento em 3x de: {conta_3x_cartao}")

print("Dahora, ate a proxima")
sleep(20)
