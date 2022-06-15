"""
  Escreva um programa que execute uma função que
  receba um número informado no console como
  parâmetro e verifique se o número informado é primo ou
  não.
"""

stop = False
answer = " "
prime = True

while stop == False:
  while True:
    try:
      number = int(input("Digite um número inteiro: "))
    except:
      print("Por favor, digite um valor válido!")
    else:
      for index in range(number -1, 1, -1):
        if number % index == 0:
          prime = False
          break
        else:
          continue

      if prime == True:
        print(f"O número {number} é primo!")
      else:
        print(f"O número {number} não é primo!")
        prime = True
      break
  
  while answer[0] not in "SN":
    answer = input("Gostaria de continuar? [S/N] ").strip().upper()
    if answer[0] == "N":
      stop = True
    elif answer[0] == "S":
      answer = " "
      break