"""
Projeto entregável final
Aluno: Akira Higashi  10/Nov/2023
Exercicio Crie um programa que simula um jogo de dados, onde vários jogadores jogam um dado e têm resultados aleatórios
"""
# biblioteca
import random
# cadastro dos jogadores
jogadores = []
# retorna tt vitórias do jogador
def tt_vitorias(jogador):
    return jogador["Vitorias"]

####coleta dados#########################################################
# informações do jogo
print("\n <<< JOGO DE DADOS >>>")
tt_jogadores = int(input("Quantos JOGADORES vão jogar? "))
tt_rodadas = int(input("Quantas RODADAS vc quer jogar? "))

# nome dos jogadores
for i in range(tt_jogadores):
    nome = input(f"Digite o nome do jogador {i + 1}: ")
    jogadores.append({"Nome": nome, "Vitorias": 0, "Resultados": []})
    #print(jogadores)       #debug JOGADORES ATE O MOMENTO

####jogadas#########################################################
for rodada in range(tt_rodadas):                       # Para cada rodada
    print(f"\nRodada {rodada + 1}:")

    # joga o dado/armazena e busca qual o maior valor da rodada
    resultados = []                                     # inicializa lista de resultados da rodada atual
    for i in range(1, tt_jogadores+1):                  # para cada jogador
        resultado = random.randrange(1, 7)              # joga o dado e guarda em resultado
        resultados.append(resultado)                    # adiciona o resultado à lista de resultados da rodada
    max_resultado = max(resultados)                     # busca o maior resultado da rodada
    #print(resultados)           #debug TODOS OS RESULTADOS DA RODADA
    #print(max_resultado)        #debug MAIOR VALOR DA RODADA

    # busca quem é o vencedor e armazena
    vencedores = []                                     # inicializa lista de vencedores da rodada atual
    for i, resultado in enumerate(resultados):          # Para cada resultado na lista de resultados da rodada
        if resultado == max_resultado:                  # Se o resultado for igual ao máximo
            vencedores.append(jogadores[i])             # Adiciona o jogador correspondente à lista de vencedores
    #print(vencedores)       #debug dicionario dos VENCEDORES ate o momento

    for i, jogador in enumerate(jogadores):             # Para cada jogador
        print(f"{jogador['Nome']} : {resultados[i]}")   # Exibir o resultado do jogador

    vencedores_nomes = []                               # Inicializar a lista de nomes dos vencedores
    for vencedor in vencedores:                         # Para cada vencedor da rodada
        vencedor["Vitorias"] += 1                       # Incrementar o contador de vitórias do jogador
        vencedores_nomes.append(vencedor["Nome"])       # Adicionar o nome do vencedor à lista de nomes
    #print(vencedores)           #debug IMPRIME O VENCEDORES E SEUS DADOS ex [{'Nome': 'Jun', 'Vitorias': 2, 'Resultados': []}]
        
    print(f"Vencedor(es) : {vencedores_nomes}")  # Exibir o(s) vencedor(es) da rodada ex:  

# listar em ordem descrescente, onde os maiores pontuadores virão primeiro
# com isso saberemos que será(ão) o(s) vencedor(es)
jogadores.sort(key=tt_vitorias, reverse=True)

###finalizacao#######################################################
# Exibir o resultado final do jogo
print("\nResultado das rodadas:")
for jogador in jogadores:                                           # Mostrar o número de vitórias de cada jogador
    print(f"{jogador['Nome']} : {jogador['Vitorias']} vitória(s) ")  

# Exibir o vencedor do jogo
if len(jogadores) > 1:                                              # Houve mais de 1 jogador na partida?
    if jogadores[0]["Vitorias"] != jogadores[1]["Vitorias"]:        # teve somente um vitorioso ?
        print(f"\n<<< O Campeão é {jogadores[0]['Nome']} >>>\n")    # mostrar o vencedor do jogo
    else:
        print("\n!! Houve um empate !!\n")                          # caso contrario houve empate
#####################################################################
 
