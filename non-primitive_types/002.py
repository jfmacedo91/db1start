# Escreva um programa que multiplique todos os itens de uma lista.
numbers = []
result = 1
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

for number in numbers:
  result *= number

print("-=-"*15)
print(f"A multiplicação de todos os valores digitados é: {result}")