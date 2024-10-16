# Recebe três números do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Determina o maior número usando uma estrutura condicional aninhada
if num1 >= num2 and num1 >= num3:
  maior = num1
elif num2 >= num1 and num2 >= num3:
  maior = num2
else:
  maior = num3

# Imprime o maior número
print("O maior número é:", maior)