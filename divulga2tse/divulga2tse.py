#!/usr/bin/python
# -*- coding: latin-1 -*-

import json
import datetime
import urllib
import codecs
import requests
import os

import time
import subprocess


from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement



destino_local = "/Volumes/Leminski/Desktop/divulga2tse/distribuicao/"
destino_remoto = "/opt/arquivos/"


cidades = {
    "AN�POLIS - GO": "go/go92215-c0011-e000221-w",
    "ARACAJU - SE": "se/se31054-c0011-e000221-w",
    "BAURU - SP": "sp/sp62197-c0011-e000221-w",
    "BEL�M - PA": "pa/pa04278-c0011-e000221-w",
    "BELFORD ROXO - RJ": "rj/rj58041-c0011-e000221-w",
    "BELO HORIZONTE - MG": "mg/mg41238-c0011-e000221-w",
    "BLUMENAU - SC": "sc/sc80470-c0011-e000221-w",
    "CAMPO GRANDE - MS": "ms/ms90514-c0011-e000221-w",
    "CANOAS - RS": "rs/rs85898-c0011-e000221-w",
    "CARIACICA - ES": "es/es56251-c0011-e000221-w",
    "CARUARU - PE": "pe/pe23817-c0011-e000221-w",
    "CAUCAIA - CE": "ce/ce13730-c0011-e000221-w",
    "CAXIAS DO SUL - RS": "rs/rs85995-c0011-e000221-w",
    "CONTAGEM - MG": "mg/mg43710-c0011-e000221-w",
    "CUIAB� - MT": "mt/mt90670-c0011-e000221-w",
    "CURITIBA - PR": "pr/pr75353-c0011-e000221-w",
    "DIADEMA - SP": "sp/sp63770-c0011-e000221-w",
    "DUQUE DE CAXIAS - RJ": "rj/rj58335-c0011-e000221-w",
    "FLORIAN�POLIS - SC": "sc/sc81051-c0011-e000221-w",
    "FORTALEZA - CE": "ce/ce13897-c0011-e000221-w",
    "FRANCA - SP": "sp/sp64254-c0011-e000221-w",
    "GOI�NIA - GO": "go/go93734-c0011-e000221-w",
    "GUARUJ� - SP": "sp/sp64750-c0011-e000221-w",
    "GUARULHOS - SP": "sp/sp64777-c0011-e000221-w",
    "JABOAT�O DOS GUARARAPES - PE": "pe/pe24570-c0011-e000221-w",
    "JOINVILLE - SC": "sc/sc81795-c0011-e000221-w",
    "JUIZ DE FORA - MG": "mg/mg47333-c0011-e000221-w",
    "JUNDIA� - SP": "sp/sp66192-c0011-e000221-w",
    "MACAP� - AP": "ap/ap06050-c0011-e000221-w",
    "MACEI� - AL": "al/al27855-c0011-e000221-w",
    "MANAUS - AM": "am/am02550-c0011-e000221-w",
    "MARING� - PR": "pr/pr76910-c0011-e000221-w",
    "MAU� - SP": "sp/sp66893-c0011-e000221-w",
    "MONTES CLAROS - MG": "mg/mg48658-c0011-e000221-w",
    "NITER�I - RJ": "rj/rj58653-c0011-e000221-w",
    "NOVA IGUA�U - RJ": "rj/rj58696-c0011-e000221-w",
    "OLINDA - PE": "pe/pe24910-c0011-e000221-w",
    "OSASCO - SP": "sp/sp67890-c0011-e000221-w",
    "PETR�POLIS - RJ": "rj/rj58777-c0011-e000221-w",
    "PONTA GROSSA - PR": "pr/pr77771-c0011-e000221-w",
    "PORTO ALEGRE - RS": "rs/rs88013-c0011-e000221-w",
    "PORTO VELHO - RO": "ro/ro00035-c0011-e000221-w",
    "RECIFE - PE": "pe/pe25313-c0011-e000221-w",
    "RIBEIR�O PRETO - SP": "sp/sp69698-c0011-e000221-w",
    "RIO DE JANEIRO - RJ": "rj/rj60011-c0011-e000221-w",
    "SANTA MARIA - RS": "rs/rs88412-c0011-e000221-w",
    "SANTO ANDR� - SP": "sp/sp70572-c0011-e000221-w",
    "S�O BERNARDO DO CAMPO - SP": "sp/sp70750-c0011-e000221-w",
    "S�O GON�ALO - RJ": "rj/rj58971-c0011-e000221-w",
    "S�O LU�S - MA": "ma/ma09210-c0011-e000221-w",
    "SERRA - ES": "es/es56995-c0011-e000221-w",
    "SOROCABA - SP": "sp/sp71455-c0011-e000221-w",
    "SUZANO - SP": "sp/sp71510-c0011-e000221-w",
#    "TAUBAT� - SP": "sp/sp71838-c0011-e000221-w",
    "VILA VELHA - ES": "es/es57037-c0011-e000221-w",
    "VIT�RIA - ES": "es/es57053-c0011-e000221-w",
    "VIT�RIA DA CONQUISTA - BA": "ba/ba39659-c0011-e000221-w",
    "VOLTA REDONDA - RJ": "rj/rj59250-c0011-e000221-w",
}

