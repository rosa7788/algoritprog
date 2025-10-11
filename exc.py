nome = input("Digite o nome do produto:")
valor = float(input("Digite o valor do produto:"))
quantidade = int(input("Digite a quantidade:"))
pagamento = int(input("Digite a forma de pagamento (1 - a vista) ou (2 - a prazo):"))
preco = quantidade * valor
valorFinal = 0.0
acrescimo = 0.0
parcela = 1
desconto = 0


if pagamento == 2:
    parcela = int(input("Digite a quantidade de parcelas:"))

    if pagamento <= 5:
        acrescimo = preco * 0.15
    else:
        acrescimo = preco * 0.2
else:
    desconto = preco * 0.1
    
   
    valorFinal = preco + acrescimo - desconto
    valorParcela = valorFinal / parcela
    print("Valor total:", preco)
    print("Acrescimo é:", acrescimo)
    print("O total para pagar:", valorFinal)
    print("Parcela:", parcela)
    print("Desconto:", desconto)

"""
matriz = [[1,2,3], [4,5,6],[7,8,9]]
print(matriz)

print(matriz[0][1])

matriz [0][1] = "oi"
print(matriz)
"""



    





    

