# Escreva um programa que concatene os dicionários abaixo e crie um novo
# Exemplo dicionário(Dict):
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Resultado esperado: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}

dictionary = {**dic1, **dic2, **dic3}

print(dictionary)