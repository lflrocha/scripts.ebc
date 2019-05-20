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

dirListMP3 = [f for f in os.listdir(diretorio) if f.endswith('.mp3')]
dirListTXT = [f for f in os.listdir(diretorio) if f.endswith('.txt')]

mp3 = []
txt = []

for f in dirListMP3:
	mp3.append(f.replace('.mp3',''))
	
for g in dirListTXT:
	txt.append(g.replace('.txt',''))

d = set(mp3) - set(txt)
e = set(txt) - set(mp3)

print len(d), sorted(d), len(e), sorted(e)