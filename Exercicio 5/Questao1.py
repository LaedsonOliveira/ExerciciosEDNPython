def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)


conta = float(input("Digite o valor da conta: R$ "))
percentual = float(input("Digite a porcentagem da gorjeta (%): "))
print(f"Valor da gorjeta: R$ {calcular_gorjeta(conta, percentual)}")