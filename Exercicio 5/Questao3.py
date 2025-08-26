def aplicar_desconto(preco: float, desconto_percentual: float) -> float:
    """
    Calcula o preço final após aplicar o desconto.
    """
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)


preco_produto = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))
print(f"Preço final com desconto: R$ {aplicar_desconto(preco_produto, desconto)}")