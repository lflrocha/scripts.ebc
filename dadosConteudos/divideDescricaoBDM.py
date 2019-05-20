#!/usr/bin/python
# -*- coding: UTF-8 -*-


##$##"250"###"2013/12/20"###"19/12/2013 - o Bom Dia Ministro, Gilberto Carvalho falou sobre Programa Nacional 
#de Apoio ao Associativismo e Cooperativismo Social, Plano Juventude Viva e Política Nacional de Participação 
#Social"###"O Bom Dia, Ministro desta sexta-feira (20) recebeu o Ministro Chefe da Secretaria Geral da Presidência 
#da República, Gilberto Carvalho. O ministro falou sobre o Programa Nacional de Apoio ao Associativismo e 
#Cooperativismo Social, o Plano Juventude Viva, a Política Nacional de Participação Social e outros programas, 
#como Pró-Catador e o Cataforte.#$$$#

import os
import datetime

diretorio = '/Users/lflrocha/Desktop/conteudos/BomDiaMinistro/'

os.system('find ' + diretorio + ' -name .DS_Store -delete');
os.system('find ' + diretorio + ' -name ._* -delete');

dirList = [f for f in os.listdir(diretorio) if f.endswith('.mp3')]


fArq = open('/Users/lflrocha/Desktop/conteudos/t_bdm_transcricao3.txt')
descricoes = fArq.readlines()

for descricao in descricoes:
	aux = descricao.split('"###"')
	
	nomeArq = aux[1].replace('/','-')
	
	for n in dirList:
		if nomeArq in n:
			nomeArq = n.replace('.mp3','')
	
	
	texto = aux[3].replace('#$$$#','')

	print nomeArq
	
	fOut = open(diretorio+nomeArq+'.txt', 'w')
	fOut.write(texto)
	fOut.close()


