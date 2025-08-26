from datetime import datetime

def dias_de_vida(data_nascimento: str) -> int:
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    return (hoje - nascimento).days


data = input("Digite sua data de nascimento (dd/mm/yyyy): ")
print("Você está vivo há", dias_de_vida(data), "dias.")