""""
# Programa: Cálculo de desconto em loja online

# Entrada de dados
idade = int(input("Informe sua idade: "))
valor_compra = float(input("Informe o valor total da compra (R$): "))

# Inicialização dos descontos
desconto_base = 0
desconto_adicional = 0

# Verifica o desconto base
if valor_compra > 500:
    desconto_base = 0.15  # 15%
elif valor_compra > 200:
    desconto_base = 0.10  # 10%
else:
    desconto_base = 0     # Sem desconto base

# Verifica se o cliente é estudante (<25) ou sênior (≥60)
if idade < 25:
    desconto_adicional = 0.05  # 5% adicional
elif idade >= 60:
    desconto_adicional = 0.07  # 7% adicional

# Calcula o valor final
valor_desconto_base = valor_compra * desconto_base
valor_desconto_adicional = valor_compra * desconto_adicional
valor_total_descontos = valor_desconto_base + valor_desconto_adicional
valor_final = valor_compra - valor_total_descontos

# Saída formatada
print("\n--- RESUMO DA COMPRA ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto base: R$ {valor_desconto_base:.2f}")
print(f"Desconto adicional: R$ {valor_desconto_adicional:.2f}")
print(f"Valor total de descontos: R$ {valor_total_descontos:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
"""
"""
# Programa: Cadastro de notas de alunos com relatório estatístico

alunos = []  # Lista para armazenar dicionários com nome e nota

while True:
    nome = input("Digite o nome do aluno: ").strip()
    
    # Validação da nota
    while True:
        try:
            nota = float(input(f"Digite a nota de {nome} (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Erro: a nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    
    # Adiciona o aluno à lista
    alunos.append({"nome": nome, "nota": nota})
    
    # Pergunta se o usuário quer continuar
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != 'sim':
        break

# --- Cálculos estatísticos ---
quantidade = len(alunos)
notas = [a["nota"] for a in alunos]
media = sum(notas) / quantidade if quantidade > 0 else 0
maior = max(notas) if quantidade > 0 else 0
menor = min(notas) if quantidade > 0 else 0
aprovados = [a for a in alunos if a["nota"] >= 7]
percentual_aprovados = (len(aprovados) / quantidade * 100) if quantidade > 0 else 0

# --- Relatório final ---
print("\n--- RELATÓRIO FINAL ---")
print(f"Quantidade de alunos cadastrados: {quantidade}")
print(f"Média geral das notas: {media:.2f}")
print(f"Maior nota: {maior:.2f}")
print(f"Menor nota: {menor:.2f}")
print(f"Porcentagem de aprovados: {percentual_aprovados:.1f}%")

print("\n--- SITUAÇÃO DOS ALUNOS ---")
for a in alunos:
    situacao = "Aprovado " if a["nota"] >= 7 else "Reprovado "
    print(f"{a['nome']:<20} - Nota: {a['nota']:.1f} - {situacao}")
"""
"""
# Função para calcular a moda
def calcular_moda(lista):
    from collections import Counter
    
    # Conta quantas vezes cada número aparece
    contagem = Counter(lista)
    
    # Encontra a frequência máxima
    max_frequencia = max(contagem.values())
    
    # Pega todos os números com essa frequência
    numeros_mais_frequentes = [num for num, freq in contagem.items() if freq == max_frequencia]
    
    # Se houver mais de um número com frequência máxima, não há moda
    if len(numeros_mais_frequentes) > 1:
        return None
    else:
        return numeros_mais_frequentes[0]


# Programa principal
numeros = []

print("Digite números positivos (digite 0 para encerrar):")

while True:
    try:
        n = int(input("Número: "))
        if n < 0:
            print("Digite apenas números *positivos*.")
        elif n == 0:
            break
        else:
            numeros.append(n)
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# Verifica se a lista não está vazia
if len(numeros) == 0:
    print("Nenhum número foi informado.")
else:
    moda = calcular_moda(numeros)
    if moda is None:
        print("\nNão existe moda (há empate na frequência máxima).")
    else:
        print(f"\nA moda do vetor é: {moda}")
"""


