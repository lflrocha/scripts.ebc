#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime

diretorio = u'/Users/lflrocha/Desktop/conteudos/AVozDoBrasil/'

os.system('find ' + diretorio + ' -name .DS_Store -delete');
os.system('find ' + diretorio + ' -name ._* -delete');

dirList = [f for f in os.listdir(diretorio) if f.endswith('.mp3')]

for arquivo in dirList:
	original = arquivo.replace(".mp3","")
	data = original.split("-")
	dia = data[0]
	mes = data[1]
	ano = data[2]
	alterado = ano+'-'+mes+'-'+dia+'.mp3'
	os.rename(diretorio+arquivo, diretorio+alterado)
	
	