print("Verificação de Senha")
senha = input("Digite sua senha: ")

if len(senha) < 8:
    print("Senha inválida: deve ter pelo menos 8 caracteres.")
elif not any(char.isdigit() for char in senha):
    print("Senha inválida: deve conter pelo menos um número.")
else:
    print("Senha válida!")