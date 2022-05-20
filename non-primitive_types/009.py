# Escreva um programa que leia chaves e valores, crie um dicionário, e depois, verifique se uma chave informada existe em um dicionário.

dictionary = {}
answer = " "
stop = False

while stop == False:
  key = input("Digite uma chave para o valor: ")
  value = input("Agora digite um valor para para a chave digitada: ")

  if key.isnumeric():
    key = float(key)

  if value.isnumeric():
    value = float(value)
  
  dictionary[key] = value

  while answer[0] not in "SN":
    answer = input("Gostaria de continuar? [S/N] ").strip().upper()
    if answer[0] == "N":
      stop = True
    elif answer[0] == "S":
      answer = " "
      break

keys = dictionary.keys()

print("-=-"*20)
search_key = input("Digite uma key para saber seu valor: ")

if search_key.isnumeric():
    search_key = float(search_key)

if search_key in keys:
  print(f"O valor para a chave '{search_key}' é '{dictionary[search_key]}'")
else:
  print("Essa chave não axiste para esse dicionário!")