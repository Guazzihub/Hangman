''' quando palavra nova é inserida o programa fecha
'''

# -*- coding: utf-8 -*-
import re
import random
import os
import time
import sys

'''
import welcome

welcome
'''

    #Função da vitória
def vit():
    os.system('CLS')
    print('\nVOCÊ ACERTOU!\n')
    print(y,'\n')
    print(r'''
                  {}
                 /__\
               /|    |\
              (_|    |_)
                 \  /
                  )(
                _|__|_
              _|______|_
             |__________|''')
    
    os.startfile('Vitoria.mp3')
    time.sleep(3)
    print('\n')
    retry()

    #Função principal
def inicio():
    global y
    vitoria = False
    derrota = False
    L = [] #Lista de letras 
    erros = 0 #Número de erros
    pos = 0 #Posição na palavra
    tentativas = 7 #contador de tentativas

    print('\n---------------------------------------------------------BEM VINDO------------------------------------------------------\n')
    print(open('regras.txt', 'r').read().upper())
    selecionador = input('\n\nSelecionar: ').lower() #Seleciona a opção

    if selecionador == 'e':
        os.system('CLS')
        opcao = input('Editar:\n1 - Número de tentativas\n2 - Inserir palavra no arquivo\n\nopção: ').upper()
        os.system('CLS')
            
        if opcao == '1':
            tentativas = int(input('Número de tentativas: ').upper())
            os.system('CLS')

        elif opcao == '2':
            print('Por favor tenha em mente que a palavra adcionada pode não ser selecionada na seguinte jogada.\n  \n- Palavras com acento não serão permitidas\n\n'.upper())     
            ap = open('Palavras.txt', 'a')
            apr = open('Palavras.txt', 'r')
            apread = apr.read().splitlines()
            os.system('CLS')
            new = input('Adcionar palavra desejada: ').lower()
            if not re.match("^[a-z]*$", new): #Não permitir acento
                print('\n--ERRO--')
                time.sleep(2)
                os.system('CLS')
                ap.close()
                inicio()
            if new not in apread and new != '': #Acionar apenas se a palavra não estiver no arquivo
                ap.write ('\n')
                ap.write (new)
                apread.close()
                ap.close()
                print('Palavra adcionada com sucesso reiniciando o programa'.upper())
                time.sleep(3)
                os.system('CLS')
                inicio()
            else:
                print('\n--ERRO AO GRAVAR--')
                time.sleep(2)
                os.system('CLS')
                inicio()
        else:
            print('--ERRO--')
            time.sleep(1)
            os.system('CLS')
            inicio()

    elif selecionador == 'a'.lower():
        os.system('CLS')
        print(open('Palavras.txt', 'r').read().upper())
        input('Pressione qualquer tecla para retornar...')
        os.system('CLS')
        inicio()

    else:
        os.system('CLS')
            
    with open('Palavras.txt', 'r') as f: #Abrir o arquivo com as palavras e chamar de 'f'
        lines = f.read().splitlines() #Ler o arquivo e separar as linhas
        f.close() #Fechar o arquivo
        palavra = list (lines) #Listar as palavras
        x = random.randrange(len(palavra))#Selecionar uma posição da lista de palavras
        y = palavra[x].upper() #Pegar a palavra selecionada (String)
        z = len(y) #Retornar numero de caracteres presentes na palavra
        campo = ["__"] * len(y) #Gerar campo com tamanho certo
        
    print('Tentativas: ', tentativas) 
    print (f'\n{campo}\n')
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    while vitoria == False and derrota == False:
        if campo == list(y): #Função vitória
            vitoria = True
            vit()
            retry()
        
        letra = input('\nDigite uma letra: ').upper()

        #Limita a quantidade de caracteres (ambos os casos)

        while len(letra) > 1 :
            os.system('CLS')
            print('Erro por favor insira apenas um caractere\n'.upper())
            print(f'\n{campo}\n\n')
            letra = input('Digite uma letra: ').upper()
        
            while not re.match("[A-Z]", letra):
                os.system('CLS')
                print ("Caractere não permitido!!!\n".upper())
                print(f'\n{campo}\n\n')
                letra = input('Digite uma letra: ').upper()
                os.system('CLS')

        while not re.match("[A-Z]", letra):
            os.system('CLS')
            print ("Caractere não permitido!!!\n".upper())
            print(f'\n{campo}\n\n')
            letra = input('Digite uma letra: ').upper()
            os.system('CLS')
    
            while len(letra) > 1 :
                os.system('CLS')
                print('Erro por favor insira apenas um caractere\n'.upper())
                print(f'\n{campo}\n\n')
                letra = input('Digite uma letra: ').upper()

        
        pos=0
        #Percorre toda a palavra em busca de letras correspondentes a letra
        if letra in y:
            os.system('CLS')
            for pos in range(z):   
                if y[pos] != letra:
                    pos = pos+1
                else:
                    campo[pos] = letra
                    pos = pos+1
            if letra not in L:
                L.append(letra)
            else:
                os.system('CLS')
                print(f'Você já utilizou a letra: {letra}\n'.upper())
                
            print(campo)
            print ('\nLetras utilizadas: ',L)
        #Senão atualizar os erros
        else:
            niveis = '''________       \n               \n        |      \n        0      \n       /|\     \n       / \     \n'''
              
            if erros < len (niveis) and letra not in L :#\\\!!!erro das tentativas!!!///                    
                os.system('CLS')
                print('Letra não encontrada\n'.upper())
                erros = erros +1
                tentativas = tentativas -1
                print ('Erros: ', erros)
                print ('\nTentativas restantes = ',tentativas, '\n')
                print (campo,'\n')
                print (niveis[0:erros*15])
                
            if tentativas == 0:
                derrota == True
                time.sleep(1)
                os.system('CLS')
                print('ERROU!\n')
                print(y,'\n')
                os.startfile('Errou.mp3')
                time.sleep(3)
                retry()

            if letra in L:
                os.system('CLS')
                print(campo,'\n')
                print(f'\nVocê já utilizou a letra: {letra}\n'.upper())
                
            else:
                L.append (letra)
            print ('Letras utilizadas: ',L,'\n')
                

def retry():
    global novamente
    novamente = ''
    vitoria = False
    derrota = False
    novamente = input ('Você gostaria de tentar novamente?(s/n): ').lower()
    if novamente == 's':
        L = []
        os.system('CLS')
        ciclo()
    if novamente == 'n':
        print('\nMuito obrigado por ter jogado')
        time.sleep(2)
        sys.exit(0)
    else:
        print ('ERRO')
        retry()

def ciclo(): #Caso novamente = 's' reiniciar o ciclo        
    inicio()
    retry()

ciclo()
