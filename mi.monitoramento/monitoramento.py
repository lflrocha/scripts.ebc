#!/usr/bin/python
# -*- coding: UTF-8 -*-

from HTMLParser import HTMLParser
import urllib
import os
import hashlib

# veiculo
# titulo
# sutian
# reporter
# materia
# link



def gera_html():

    fin  = open('/Users/lflrocha/Desktop/noticias.txt',  'r')
    fout = open('/Users/lflrocha/Desktop/noticias.html', 'w')

    noticias = fin.readlines()
    secao = 0

    fout.write('<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8"></head><body>')
    
    for i in range(len(noticias)):
        linha = noticias[i]
        if "<noticia>" in linha:
            fout.write('<div style="text-align:justify">')
        elif "</noticia>" in linha:
            fout.write('</div><br><br>')
        elif "<veiculo>" in linha:
            fout.write('<span style="font-family:Times New Roman, Times, serif; font-size:18px; font-weight: bold;">')
        elif "</veiculo>" in linha:
            fout.write('</span><br>')
        elif "<titulo>" in linha:
            fout.write('<span style="font-family:Times New Roman, Times, serif; font-size:34px; font-weight: bold;">')
        elif "</titulo>" in linha:
            fout.write('</span>')
        elif "<sutian>" in linha:
            fout.write('<p style="font-family:Times New Roman, Times, serif; font-size:20px; font-style: italic;">')
        elif "</sutian>" in linha:
            fout.write('</p>')
        elif "<reporter>" in linha:
            fout.write('<p style="font-family:Times New Roman, Times, serif; font-size:20px; text-transform: uppercase;">')
        elif "</reporter>" in linha:
            fout.write('</p>')
        elif "<materia>" in linha:
            fout.write('<p style="font-family:Times New Roman, Times, serif; font-size:20px;">')
        elif "</materia>" in linha:
            fout.write('</p>')
        elif "<link>" in linha:
            fout.write('<p style="font-family:Times New Roman, Times, serif; font-size:20px; font-style: italic;">')
        elif "</link>" in linha:
            fout.write('</p>')
        else:
            if noticias[i+1].startswith('<'):
                fout.write(linha)
            else:
                fout.write(linha  + '<br>' )        

    fout.write('</body></html>')

def main():    
    gera_html()
    
if  __name__ =='__main__':main()
    