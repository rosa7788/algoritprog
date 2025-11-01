"""
def imprimeCompras ():
    compras = ["Miojo", "Ovo", "Leite", "Pão"]
    print("Lista de compras")
    for item in compras:
        print("Produto:", item)
#fim da função

print ("Antes da função")
imprimeCompras()

print("Depois da função")
"""
"""
def reajuste(salario, juros = 0.25):
    return salario + salario * juros

print("Reajuste 1:", reajuste(100))
print("Reajuste 2:", reajuste (100, 0.10))
"""
"""
def maior (x,y):
    if x > y:
        return x
    else:
        return y
        print("Essa mensagem não será impressa")

#fim da função

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y:"))
z = maior(x,y)
print("O maior valor é: ", z)
"""
"""
def valor():
    print("Valor de x:", x)
    y = 2 * x 
    print ("y:", y)
x = 10
print("Antes da funcao:", x)

valor()

print("Fora da funcao, valor y:", y)
"""
# cdb e lca

def calcula ():
    investimento = int(input("Digite o valor que quer investir:"))
    aplicar = float("Digite a forma de aplicar, CDB OU LCA")
    tempo = int(input("Digite quantidade de anos, 5,10,20:"))

    if aplicar == "CDB":
        valor1 = (investimento * 0.145) * tempo
       
    else:
        valor1 = (investimento * 0.15) * tempo

print("Mostra o resultado:", valor1)

        
    


  
    





