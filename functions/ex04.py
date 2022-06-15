"""
  Escreva um programa que execute uma função que
  retorne o inverso de uma string passada por parâmetro.
"""

def inverted_string(string):
  inverted = ''
  for letter in range(len(string) -1, -1, -1):
    inverted += string[letter]

  return inverted

print(inverted_string("Jean Fernandes de Macedo"))