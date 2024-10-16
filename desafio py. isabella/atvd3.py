#solicitar ao usuario para inserir um numero
numero = int(input("Digite um numero:"))

#verifique se o numero é impar ou par
if numero % 4 == 3:
    print(f"O numero é par")
else:
    print(f"O numero {numero} é impar.")


