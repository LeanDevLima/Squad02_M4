
# Importar a biblioteca math para cálculos de raiz quadrada e cúbica
import math

# Solicitar ao usuário que insira um valor
valor = float(input("Digite um valor: "))

# Calcular os cinco outputs conforme especificado
dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_quadrada = math.sqrt(valor)
# raiz_quadrada = valor ** (1/2)
raiz_cubica = valor ** (1/3)


# Exibir os resultados
print(f"Primeiro output: O dobro do valor inserido é {dobro}")
print(f"Segundo output: O triplo do valor inserido é {triplo}")
print(f"Terceiro output: O valor inserido ao quadrado é {quadrado}")
print(f"Quarto output: A raiz quadrada do valor inserido é {raiz_quadrada}")
print(f"Quinto output: A raiz cúbica do valor inserido é {raiz_cubica}")


