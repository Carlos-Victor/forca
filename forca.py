import desenho

palavra = input("Digite a palavra para ser descoberta: ")
dica = input("Digite a Dica para a palavra: ")
erros = 0
letra = ''
check_palavra = []
letras_chamadas = []
for create_list in range(len(palavra)):
    check_palavra.append("-")

while erros <= 6:
    desenho.imprimir_desenhos(erros), print(
        f"Dica: {dica}, Tamanho da palavra: {desenho.func_tam_palavra(str(check_palavra))}")
    letra = input("Digite uma Letra para acertar a palavra: ")
    if len(letra) > 1:
        print("Digite apenas uma letra")
    else:
        try:
            tentativa = letras_chamadas.index(letra)
            print("A letra já foi chamada tente novamente")
        except:
            try:
                tentativa = list(palavra).index(letra)
                copia_palavra = list(palavra)
                for x in range(len(palavra)):
                    try:
                        posicao = copia_palavra.index(letra)
                        check_palavra[posicao] = letra
                        copia_palavra[posicao] = '\n'
                    except:
                        pass
                letras_chamadas.append(letra)
            except:
                print("Está Letra não possui nesta palavra")
                erros = erros + 1
        if check_palavra == list(palavra):
            print(
                f"Você Acertou a Palavra: {palavra}, você chamou essas letras {letras_chamadas}, você errou {erros} para acertar!")
            break
if erros >= 6:
    print(
        f"Você Perdeu, a palavra era {palavra},você chamou essas letras {letras_chamadas}")
