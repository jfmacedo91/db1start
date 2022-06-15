"""
  Escreva um programa que execute uma função que
  encontre o maior número de uma lista passada por
  parâmetro.
"""

def higher_number(arr):
  higher = 0
  for number in arr:
    if number > higher:
      higher = number
    else:
      continue

  return higher

print(higher_number([4, 5, 1, 9, 2]))