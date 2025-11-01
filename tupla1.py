"""
numeros = [1,2,3,4,5]
#sublista valores < 4
sublista = []
for n in numeros:
    if n < 4:
        sublista.append(n)
print(sublista)

listab = [n for n in numeros if n < 4]
print(listab)

aluno =("joao da silva", 1111, 23.40)
print(aluno)

print("Acesso posicional da tupla")
print("nome:", aluno[0])
print("código:", aluno[1])
print("nota:", aluno[2])

#nao permitido devido a imutabilidade da tupla
#aluno[0] =  "ana"

aluno2 = ("maria", 222, 33.22)
alunos = aluno + aluno2
print(alunos)
"""
"""
dicionario = {"nome" : "joao", "codigo" : 10}
print(dicionario)
#pop obtem o valor relativo a uma chave
x = dicionario.pop("codigo")
print(x)

#copia do objeto
a = dicionario.popitem()
print(a)
print(dicionario)
"""
aluno = {"nome": "joao da silva", 
         "curso": "computação",
         "instituição" : "facef",
         "codigo" : 1919}

print(aluno)
print(aluno['nome'])

aluno['nome'] = "Bortoltoti"
print(aluno)
aluno ['disciplina'] = "logica"
print(aluno)

#funcao sao blocos de codigos que podem ser nomeadas e chamadas dentro de um programa
