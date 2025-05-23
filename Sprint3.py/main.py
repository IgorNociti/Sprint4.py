import json
import os
import random

"""
Importação de bibliotecas:
- json: para salvar e carregar os pedidos de forma estruturada
- os: para verificar se os arquivos existem
- random: para gerar estimativas de tempo aleatórias
"""

# Arquivos onde os pedidos serão salvos
ARQUIVO_MAMADEIRAS = "pedidos_mamadeiras.txt"
ARQUIVO_REMEDIOS = "pedidos_remedios.txt"

# Estrutura de dados: listas contendo dicionários com os pedidos
pedidos_mamadeiras = []
pedidos_remedios = []

"""
Carrega os pedidos salvos em arquivos (se existirem) para as listas de pedidos
"""
def carregar_pedidos():
    global pedidos_mamadeiras, pedidos_remedios
    try:
        if os.path.exists(ARQUIVO_MAMADEIRAS):
            with open(ARQUIVO_MAMADEIRAS, 'r') as f:
                pedidos_mamadeiras.extend(json.load(f))
        if os.path.exists(ARQUIVO_REMEDIOS):
            with open(ARQUIVO_REMEDIOS, 'r') as f:
                pedidos_remedios.extend(json.load(f))
    except Exception as e:
        print(f"Erro ao carregar arquivos: {e}")

"""
Salva os pedidos atuais nos arquivos .txt usando o formato JSON
"""
def salvar_pedidos():
    try:
        with open(ARQUIVO_MAMADEIRAS, 'w') as f:
            json.dump(pedidos_mamadeiras, f)
        with open(ARQUIVO_REMEDIOS, 'w') as f:
            json.dump(pedidos_remedios, f)
    except Exception as e:
        print(f"Erro ao salvar arquivos: {e}")

"""
Função para registrar pedido de mamadeira, com validação numérica
"""
def solicitar_mamadeira():
    try:
        nome_bebe = input("Digite o nome do bebê: ")
        quantidade = int(input("Digite a quantidade de mamadeiras: "))
        pedido = {"nome_bebe": nome_bebe, "quantidade": quantidade}
        pedidos_mamadeiras.append(pedido)
        salvar_pedidos()
        print(f"Pedido registrado: {nome_bebe} - {quantidade} mamadeira(s)\n")
    except ValueError:
        print("Erro: Digite um número válido para a quantidade.\n")

"""
Função para registrar pedido de remédio
"""
def solicitar_remedio():
    nome_bebe = input("Digite o nome do bebê: ")
    remedio = input("Digite o nome do remédio: ")
    pedido = {"nome_bebe": nome_bebe, "remedio": remedio}
    pedidos_remedios.append(pedido)
    salvar_pedidos()
    print(f"Pedido de remédio registrado: {nome_bebe} - {remedio}\n")

"""
Função para chamar uma enfermeira ou médico
"""
def chamar_enfermeira():
    motivo = input("Digite o motivo para chamar a enfermeira ou médico: ")
    print(f"Chamando a enfermeira/médico... Motivo: {motivo}\n")

"""
Exibe todos os pedidos pendentes de mamadeiras e remédios
"""
def listar_pedidos():
    print("\n--- Pedidos Pendentes ---")
    if pedidos_mamadeiras:
        print("Mamadeiras:")
        for i, p in enumerate(pedidos_mamadeiras, 1):
            print(f"{i}. {p['nome_bebe']} - {p['quantidade']} mamadeira(s)")
    if pedidos_remedios:
        print("\nRemédios:")
        for i, p in enumerate(pedidos_remedios, 1):
            print(f"{i}. {p['nome_bebe']} - {p['remedio']}")
    if not pedidos_mamadeiras and not pedidos_remedios:
        print("Nenhum pedido pendente.")
    print()

"""
Mostra a estimativa de tempo para entrega dos pedidos (como no iFood)
"""
def exibir_status():
    print("\n--- Status dos Pedidos ---")
    if not pedidos_mamadeiras and not pedidos_remedios:
        print("Nenhum pedido em andamento.\n")
        return

    if pedidos_mamadeiras:
        print("Mamadeiras:")
        for p in pedidos_mamadeiras:
            tempo = random.randint(5, 15)
            print(f"{p['nome_bebe']} - {p['quantidade']} mamadeira(s) | Estimativa: {tempo} minutos")

    if pedidos_remedios:
        print("\nRemédios:")
        for p in pedidos_remedios:
            tempo = random.randint(10, 20)
            print(f"{p['nome_bebe']} - {p['remedio']} | Estimativa: {tempo} minutos")
    print()

"""
Início do sistema: coleta nome e número do quarto
"""
carregar_pedidos()

quarto = input("Digite o número do quarto: ")
nome_usuario = input("Digite seu nome: ")
print(f"Bem-vindo(a), {nome_usuario}! Você está no quarto {quarto}.\n")

"""
Menu principal do sistema
"""
while True:
    print("\n--- Sistema Baby Kitchen ---")
    print("1. Solicitar mamadeira")
    print("2. Chamar enfermeira/médico")
    print("3. Solicitar remédio")
    print("4. Listar pedidos")
    print("5. Ver status dos pedidos")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        solicitar_mamadeira()
    elif opcao == "2":
        chamar_enfermeira()
    elif opcao == "3":
        solicitar_remedio()
    elif opcao == "4":
        listar_pedidos()
    elif opcao == "5":
        exibir_status()
    elif opcao == "6":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida, tente novamente.\n")
