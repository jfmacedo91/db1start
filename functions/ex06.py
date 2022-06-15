"""
  Escreva um programa que execute uma função que
  conte o número de letras maiúsculas e minúsculas de
  um texto e que ao final, chame outra função para
  imprimir o resultado.
"""

def print_results(uppercase, lowercase):
  print(f"O total de letras maiúsculas é: {uppercase}")
  print(f"O total de letras minúsculas é: {lowercase}")

def letters_count(string):
  uppercase = 0
  lowercase = 0
  for letter in string:
    if letter.isupper():
      uppercase += 1
    elif letter.islower():
      lowercase += 1
    else:
      continue

  print_results(uppercase, lowercase)

letters_count("Jean Fernandes de Macedo")