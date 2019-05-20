#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import datetime
import urllib

'''
0 - 
1 - Ministério da Previdência Social
2 - 2009-09-18
3 - Previdência Complementar divulga resultado de concurso de monografia
4 - Sai na segunda-feira resultado de concurso de monografia
5 - http://192.168.20.154:8081/ebc-servicos/servicos/servico-de-radio/radiorelease/ministerio-da-previdencia-social/18-09-09-previdencia-complementar.mp3
6 - 

'''

diretorio = '/Users/lflrocha/Desktop/conteudos/Radiorelease/'

os.system('find ' + diretorio + ' -name .DS_Store -delete');
os.system('find ' + diretorio + ' -name ._* -delete');

fArq = open('/Users/lflrocha/Desktop/conteudos/materiasRadiorelease.txt')
descricoes = fArq.readlines()



for i, descricao in enumerate(descricoes):

	print i
	aux = descricao.split('###')


	ministerio = aux[1]
	data = aux[2]
	titulo = aux[3]
	descricao = aux[4]
	endereco = aux[5]

	filename = data + ' - ' + titulo
	filename = filename.replace('/','-')
	
	try:
		os.mkdir(diretorio+ministerio)
	except:
		pass

	dirTemp = diretorio + ministerio + '/'

	fTemp = open(dirTemp+filename+'.txt','w')
	fTemp.write(descricao)
	fTemp.close()
	
	urllib.urlretrieve (endereco, dirTemp+'/'+filename+'.mp3')

#	nomeArq = aux[1].replace('/','-')
#	texto = aux[3]

#	for n in dirList:
#		if nomeArq in n:
#			nomeArq = n.replace('.mp3','')

#	print nomeArq

#	fOut = open(diretorio+nomeArq+'.txt', 'w')
#	fOut.write(texto)
#	fOut.close()
