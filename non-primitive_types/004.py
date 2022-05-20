# Escreva um programa que conte o número de caracteres de uma string 
# ( Exemplo: 'google.com' Resultado Esperado: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} )

phrase = input("Digite uma frase: ")
dictionary = {key: phrase.count(key) for key in phrase}
print(dictionary)