#cidades = {
#    "SÃO PAULO - SP": "sp/sp71072-c0011-e000221-w",
#    "RIO DE JANEIRO - RJ": "rj/rj60011-c0011-e000221-w",
#}


def baixaDados(cidade):

    lista = []

    #Baixa arquivos do TSE
#    proxies = {"http" : "http://automator:!ebc!@@des@proxydf.ebc:3128"}
#    try:
#        f = urllib.urlopen('http://divulga.tse.jus.br/2016/divulgacao/oficial/220/dadosdivweb/'+cidade+'.js', proxies=proxies)
#    except:
#        erro = "Erro baixando os arquivos do TSE"

    r = requests.get('http://divulga.tse.jus.br/2016/divulgacao/oficial/221/dadosdivweb/'+cidade+'.js')
    if r.status_code == 200:
        parsed_json = r.json()

    resultado = {}
    resultado['codigoEleicao'] = parsed_json['ele'].encode('latin-1')
    resultado['cargoPergunta'] = parsed_json['carper']
    resultado['turno'] = parsed_json['t']
    resultado['fase'] = parsed_json['f']
    resultado['eleicaoSemAtribuicaoEleito'] = parsed_json['esae']
    resultado['motivoNaoAtribuicao'] = parsed_json['mnae']

    abrangencia = {}
    abrangencia['dataTotalizacao'] = parsed_json['dt']
    abrangencia['horaTotalizacao'] = parsed_json['ht']
    abrangencia['totalizacaoFinal'] = parsed_json['tf']
    abrangencia['tipoAbrangencia'] = parsed_json['tpabr']
    abrangencia['codigoAbrangencia'] = parsed_json['cdabr']
    abrangencia['secoesTotalizadas'] = parsed_json['st']
    abrangencia['secoesNaoTotalizadas'] = parsed_json['snt']
    abrangencia['eleitoradoApurado'] = parsed_json['ea']
    abrangencia['eleitoradoNaoApurado'] = parsed_json['ena']
    abrangencia['abstencao'] = parsed_json['a']
    abrangencia['comparecimento'] = parsed_json['c']
    abrangencia['votosTotalizados'] = parsed_json['tv']
    abrangencia['votosEmBranco'] = parsed_json['vb']
    abrangencia['votosNulos'] = parsed_json['vn']
    abrangencia['votosAnulados'] = parsed_json['van']
    abrangencia['votosPendentes'] = parsed_json['vp']
    abrangencia['votosValidos'] = parsed_json['vv']
    abrangencia['votosNominais'] = parsed_json['vnom']
    abrangencia['votosLegenda'] = parsed_json['vl']


    aux = []
    candidatos = parsed_json['cand']
    for candidato in candidatos:
        dt = {}
        dt['numeroCandidato'] = candidato['n']
        dt['totalVotos'] = candidato['v']
        dt['classificacao'] = candidato['seq']
        dt['eleito'] = candidato['e']
        aux.append(dt)

    return [resultado, abrangencia, aux]


def geraXml(cidade, dados):

    resultado = Element('Resultado')

    dadosResultado = dados[0]
    dadosAbrangencia = dados[1]
    dadosCandidatos = dados[2]

    for chave in dadosResultado.keys():
        resultado.set(chave, dadosResultado[chave])

    abrangencia = SubElement( resultado, 'Abrangencia' )
    for chave in dadosAbrangencia.keys():
        abrangencia.set(chave, dadosAbrangencia[chave])

    for cand in dadosCandidatos:
        votocandidato = SubElement( abrangencia, 'VotoCandidato' )
        for chave in cand.keys():
            votocandidato.set(chave, cand[chave])

    aux = cidade.split('/')
    arq = aux[1].replace('-w', '-v')


    output_file = codecs.open( destino_local + arq+'.xml', 'w', 'iso-8859-1' )

    aux = '<?xml version="1.0" encoding="ISO-8859-1"?>'
    output_file.write( aux )
    aux = ElementTree.tostring( resultado )
    output_file.write( aux )
    output_file.close()


def copiaServidor(cidade):
    aux = cidade.split('/')
    arq = aux[1].replace('-w', '-v')

    host = "jboss-prod01.ebc:" + destino_remoto
    args = ['scp', destino_local + arq + ".xml", host ]
    p = subprocess.Popen(args)


def main():

    start_time_tot = time.time()
    for cidade in cidades.keys():
        print "Executando cidade " + cidade
        dados = baixaDados(cidades[cidade])
        geraXml(cidades[cidade], dados)
        copiaServidor(cidades[cidade])

    print("TOTAL --- %s seconds ---" % (time.time() - start_time_tot))


if __name__ == "__main__":
    main()
