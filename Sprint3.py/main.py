import json
import os
import random

# Arquivos de armazenamento
ARQUIVO_MAMADEIRAS = "pedidos_mamadeiras.json"
ARQUIVO_REMEDIOS = "pedidos_remedios.json"

def carregar_pedidos(arquivo):
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar {arquivo}: {e}")
    return []

def salvar_pedidos(arquivo, pedidos):
    try:
        with open(arquivo, 'w') as f:
            json.dump(pedidos, f)
    except Exception as e:
        print(f"Erro ao salvar {arquivo}: {e}")

def solicitar_mamadeira(pedidos):
    nome_bebe = input("Digite o nome do bebê: ").strip()
    if not nome_bebe:
        print("Nome do bebê não pode estar vazio.\n")
        return
    try:
        quantidade = int(input("Digite a quantidade de mamadeiras: "))
        pedido = {"nome_bebe": nome_bebe, "quantidade": quantidade}
        pedidos.append(pedido)
        salvar_pedidos(ARQUIVO_MAMADEIRAS, pedidos)
        print(f"Pedido registrado: {nome_bebe} - {quantidade} mamadeira(s)\n")
    except ValueError:
        print("Erro: Digite um número válido para a quantidade.\n")

def solicitar_remedio(pedidos):
    nome_bebe = input("Digite o nome do bebê: ").strip()
    remedio = input("Digite o nome do remédio: ").strip()
    if not nome_bebe or not remedio:
        print("Erro: Nome do bebê e do remédio não podem estar vazios.\n")
        return
    pedido = {"nome_bebe": nome_bebe, "remedio": remedio}
    pedidos.append(pedido)
    salvar_pedidos(ARQUIVO_REMEDIOS, pedidos)
    print(f"Pedido de remédio registrado: {nome_bebe} - {remedio}\n")

def chamar_enfermeira():
    motivo = input("Digite o motivo para chamar a enfermeira ou médico: ").strip()
    if motivo:
        print(f"Chamando a enfermeira/médico... Motivo: {motivo}\n")
    else:
        print("Motivo não pode estar vazio.\n")

def listar_pedidos(pedidos_mamadeiras, pedidos_remedios):
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

def exibir_status(pedidos_mamadeiras, pedidos_remedios):
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

def main():
    pedidos_mamadeiras = carregar_pedidos(ARQUIVO_MAMADEIRAS)
    pedidos_remedios = carregar_pedidos(ARQUIVO_REMEDIOS)

    quarto = input("Digite o número do quarto: ")
    nome_usuario = input("Digite seu nome: ")
    print(f"Bem-vindo(a), {nome_usuario}! Você está no quarto {quarto}.\n")

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
            solicitar_mamadeira(pedidos_mamadeiras)
        elif opcao == "2":
            chamar_enfermeira()
        elif opcao == "3":
            solicitar_remedio(pedidos_remedios)
        elif opcao == "4":
            listar_pedidos(pedidos_mamadeiras, pedidos_remedios)
        elif opcao == "5":
            exibir_status(pedidos_mamadeiras, pedidos_remedios)
        elif opcao == "6":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    main()
