"""
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
matriz [0][1]


matriz[0][1] = "oi"
print(matriz)
"""
"""

matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz.append([10,11,12])
print(matriz)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
print(matriz[1][1])
del matriz[2][0]
print(matriz)

print("### matriz impressao ###")
soma = 0
for linha in matriz:
        for coluna in linha:
                print(coluna)
                soma += coluna
print("Soma matriz:", soma)

quadrados = []

for x in range (10):
    quadrados.append(x**2)
print(quadrados)

listaQuadrados = [x**2 for x in range(10)]
print(listaQuadrados)
"""
