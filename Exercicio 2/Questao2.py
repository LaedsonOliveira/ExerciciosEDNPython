nomeProduto = "Camiseta"
precoOriginal = 50.00
porcentagemDesconto = 20

valorDesconto = (porcentagemDesconto / 100) * precoOriginal
precoComDesconto = precoOriginal - valorDesconto

print("Detalhes do Produto:")
print(f"Produto: {nomeProduto}")
print(f"Preço Original: R$ {precoOriginal:.2f}")
print(f"Desconto: {porcentagemDesconto}%")
print(f"Preço com Desconto: R$ {precoComDesconto:.2f}")