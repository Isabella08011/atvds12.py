def celsius_para_fahrenheit(celsius):
  """Converte uma temperatura de Celsius para Fahrenheit.

  Args:
    celsius: A temperatura em Celsius.

  Returns:
    A temperatura em Fahrenheit.
  """
  fahrenheit = celsius * 1.8 + 32
  return fahrenheit

# Exemplo de uso:
temperatura_celsius = int(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f}")
