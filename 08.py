from time import sleep
#Aqui é a recepção e saudação com o usuário
nome=input("Qual é o seu nome macaquinho?\n ")
print(f"Seja bem vindo {nome} ou melhor uhuhuhuhuhuhuhu")

#Aqui começa nossas perguntas e atribuição as váriaveis
print("Vamos realizar as principais contas matematicas entre dois números?")
valor01=int(input("Digite o valor 1 por favor\n"))
valor02=int(input("Digite o valor 2 por favor\n"))

#contas e resultados
resultado_soma = valor01 + valor02
resultado_subitracao = valor01 - valor02
resultado_multiplicacao = valor01 * valor02
resultado_divisao = valor01 / valor02
resultado_divisaointeiro = valor01 // valor02
resultado_potencia = valor01 ** valor02
print(f" A soma é {resultado_soma}")
print(f" A Subtração é {resultado_subitracao}")
print(f" A Subtração é {resultado_subitracao}")
print(f" A Multiplicação é {resultado_multiplicacao}")
print(f" A Divisão é {resultado_divisao :.2f}")
print(f" A o resto da sua divisão é {resultado_divisaointeiro}")
print(f" A Potênciação é {resultado_potencia}")
sleep(20)