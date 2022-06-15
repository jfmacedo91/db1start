"""
  Escreva um programa que execute uma função que
  calcule o fatorial de um número passado por parâmetro.
"""

def factorial(number):
  result = 1
  for number in range(number, 0, -1):
    result *= number

  return result

print(factorial(5))