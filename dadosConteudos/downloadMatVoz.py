#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import datetime
import urllib



diretorio = '/Users/lflrocha/Desktop/conteudos/MateriasVoz/'

os.system('find ' + diretorio + ' -name .DS_Store -delete');
os.system('find ' + diretorio + ' -name ._* -delete');

dirList = [f for f in os.listdir(diretorio) if f.endswith('.mp3')]


fArq = open('/Users/lflrocha/Desktop/conteudos/materiasVoz.txt')
descricoes = fArq.readlines()

for i, descricao in enumerate(descricoes):

	print i
	aux = descricao.split('###')
	nome = aux[1].replace(":","-",1).replace("/","-")
	endereco = aux[2]
	urllib.urlretrieve (endereco, diretorio+nome+'.mp3')

#	nomeArq = aux[1].replace('/','-')
#	texto = aux[3]

#	for n in dirList:
#		if nomeArq in n:
#			nomeArq = n.replace('.mp3','')

#	print nomeArq

#	fOut = open(diretorio+nomeArq+'.txt', 'w')
#	fOut.write(texto)
#	fOut.close()
