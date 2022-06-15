"""
  Escreva um programa que execute uma função que
  valide se o número informado é um número perfeito ou
  não.
"""

stop = False
answer = " "
summation = 0

while stop == False:
  while True:
    try:
      number = int(input("Digite um número inteiro: "))
    except:
      print("Por favor, digite um valor válido!")
    else:
      for index in range(number -1, 0, -1):
        if number % index == 0:
          summation += index
        else:
          continue

      if number == summation:
        print(f"O número {number} é perfeito, pois a soma de seu divisores é {summation}")
        summation = 0
      else:
        print(f"O número {number} não é perfeito!, pois a soma de seu divisores é {summation}")
        summation = 0
      break
  
  while answer[0] not in "SN":
    answer = input("Gostaria de continuar? [S/N] ").strip().upper()
    if answer[0] == "N":
      stop = True
    elif answer[0] == "S":
      answer = " "
      break