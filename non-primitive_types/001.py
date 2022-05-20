# Escreva um programa que some todos os itens de uma lista.
numbers = []
sum = 0
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
  sum += number

print("-=-"*15)
print(f"A soma de todos os valores digitados é: {sum}")