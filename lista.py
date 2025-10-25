"""
compras = ["arroz", "feijão", "carne", 12.2]

print (compras)


print (compras[3])
compras[3] = 99.9
print (compras)

print(len(compras))

compras = []
print (compras)

x = (list(range(5)))
print(x)
"""
"""
lista = [2.3, 5.5, 2.2, 5.5, 7.7]

#somar elementos
soma = 0

for n in lista:
    soma += n

    print("A soma das notas é:", soma)

#lista posicional

alunos = ['Glauber', 'Bortoloti', 'Hugo', 'Marina']

for n in range(len(alunos)):
    print(f"Posição {n} da lista: {alunos[n]}")

    print ("===>", list(range(len(alunos))))

"""
"""
n = 5
notas = []

for i in range(1, n+1):
    x = int(input("Nota do aluno:"))
    notas.append(x)

media = 0
for n1 in notas:
    media = media + n1
media = media / n

for n1 in notas:
    if n1 > media:
        print ("Aprovado", n1)
 """
"""
soma = 0
maior = 0
quantidadeMaior = 0

for i in range (1, 6):
    produto = int(input("Quantidade do produto:"))
    valor = float(input("Valor do produto:"))
    total = valor * produto
    soma += total

    print ("A quantidade é", produto)
    print ("O valor é:", valor)
    print ("O total é:", total)

   
    if valor > maior:
        maior = valor
        quantidadeMaior = produto

print("Quantidade do produto de maior valor:", quantidadeMaior)
print("Maior valor unitário:", maior)
print("Soma total de cada produto:", soma)

"""
"""
quantidades = []
valores = []
totais = []
totalGeral = 0.0

for i in range(5):
    qtd = int(input("Quantidade:"))
    valor = float(input("Valor:"))
    quantidades.append(int("Quantidade:"))
    valores.append(float(input("Valor:")))

    totais.append( (qtd * valor))
    totalGeral += (qtd * valor)

#encontrar produto de maior valor
maior = valores[0] #inicializa maior com um valor qualquer
posicaoMaior = 0
for i in range(len(quantidades)):
    if valores[i] > maior:
        maior = valores[i]
        posicaoMaior = i

print (quantidades)
print (valores)
"""
"""
valores = [1, 3, 4, 5, 6, 7, 8, 20]
print (valores)

v1 = valores[1:4]
print (v1)

#da posição té o fim da lista
print (valores[3:])

#do inicio até a posição j-1
print (valores[ :3])

#de quanto em quanto
print (valores[1:7:2])
"""
"""
x = [5, 7, 9]

print(x)
n1 = x[0]
n2 = x[1]
n3 = x[3]

print ("n1: ", n1)

[a,b,c] = x
print(a)
print(b)
print(c)

a = [1,2,3]
b = [4,5,6]

#concatenando a e b em uma so listinha 
lista = a + b
print (lista)

listaATripla = a * 3
print (listaATripla)

#remove o elemento da lista na posição indicada
del listaATripla[2]
print(listaATripla)
"""
"""
a = [1,2,3]

print(a)

#b aponta pra a mesma referencia de a 
#b = a
b = a [:]

print(b)

a.append(-5)
print(a)
print(b)
"""
"""
lista1 = [1,2,3,4]
lista2 = [9,8,7,6]

#concatenacao ou uniao
x = lista1 + lista2
print(x)

y = lista1 * 3
print(y)

#deleta uma posicao especifica da lista
del y[5]
print(y)
"""
"""
a = [9,8,7]
print(a)
b = a
print(b)

b.append(333)
print(a)
print(b)

del a[1]
print(a)
print(b)

#copia
c = a[:]
print('c', c)
c.append(444)
print(c)
print('a:', a)

#endereços de memoria
print(id(a))
print(id(b))
print(id(c))

#verificar se um elemento consta na linha
if 7 in c:
    print("7 esta na lista")

print(c)
c.append(55)
print(c)
c.insert(0,99)
print(c)
"""




    




    

