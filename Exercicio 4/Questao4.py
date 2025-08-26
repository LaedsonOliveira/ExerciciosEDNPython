print("=== Classificador de Números ===")
pares = 0
impares = 0

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break

    if entrada.isdigit():
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
            print(f"{numero} é PAR")
        else:
            impares += 1
            print(f"{numero} é ÍMPAR")
    else:
        print("Digite apenas números ou 'sair'.")

print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")
