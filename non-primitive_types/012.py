# Escreva um programa que verifique se uma lista está vazia ou não.

my_list = [5, 6, 0]

if len(my_list) == 0:
  print("A lista está vazia!")
elif len(my_list) == 1:
  print("A lista contém o item:")
  for item in my_list:
    print(item)
else:
  print("A lista contém os itens:")
  for item in my_list:
    print(item)