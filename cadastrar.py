
# -*- coding: utf-8 -*-

import time
from pyfingerprint.pyfingerprint import PyFingerprint


## Enrolls new finger
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

    ## Espera que a impressão digital seja lida
    while ( f.readImage() == False ):
        pass

    ## Converte a imagem lida em características e armazena-a no carregador de caracteres 1
    f.convertImage(0x01)

    ## Verifica se o dedo já está inscrito
    result = f.searchTemplate()
    positionNumber = result[0]

    if ( positionNumber >= 0 ):
        print('Impressão digital já existe na posição n°: ' + str(positionNumber))
        exit(0)

    print('Remova o dedo...')
    time.sleep(2)

    print('Insira novamente o dedo...')

    ## Espere que o dedo seja lido novamente
    while ( f.readImage() == False ):
        pass

    ## Converte a imagem lida em características e a armazena no charbuffer 2
    f.convertImage(0x02)

    ## Compara os charbuffers
    if ( f.compareCharacteristics() == 0 ):
        raise Exception('Impressões digitais não combinam!')

    ## Cria uma nova impressão digital
    f.createTemplate()

    ## Salva a impressão digital no novo número de posição
    positionNumber = f.storeTemplate()
    print('Impressão digital cadastrada com sucesso!')
    print('Nova impressão digital cadastrada na posição n°:' + str(positionNumber))

except Exception as e:
    print('Falha na operação')
    print('Mensagem de erro: ' + str(e))
    exit(1)
