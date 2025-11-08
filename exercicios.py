"""
#lower() = deixa minusculo
def calcula (a, b, operacao):
    if operacao == "somar":
        return a + b
    elif operacao == "subtrair":
        return a - b
    elif operacao == "multiplicar":
        return a * b
    elif operacao == "dividir":
        return a / b
    
o = input("Digite a operacao:").strip() #strip remove espaco antes e depois
valor1 = int(input("Valor 1:"))
valor2 = int(input("Valor 2:"))

print("Resultado", calcula(valor1, valor2, o))
"""
"""
def vogais (texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador
    
    
entrada = input("Digite um texto:")
quantidade = vogais(entrada)
print(f"O texto contém {quantidade} vogais.")
"""
"""
def calcularMedia(numeros):
    soma = 0
    cont = 0
    for n in numeros:
        soma = soma + n
        cont = cont + 1

    return soma / cont

    
lista = [2,4,5,7,8]
print("Tamanho:", len(lista))


def mediaPonderada(numeros,pesos):
    for n in range(5):
        print(n)
lista = [2,4,5,7,8]
peso = [1,1,2,3,1]

media = calcularMedia(lista)
print("media:", media)

mediaP = mediaPonderada(lista, peso)
"""
def incluir(lista, cod, desc, valor):
    lista.append ({ 'cod' : cod,
        'desc': desc,
        'valor': valor })
    lista = []
        
    
    incluir(lista,111,'tv', 1999.99)
    incluir(lista,222,'geladeira',2500.0)

    print(lista)











    


    





        





