"""
  Escreva um programa Python que execute uma string
  que contenha um código Python.
"""

def run_string(string):
  exec(string)

run_string("for number in range(5): print(number + 1)")