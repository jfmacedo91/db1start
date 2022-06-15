"""
  Escreva um programa que execute uma função que
  some todos os itens de uma lista passada por
  parâmetro.
"""

def summation_list(arr):
  summation = 0
  for number in arr:
    summation += number

  return summation

print(summation_list([4, 5, 1, 9, 2]))