#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''  
###$##"0"###"2009/02/12"###"12/02/09 Voz do Brasil"###"Cerca de quarenta e seis mil 
pessoas financiaram imóveis no mês passado pela Caixa Econômica Federal. Lançada hoje 
campanha para a inclusão de pessoas com deficiência. Pela primeira vez, mensagens vão 
trazer legendas e descrições em áudio para deficientes visuais. Ministério das Relações 
Exteriores cobra rigor nas investigações e na punição aos agressores da advogada 
brasileira na Suíça.#$$$#
'''

import os
import datetime

diretorio = '/Users/lflrocha/Desktop/conteudos/AVozDoBrasil/'

os.system('find ' + diretorio + ' -name .DS_Store -delete');
os.system('find ' + diretorio + ' -name ._* -delete');

dirList = [f for f in os.listdir(diretorio) if f.endswith('.mp3')]


fArq = open('/Users/lflrocha/Desktop/conteudos/t_voz_descricao.txt')
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


