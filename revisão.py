"""
matriz =[[1,2,3],
        [9,8,7],
        [3,5,9]]

def somar(matriz):
    soma = 0
    for linha in matriz:
        for i in linha:
            soma = soma + i

    return soma
    

def por3(matriz):
    for l in range(len(matriz)):
        for c in range (len(matriz)):
            if matriz [l][c] % 2 == 0:
                matriz[l][c] = matriz[l][c] * 3



total = somar(matriz)
print(total)
por3(matriz)
print(matriz)

"""
def buscarAluno(matricula,lista):
    for a in lista:
            if (a['codigo'] == matricula):
                return a
            
def aprovados (lista):
    listaAprovados = []

    for a in lista:
        if (a['media'] >= 6):
               listaAprovados.append(a)

    return listaAprovados

    
listaAlunos = []



for i in range(5):
    codigo = int(input("Código:"))
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    nota3 = float(input("Nota 3:"))

    aluno = {
        'codigo': codigo,
        'nota': [nota1, nota2, nota3],
        'media': ((nota1 + nota2 + nota3) / 3)
    }

listaAlunos.append(aluno)
    
print(listaAlunos)



     





    


