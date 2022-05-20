# Escreva um programa que ordene em ordem crescente uma lista de tuplas informadas, pelo último item da tupla
# Exemplo de lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Resultado esperado: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
tuples.sort(key=lambda x: x[1])
print(tuples)