import os

# Caminho para a pasta dos arquivos
pasta_mapas = "mapas"

## Função para ler os arquivos
def leitor(nome_arquivo):
    caminho_arquivo = os.path.join(pasta_mapas, nome_arquivo)
    matriz = []

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Remover caracteres de quebra de linha e espaços em branco
            linha = linha.strip()
            # Adicionar a linha como uma lista de caracteres a matriz
            matriz.append(list(linha))

    # Imprimir a matriz
    for linha in matriz:
        print("".join(linha))

## Função para exibir o menu e processar a escolha do usuário
def menu():
    opcoes = {
        "1": "casoG50.txt",
        "2": "casoG100.txt",
        "3": "casoG200.txt",
        "4": "casoG500.txt",
        "5": "casoG750.txt",
        "6": "casoG1000.txt",
        "7": "casoG1500.txt",
        "8": "casoG2000.txt",
    }

    print("Siga o dinheiro! (>_<)")
    print("========================================")
    print("       > Casos disponíveis: <3")
    print("    1. Caso G50    |   5. Caso G750")
    print("    2. Caso G100   |   6. Caso G1000")
    print("    3. Caso G200   |   7. Caso G1500")
    print("    4. Caso G500   |   8. Caso G2000")

    escolha = input("Digite o número do caso desejado: ")
    print("========================================")

    # Verifica se a escolha do usuário é válida
    if escolha in opcoes:
        nome_arquivo = opcoes[escolha]
        leitor(nome_arquivo)  # Chama a função leitor com o nome do arquivo escolhido
    else:
        print("Escolha inválida!")

# Inicia o programa
menu()
