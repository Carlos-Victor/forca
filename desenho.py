def forca_normal():
    print("###########################################################")
    print("_______________________")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")

def cabeça():
    print("#############################")
    print("_______________________")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                    _|_")
    print("|                   |___|")
    print("|")
    print("|")
    print("|")
    print("|")


def tronco():
    print("#############################")
    print("_______________________")
    print("|                     |")
    print("|                    _|_")
    print("|                   |___|")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                      ")
    print("|                      ")


def perna_esquerda():
    print("#############################")
    print("_______________________")
    print("|                     |")
    print("|                    _|_")
    print("|                   |___|")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                      \ ")
    print("|                       \ ")

def perna_direita():
    print("#############################")
    print("_______________________")
    print("|                     |")
    print("|                    _|_")
    print("|                   |___|")
    print("|                     |")
    print("|                     |")
    print("|                     |")
    print("|                    / \ ")
    print("|                   /   \ ")

def braco_esquerdo():
    print("#############################")
    print("_______________________")
    print("|                     |")
    print("|                    _|_")
    print("|                   |___|")
    print("|                     |")
    print("|                     |\ ")
    print("|                     | \ ")
    print("|                    / \ ")
    print("|                   /   \ ")

def braco_direito():
    print("#############################")
    print("_______________________")
    print("|                     |")
    print("|                    _|_")
    print("|                   |___|")
    print("|                     |")
    print("|                    /|\ ")
    print("|                   / | \ ")
    print("|                    / \ ")
    print("|                   /   \ ")


def imprimir_desenhos(erros):
    if erros == 0:
        return forca_normal()
    if erros == 1:
        return cabeça()
    if erros == 2:
        return tronco()
    if erros == 3:
        return perna_esquerda()
    if erros == 4:
        return perna_direita()
    if erros == 5:
        return braco_esquerdo()
    if erros == 6:
        return braco_direito()


def func_tam_palavra(palavra):
    remove_virgula = palavra.replace(',','')
    remove_cochete = remove_virgula.replace('[','')
    palavra = remove_cochete.replace(']','')
    return palavra