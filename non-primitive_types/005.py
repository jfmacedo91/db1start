# Escreva um programa que conte quantas string tenham tamanho maior que 2 e o primeiro e último caracteres sejam iguais.
# (Exemplo de lista: ['abc','xyz','aba','1221'] Resultado esperado: 2 )
string_list = []
stop = False
answer = " "

while stop == False:
  string = input("Digite uma palavra: ").strip().upper()
  string_list.append(string)
  
  while answer[0] not in "SN":
    answer = input("Gostaria de continuar? [S/N] ").strip().upper()
    if answer[0] == "N":
      stop = True
    elif answer[0] == "S":
      answer = " "
      break

total = 0

for string in string_list:
  if len(string) > 2 and string[0] == string[-1]:
    total += 1

print("-=-"*20)
print(f"A quantidade de strings com mais de 2 caracteres e o primeiro e último caracteres são iguais: {total}")