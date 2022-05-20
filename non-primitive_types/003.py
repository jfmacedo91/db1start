# Escreva um programa que retorne o maior e o menor número de uma lista.
numbers = []
stop = False
answer = " "

while stop == False:
  while True:
    try:
      number = float(input("Digite um número: "))
    except:
      print("Por favor, digite um valor válido!")
    else:
      numbers.append(number)
      break
  
  while answer[0] not in "SN":
    answer = input("Gostaria de continuar? [S/N] ").strip().upper()
    if answer[0] == "N":
      stop = True
    elif answer[0] == "S":
      answer = " "
      break

print("-=-"*15)
print(f"O maior número digitado foi: {max(numbers)}")
print(f"O menor número digitado foi: {min(numbers)}")