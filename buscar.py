
# -*- coding: utf-8 -*-

import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint


## Pesquisar por uma impressão digital
##

## Tenta inicializar o sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('A senha do sensor de impressão digital está errada!')

except Exception as e:
    print('O sensor de impressão digital não pôde ser inicializado!')
    print('Mensagem de erro: ' + str(e))
    exit(1)

## Obtém algumas informações do sensor
print('Modelos usados atualmente: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tenta pesquisar a impressão digital e calcular o hash
try:
    print('Aguardando impressão digital...')

    ## Espere que a impressão digital seja lida
    while ( f.readImage() == False ):
        pass

    ## Converte a imagem lida em características e armazena-a no carregador de caracteres 1
    f.convertImage(0x01)

    ## Modelo de pesquisa
    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        print('Nenhuma combinação encontrada!')
        exit(0)
    else:
        print('Impressão digital encontrada na posição n°: ' + str(positionNumber))
        print('A pontuação de precisão é: ' + str(accuracyScore))

    ## OPTIONAL stuff
    ##

    ## Carrega o modelo encontrado para o charbuffer 1
    f.loadTemplate(positionNumber, 0x01)

    ## Faz o download das características da impressão digital carregado no charbuffer 1
    characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

    ## Hashes características da impressão digital
    print('SHA-2 hash da impressão digital: ' + hashlib.sha256(characterics).hexdigest())

except Exception as e:
    print('Falha na operação!')
    print('Mensagem de erro: ' + str(e))
    exit(1)
