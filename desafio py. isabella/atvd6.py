# Solicita as três notas ao usuário
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno está aprovado ou reprovado
if media >= 7:
  situacao = "Aprovado"
else:
  situacao = "Reprovado"

# Exibe a média e a situação do aluno
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
