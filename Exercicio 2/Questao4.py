Quilomentragem = float(input("Digite a quilometragem percorrida: "))
LitrosAbastecimento = float(input("Digite o quantos litros foi abastecido: "))

consumoMedio = Quilomentragem / LitrosAbastecimento

print(f"\nConsumo Médio: {consumoMedio:.2f} km/L")