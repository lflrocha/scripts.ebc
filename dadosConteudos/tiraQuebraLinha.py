#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

linhas = open('/Users/lflrocha/Desktop/t_voz_transcricao.txt','r').readlines()
saida = open('/Users/lflrocha/Desktop/t_voz_transcricao2.txt','w')

conteudo = {}

linhas = linhas.replace('\n',' ')
linhas = linhas.replace('<br>                                    ','\n')


for linha in linhas:
	a = linha.split('###',1)
	b = a[1].split('###')
	data = b[0].replace('"','')
	texto = b[2]
	conteudo[data] = texto


out = ''	
for key in sorted(conteudo.iterkeys()):	
	out = out + key + "###" + conteudo[key]

saida.write(out)







