import random


def jogar():

    bem_vindo()
    arquivo_palavras()

    palavra_secreta = arquivo_palavras()
    tentativas = 0
    nivel = 0
    list = []
    list[:] = "_" * len(palavra_secreta)

    #dificuldade do jogo
    while not nivel :

        nivel = int(input("\nescolha o nível de dificuldade: \nHard (1)\nMedium (2)\nEasy (3)\n>>> "))

        if nivel == 1:
            tentativas = 3
            print("\nVocê escolheu o nível hard, portanto, possuí {} tentativas".format(tentativas))
            nivel = True
        elif nivel == 2:

            tentativas = 5
            print("Você escolheu o nível medium, portanto, possuí {} tentativas".format(tentativas))
            nivel = True
        elif nivel == 3:
            tentativas = 10
            print("\nVocê escolheu o nível easy, portanto, possuí {} tentativas".format(tentativas))
            nivel = True

        else:
            nivel = False

    #variável de contagem do loop while
    cont = 0
    #início
    while cont == 0:

        #variável para capturar a letra informada
        chute = input("digite uma letra ou a palavra: ")
        chute = chute.strip().lower()

        #blocos de teste
        if chute not in palavra_secreta:
            print("a letra {} não está na palavra secreta".format(chute))
            tentativas -= 1
            print("você possui mais {} tentativas".format(tentativas))

        elif tentativas <= 0:
            print("você foi enforcado")
            break

        elif chute == palavra_secreta:
            print("você descobriu a palavra secreta")
            break

        else:
            i = 0
            #iterando as letras captadas e adicionando nas posições
            for x in palavra_secreta:

                if chute == x:
                    list[i] = x
                    print("\n...\nencontrei a letra {} na posição {}".format(x, i+1) ,end= " ")
                    print(">>>", list, "\n")

                #usando a lista 2 do começo, verifica se a palavra foi completada
                elif "_" not in list:
                    print(tuple(list))
                    print("você acertou a palavra")
                    break

                i += 1


    print("Fim do jogo")

def bem_vindo():
    print("*********************************")
    print("**********jogo da Forca!*********")
    print("*********************************")

def arquivo_palavras():
    # abrindo o arquivo txt
    arquivo = open("palavras.txt", "r")
    # armazinando em uma lista o conteudo do arquivo
    lista_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)
    arquivo.close()
    # randomizando os valores desse arquivo agora na lista, a fim de gerar uma palvra secreta aleatória
    index_palvra_sorteada = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[index_palvra_sorteada]

    return palavra_secreta

if(__name__ == "__main__"):
    jogar()