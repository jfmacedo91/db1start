"""
  Escreva um programa que execute uma função que
  multiplique todos os números de uma lista passada por
  parâmetro.
"""

def multiplication_list(arr):
  multiplication = 1
  for number in arr:
    multiplication *= number

  return multiplication

print(multiplication_list([4, 5, 1, 9, 2]))