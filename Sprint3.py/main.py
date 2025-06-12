import json
import os
import random

"""
Constantes com os nomes dos arquivos onde os pedidos serão armazenados.
"""
ARQUIVO_MAMADEIRAS = "pedidos_mamadeiras.json"
ARQUIVO_REMEDIOS = "pedidos_remedios.json"

# ------------------ Funções utilitárias ------------------

def carregar_pedidos(arquivo):
    """
    Carrega pedidos de um arquivo JSON, se existir.
    Retorna uma lista de pedidos ou lista vazia se o arquivo não existir ou estiver corrompido.
    """
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"[Erro] Falha ao carregar {arquivo}: {e}")
    return []

def salvar_pedidos(arquivo, pedidos):
    """
    Salva a lista de pedidos no arquivo JSON correspondente.
    Usa indentação para facilitar a leitura manual do arquivo.
    """
    try:
        with open(arquivo, 'w') as f:
            json.dump(pedidos, f, indent=4)
    except Exception as e:
        print(f"[Erro] Falha ao salvar {arquivo}: {e}")

# ------------------ Entrada de pedidos ------------------

def solicitar_pedido_mamadeira():
    """
    Solicita ao usuário o nome do bebê e a quantidade de mamadeiras.
    Retorna um dicionário com os dados do pedido ou None em caso de erro.
    """
    nome = input("Nome do bebê: ").strip()
    if not nome:
        print("Nome não pode estar vazio.\n")
        return None
    try:
        quantidade = int(input("Quantidade de mamadeiras: "))
        return {"nome_bebe": nome, "quantidade": quantidade}
    except ValueError:
        print("Erro: digite um número válido.\n")
        return None

def solicitar_pedido_remedio():
    """
    Solicita ao usuário o nome do bebê e o nome do remédio.
    Retorna um dicionário com os dados do pedido ou None em caso de erro.
    """
    nome = input("Nome do bebê: ").strip()
    remedio = input("Nome do remédio: ").strip()
    if not nome or not remedio:
        print("Nome do bebê e do remédio são obrigatórios.\n")
        return None
    return {"nome_bebe": nome, "remedio": remedio}

# ------------------ Outras ações ------------------

def chamar_enfermeira():
    """
    Solicita um motivo ao usuário e simula a chamada de uma enfermeira ou médico.
    """
    motivo = input("Motivo para chamar a enfermeira/médico: ").strip()
    if motivo:
        print(f"\n[!] Enfermeira/médico sendo chamado. Motivo: {motivo}\n")
    else:
        print("Motivo não pode estar vazio.\n")

def listar_pedidos(mamadeiras, remedios):
    """
    Lista todos os pedidos pendentes de mamadeiras e remédios.
    """
    print("\n--- Pedidos Pendentes ---")
    if mamadeiras:
        print("Mamadeiras:")
        for i, p in enumerate(mamadeiras, 1):
            print(f"{i}. {p['nome_bebe']} - {p['quantidade']} mamadeira(s)")
    if remedios:
        print("\nRemédios:")
        for i, p in enumerate(remedios, 1):
            print(f"{i}. {p['nome_bebe']} - {p['remedio']}")
    if not mamadeiras and not remedios:
        print("Nenhum pedido pendente.")
    print()

def exibir_status(mamadeiras, remedios):
    """
    Exibe o status dos pedidos com uma estimativa de tempo de entrega aleatória.
    """
    print("\n--- Status dos Pedidos ---")
    if not mamadeiras and not remedios:
        print("Nenhum pedido em andamento.\n")
        return

    if mamadeiras:
        print("Mamadeiras:")
        for p in mamadeiras:
            tempo = random.randint(5, 15)
            print(f"{p['nome_bebe']} - {p['quantidade']} mamadeira(s) | Estimativa: {tempo} min")

    if remedios:
        print("\nRemédios:")
        for p in remedios:
            tempo = random.randint(10, 20)
            print(f"{p['nome_bebe']} - {p['remedio']} | Estimativa: {tempo} min")
    print()

# ------------------ Programa principal ------------------

def main():
    """
    Função principal do sistema.
    Inicializa o programa, carrega os dados e exibe o menu de opções.
    Gerencia o fluxo de interação com o usuário.
    """
    pedidos_mamadeiras = carregar_pedidos(ARQUIVO_MAMADEIRAS)
    pedidos_remedios = carregar_pedidos(ARQUIVO_REMEDIOS)

    quarto = input("Número do quarto: ")
    nome_usuario = input("Seu nome: ")
    print(f"\nBem-vindo(a), {nome_usuario}! Quarto {quarto}.\n")

    while True:
        print("--- Sistema Baby Kitchen ---")
        print("1. Solicitar mamadeira")
        print("2. Chamar enfermeira/médico")
        print("3. Solicitar remédio")
        print("4. Listar pedidos")
        print("5. Ver status dos pedidos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pedido = solicitar_pedido_mamadeira()
            if pedido:
                pedidos_mamadeiras.append(pedido)
                salvar_pedidos(ARQUIVO_MAMADEIRAS, pedidos_mamadeiras)
                print(f"Pedido registrado: {pedido['nome_bebe']} - {pedido['quantidade']} mamadeira(s)\n")

        elif opcao == "2":
            chamar_enfermeira()

        elif opcao == "3":
            pedido = solicitar_pedido_remedio()
            if pedido:
                pedidos_remedios.append(pedido)
                salvar_pedidos(ARQUIVO_REMEDIOS, pedidos_remedios)
                print(f"Pedido de remédio registrado: {pedido['nome_bebe']} - {pedido['remedio']}\n")

        elif opcao == "4":
            listar_pedidos(pedidos_mamadeiras, pedidos_remedios)

        elif opcao == "5":
            exibir_status(pedidos_mamadeiras, pedidos_remedios)

        elif opcao == "6":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida, tente novamente.\n")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
