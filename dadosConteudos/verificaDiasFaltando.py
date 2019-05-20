#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime

diretorio = u'/Users/lflrocha/Desktop/conteudos/AVozDoBrasil/'
diretorio = u'/Volumes/LFLR-HD05/_ConteudosEBC/AVozDoBrasil/Audio'

feriados =  [ \
'2014-01-01', '2014-03-04', '2014-04-18', '2014-04-21', '2014-05-01', '2014-06-19', '2014-09-07', '2014-10-12', '2014-11-02', '2014-11-15', '2014-12-25', \
'2013-01-01', '2013-02-12', '2013-03-29', '2013-04-21', '2013-05-01', '2013-05-30', '2013-09-07', '2013-10-12', '2013-11-02', '2013-11-15', '2013-12-25', \
'2012-01-01', '2012-02-21', '2012-04-06', '2012-04-21', '2012-05-01', '2012-06-07', '2012-09-07', '2012-10-12', '2012-11-02', '2012-11-15', '2012-12-25', \
'2011-01-01', '2011-03-08', '2011-04-21', '2011-04-22', '2011-05-01', '2011-06-23', '2011-09-07', '2011-10-12', '2011-11-02', '2011-11-15', '2011-12-25', \
'2010-01-01', '2010-02-16', '2010-04-02', '2010-04-21', '2010-05-01', '2010-06-03', '2010-09-07', '2010-10-12', '2010-11-02', '2010-11-15', '2010-12-25', \
'2009-01-01', '2009-02-24', '2009-04-10', '2009-04-21', '2009-05-01', '2009-06-11', '2009-09-07', '2009-10-12', '2009-11-02', '2009-11-15', '2009-12-25', \
 ]

os.system('find ' + diretorio + ' -name .DS_Store -delete');
os.system('find ' + diretorio + ' -name ._* -delete');

dirList = [f for f in os.listdir(diretorio) if f.endswith('.mp3')]

datas = []

for arquivo in dirList:
	original = arquivo.replace(".mp3","")
	data = original.split("-")
	dia = data[2]
	mes = data[1]
	ano = data[0]
	alterado = ano+'-'+mes+'-'+dia
	datas.append(alterado)



data = datetime.date(2009,1,1)
hoje = datetime.date(2014,1,17)

while data <> hoje:
	dataStr = data.strftime("%Y-%m-%d")
	if (dataStr not in datas) and (data.weekday() not in [5,6]) and (dataStr not in feriados):
		print dataStr
	data = data + datetime.timedelta(days=1)