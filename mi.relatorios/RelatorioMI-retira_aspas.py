#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os

fIn = open('../RelatoriosMI/201310/23102013.csv', 'r')
fOut = open('../RelatoriosMI/201310/23102013-2.csv', 'w')

arquivo = fIn.readlines()

for linha in arquivo[1:]:
    dados = linha.rsplit(',',1)
    dados[1] = dados[1].strip('\"')
    d = dados[0] + ",1\n"
    fOut.write(d)
    
fIn.close()
fOut.close()