#!/usr/bin/python
# -*- coding: UTF-8 -*-

#  0 "TRATAMENTO";
#  1 "NOME";
#  2 "CARGO";
#  3 "ENDEREÇO";
#  4 "BAIRRO";
#  5 "ROTA";
#  6 "CIDADE - UF";
#  7 "ÓRGÃO";
#  8 "ENDERECO FS";
#  9 "BAIRRO FS";
# 10 "ROTA FS";
# 11 "#"

import os
import datetime

import io

mes = "201502"

fout = open('../../RelatoriosMI/'+mes+'-PR.txt', 'w')
dirList=os.listdir('../../RelatoriosMI/'+mes)

dias = float(len(dirList))
print dias
orgaos = {}
end = {}

total = 0


for fname in dirList:
    print fname
    if fname <> '.DS_Store':
        farquivo = io.open('../../RelatoriosMI/'+mes+'/'+fname, 'r', encoding='utf16')
#        farquivo = io.open('../../RelatoriosMI/'+mes+'/'+fname, 'r', encoding='utf8')
        arquivo = farquivo.readlines()
        data_str = fname.split('.')[0]
        #print data_str
        data = datetime.date(int(data_str[4:8]), int(data_str[2:4]), int(data_str[0:2]))
        dia_semana = data.weekday()
        for linha in arquivo[1:]:
            #print data
            dados = linha.split('";"')
            if len(dados) <> 11:
                print data, len(dados), dados
            orgao = dados[7]
            #print orgao
            if orgao not in orgaos.keys():
                orgaos[orgao] = {}

            if int(dia_semana) not in [5,6]:
                # De segunda a sexta
                # Só inclui se tem endereço preenchido
                if dados[3] != "":
                    nome = dados[1]
                    endereco = dados[3]
                    nome_endereco = nome
                    print nome_endereco
                    if nome_endereco in orgaos[orgao].keys():
                        orgaos[orgao][nome_endereco] = orgaos[orgao][nome_endereco] + 1
                    else:
                        orgaos[orgao][nome_endereco] = 1
            else:
                # Sábado e domingo
                if dados[8] != "":
                    nome = dados[1]
                    endereco = dados[8]
                    nome_endereco = nome
                    print nome_endereco                    
                    if nome_endereco in orgaos[orgao].keys():
                        orgaos[orgao][nome_endereco] = orgaos[orgao][nome_endereco] + 1
                    else:
                        orgaos[orgao][nome_endereco] = 1

a = orgaos.keys()
a.sort()

for orgao in a:
    fout.write(orgao.encode('utf8') + '\n')
fout.write('\n')    

for orgao in a:
    nomes = orgaos[orgao].keys()
    nomes.sort()
    fout.write(orgao.encode('utf8') + '\n')
    soma = 0
    for nome in nomes:
        fout.write(' ' + '{:2}'.format(orgaos[orgao][nome]) + ': ' + nome.encode('utf8') +'\n')
        soma = soma + orgaos[orgao][nome]
    fout.write('Total de exemplares: ' + str(soma) + ' - Média por dia: ' +  "%.2f" % (soma/dias) +'\n')
    total = total + soma
    fout.write('\n')
    fout.write('\n')

fout.write('\n')
fout.write('Total de exemplares (MI Jornal) entregues no mês: '+ str(total) + ' - Média por dia: ' +  "%.2f" % (total/dias) +'\n')
    


