# -*- coding: utf-8 -*-


#Casos de teste
N = int(input());

for i in range(0,N):
    palavra = input();
    quantity = int(input())
    new_word = ''
    for j in palavra:
        posicao = ord(j) - quantity
        if(posicao < 65):
            new_word += chr(91-(65-posicao))
        else:
            new_word += chr(ord(j)-quantity)
    print(new_word)