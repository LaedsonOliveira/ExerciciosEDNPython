
print("Média da Turma")
notas = []
qtd = int(input("Quantos alunos na turma? "))

for i in range(qtd):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Notas:", notas)
print("Média da turma:", media)
