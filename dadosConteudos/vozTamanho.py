#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime

from mutagen.mp3 import MP3


diretorio = u'/Users/lflrocha/Desktop/conteudos/AVozDoBrasil/'
diretorio = u'/Volumes/LFLR-HD05/_ConteudosEBC/AVozDoBrasil/Audio/'

os.system('find ' + diretorio + ' -name .DS_Store -delete');
os.system('find ' + diretorio + ' -name ._* -delete');

dirList = [f for f in os.listdir(diretorio) if f.endswith('.mp3')]


for arquivo in dirList:
	audio = MP3(diretorio+arquivo)
	duracao = "%u:%.2d" % (audio.info.length / 60, audio.info.length % 60)
	if (audio.info.length / 60) > 26:
		print arquivo, duracao
