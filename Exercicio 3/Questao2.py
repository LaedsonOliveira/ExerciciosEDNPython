
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))   


imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif 18.5 <= imc < 24.9:
    print("Você está com o peso ideal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")