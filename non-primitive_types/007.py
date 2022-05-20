# Escreva um programa que adicione uma chave (key) a um dicionário.
# Exemplo dicionário(Dict): {0: 10, 1: 20}
# Resultado esperado: {0: 10, 1: 20, 2: 30}

dictionary = {0: 10, 1: 20}
stop = False
answer = " "

while stop == False:
  while True:
    try:
      number = int(input("Digite um número inteiro: "))
    except:
      print("Por favor, digite um valor válido!")
    else:
      dictionary[len(dictionary)] = number
      break
  
  while answer[0] not in "SN":
    answer = input("Gostaria de continuar? [S/N] ").strip().upper()
    if answer[0] == "N":
      stop = True
    elif answer[0] == "S":
      answer = " "
      break

print(dictionary)