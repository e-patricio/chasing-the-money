import os
from time import process_time

# Caminho para a pasta dos arquivos
pasta_mapas = "mapas"

## Função para ler os arquivos
def leitor(nome_arquivo):
    caminho_arquivo = os.path.join(pasta_mapas, nome_arquivo)
    matriz = []

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Adicionar a linha como uma lista de caracteres a matriz
            matriz.append(list(linha))
    return matriz
        
## Função que muda o sentido de leitura        
def direc(char, sentido):
    if char == '/':
        if sentido == 0:    # Se estiver indo para a direta, vai para cima 
            return 3
        elif sentido == 1:  # Se estiver indo para baixo, vai para a esquerda
            return 2
        elif sentido == 2:  # Se estiver indo para a esquerda, vai para baixo
            return 1
        else:               # Se estiver indo para cima, vai para a direita
            return 0
    else: # '\'
        if sentido == 0 or sentido == 2:   
            return sentido + 1  # Vai para o próximo sentido na lista (direita => baixo, esquerda => cima)
        else:
            return sentido - 1  # Vai para o sentido anterior na lista (baixo => direita, cima => esquerda)

## Função que junta os dígitos no caminho e monta o número     
def montante(sentido, l, c, mapa):
    digit = mapa[l][c]
    number = ''
    leap = -1 # Quantidade de casas que terão que ser puladas no mapa depois do número ser montado para não ser lido novamente
    match sentido:
        case 0: # Direita
            while digit.isdigit():
                number = str(number) + str(digit)
                c = c + 1
                digit = mapa[l][c]
                leap = leap + 1
        case 1: # Baixo
            while digit.isdigit():
                number = str(number) + str(digit)
                l = l + 1
                digit = mapa[l][c]
                leap = leap + 1
        case 2: # Esquerda
            while digit.isdigit():
                number = str(number) + str(digit)
                c = c - 1
                digit = mapa[l][c]
                leap = leap + 1
        case 3: # Cima
            while digit.isdigit():
                number = str(number) + str(digit)
                l = l - 1
                digit = mapa[l][c]
                leap = leap + 1
    retorno = [number,leap]
    return retorno

## Função que acha o início do mapa
def achaInicio(mapa, col):
    for i in range(2,col +2):
        if mapa[i][0] == '-':
            # print("Início:" +str(i))
            return i

## Função que percorre cada caractere e chama os métodos auxiliares necessários
def funcionamento(mapa):
    start = process_time()
    stringMapa= "".join(str(element) for element in mapa[0])
    tams = stringMapa.split(" ")
    quantCol = int(tams[0])
    quantLinha = int(tams[1])
    sentido = 0 # Sempre começa na direita
    co = 0
    lin = achaInicio(mapa, quantLinha)
    char = ''
    countChar = 1
    total = 0
    while char != '#':
        countChar = countChar + 1
        match sentido:
            case 0: # Direita
                co = co+1
                if mapa[lin][co] == '/' or mapa[lin][co] == '\\':
                    sentido = direc(mapa[lin][co], sentido)
                elif mapa[lin][co] == '#':
                    char = '#'
                elif mapa[lin][co].isdigit():
                    resultado = montante(sentido, lin, co, mapa)
                    result = resultado[0]
                    total = total + int(result)
                    co = co + resultado[1]
                    countChar = countChar + resultado[1]
            case 1: # Baixo
                lin = lin+1
                if mapa[lin][co] == '/' or mapa[lin][co] == '\\':
                    sentido = direc(mapa[lin][co], sentido)
                elif mapa[lin][co] == '#':
                    char = '#'
                elif mapa[lin][co].isdigit():
                    resultado = montante(sentido, lin, co, mapa)
                    total = total + int(resultado[0])
                    lin = lin + resultado[1]
                    countChar = countChar + resultado[1]
            case 2: # Esquerda
                co = co-1
                if mapa[lin][co] == '/' or mapa[lin][co] == '\\':
                    sentido = direc(mapa[lin][co], sentido)
                elif mapa[lin][co] == '#':
                    char = '#'
                elif mapa[lin][co].isdigit():
                    resultado = montante(sentido, lin, co, mapa)
                    total = total + int(resultado[0])                    
                    co = co - resultado[1]
                    countChar = countChar + resultado[1]
            case 3: # Cima
                lin = lin - 1
                if mapa[lin][co] == '/' or mapa[lin][co] == '\\':
                    sentido = direc(mapa[lin][co], sentido)
                elif mapa[lin][co] == '#':
                    char = '#'
                elif mapa[lin][co].isdigit():
                    resultado = montante(sentido, lin, co, mapa)
                    total = total + int(resultado[0])
                    lin = lin - resultado[1]
                    countChar = countChar + resultado[1]
    print("Dinheiro recolhido: " + str(total))
    end = process_time()
    t = end-start
    print("Tempo de execução: " + str(t)+"s")
    print("Total de caracteres: " + str(countChar))

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
        "9": "Sair",
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
        if opcoes[escolha] == opcoes["9"]:
            print("Encerrando... ")
        else:
            nome_arquivo = opcoes[escolha]
            mapa = leitor(nome_arquivo)  # Chama a função leitor com o nome do arquivo escolhido
            funcionamento(mapa)
            menu()
    else:
        print("Escolha inválida!")
        menu()

# Inicia o programa
menu()