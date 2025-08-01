Na matriz de 20 × 20 abaixo, quatro números ao longo de uma diagonal foram marcados em negrito. O produto desses números é 26 × 63 × 78 × 14 = 1788696. Qual é o maior produto de quatro números adjacentes em qualquer direção (vertical, horizontal ou diagonal) na matriz de 20 × 20? A matriz 20 × 20 será dada como entrada, e o programa deve exibir o valor da multiplicação, a posição (linha e coluna) de onde começam os números, e a direção (cima, baixo, esquerda, direita, direita cima, esquerda cima, direita baixo, esquerda baixo). No caso da matriz abaixo, o maior número é 89 × 94 × 97 × 87 = 70600674, começando na posição de linha 12 e coluna 6, e na diagonal esquerda baixo.

def fazerMatriz(l, c):
    ma = []
    for i in range(l):
        a = []
        for j in range(c):
            a.append(int(input()))

        ma.append(a)
    return ma


def descobrirPadrao(matriz, i, j):
    # Não faz sentido descobrir os padrões cima, cima esquerda ou cima direita
    produtoD = produtoB = produtoBD = produtoBE = 1
    direcao = ""

    for k in range(i, i + 4):
        for l in range(j, j + 4):  
            # Ignorar posições inválidas
            if k < 0 or k > 19 or l < 0 or l > 19:
                pass
            else:
                # Horizontal
                if k == i:
                    produtoD *= matriz[k][l]
                # Vertical
                if l == j:
                    produtoB *= matriz[k][l]

    # Diagonais
    if i < 16 and j < 16:
        produtoBD = matriz[i][j] * matriz[i + 1][j + 1] * matriz[i + 2][j + 2] * matriz[i + 3][j + 3]
    
    if j > 3 and i <= 16:
        produtoBE = matriz[i][j] * matriz[i + 1][j - 1] * matriz[i + 2][j - 2] * matriz[i + 3][j - 3] 

    produtos = [produtoD, produtoB, produtoBE, produtoBD]
    
    # Descobrindo o maior
    maior = produtos[0]
    for e in range(len(produtos)):
        if produtos[e] >= maior:
            maior = produtos[e]
            if e == 0:
                direcao = "direita"
            elif e == 1:
                direcao = "baixo"
            elif e == 2:
                direcao = "esquerda baixo"
            elif e == 3:
                direcao = "direita baixo"
    
    produto = maior
    
    return produto, direcao


def acharProduto(matriz):
    maior = float("-inf")
    direcao = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            produto, d = descobrirPadrao(matriz, i, j)
            if produto > maior:
                maior = produto
                posicaoI = i
                posicaoJ = j
                direcao = d

    return maior, posicaoI, posicaoJ, direcao
            

def main():
    m = fazerMatriz(20, 20)
    produto, i, j, direcao = acharProduto(m)

    print(produto)
    print(i)
    print(j)
    print(direcao)


main()
