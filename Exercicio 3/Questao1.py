
idade = int(input("Digite a sua idade: "))

if idade > 0 and idade <= 12:
    print("Você é CRIANÇA.")

elif idade >= 13 and idade < 17:
    print("Você é ADOLECENTE.")

elif idade >= 18 and idade < 59:
    print("Você é ADULTO.")

elif idade >= 60:
    print("Você é IDOSO.") 
    
else:
    print("Idade inválida. Por favor, insira uma idade positiva.")