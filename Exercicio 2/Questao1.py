valorReais = float(input("Digite o valor em reais: "))

taxaDolar = 5.20
taxaEuro = 6.15

valorDolares = valorReais / taxaDolar
valorEuros = valorReais / taxaEuro

print("Reais para Dólares e Euros:")
print(f"R$ {valorReais:.2f}")

print("--------------------------")
print(f"Valor em dólares: {valorDolares:.2f}")
print(f"Valor em euros: {valorEuros:.2f}")
print("--------------------------")