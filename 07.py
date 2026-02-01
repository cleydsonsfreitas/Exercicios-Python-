from time import sleep

# saudação
saudacao01 = input("Seja bem-vindo, jovem Padawan! Qual é o seu nome?\n")
print(f"Muito bem, {saudacao01}!")

# tentando_melhorar_meus_limites
saudacao = input("Você está pronto para continuar? (Sim/Não)\n")

if saudacao.lower() == "sim":
    print(f"Já que digitou {saudacao}, vamos lá!")
else:
    print(f"Para de ser chato, {saudacao01}, você vai fazer sim!")


# Variáveis0102
try:
    valor01 = int(input("Digite o valor 1:\n"))
    print(valor01)
    valor02 = int(input("Digite o valor 2:\n"))
    print(valor02)

    resultado = valor01 + valor02
    print(f"Parabéns, padawan! Seu resultado é {resultado}.")
except ValueError:
    print("Por favor, digite apenas números inteiros.")

# saída
print(f"Muito obrigado por ter ido até o final, jovem {saudacao01}. Até a próxima!")
sleep(10)
