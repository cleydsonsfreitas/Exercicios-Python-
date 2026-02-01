nome = input("Qual é o seu nome? ")
print(nome)

incognita = input("Digite um valor  ")

try:
    valor = int(incognita)
    print(f"Parabéns! O tipo do valor digitado é {type(valor)} e o valor é {valor}.")
except ValueError:
    try:
        valor = float(incognita)
        print(f"Parabéns! O tipo do valor digitado é {type(valor)} e o valor é {valor}.")
    except ValueError:
        if incognita.lower() in ['true', 'false']:
            valor = bool(incognita.lower() == 'true')
            print(f"Parabéns! O tipo do valor digitado é {type(valor)} e o valor é {valor}.")
        else:
            print(f"Parabéns! O tipo do valor digitado é {type(incognita)} e o valor é {incognita}.")