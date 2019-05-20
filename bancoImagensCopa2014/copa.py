#!/usr/bin/python
# -*- coding: UTF-8 -*-

from HTMLParser import HTMLParser
import urllib
import os
import hashlib


def limpa_lixos():
    os.system('find ' + diretorio + ' -name .DS_Store -delete')
    os.system('find ' + diretorio + ' -name ._* -delete')
    os.system('find ' + diretorio + ' -name __MACOSX -delete')


lista = {}
htmls =  u'/Users/lflrocha/Repositorios/copa/'
diretorio = u'/Users/lflrocha/Repositorios/copa/_preview/'

categorias = {
'BHZ_001': u'Inhotim (MG) - Arte Contemporanea',
'BHZ_002': u'Sabará (MG) - Cidade Histórica',
'BHZ_003': u'Igrejinha da Pampulha',
'BHZ_004': u'Lagoa da Pampulha',
'BHZ_005': u'Mercado Central',
'BHZ_006': u'Praça da Liberdade',
'BHZ_007': u'Parque Municipal',
'BHZ_008': u'Estádio do Mineirão',
'BHZ_009': u'Mirante',
'BHZ_010': u'Mobilidade Urbana',
'BSB_001': u'Aeroporto Presidente Juscelino Kubitschek',
'BSB_002': u'Esportes aquáticos',
'BSB_003': u'Esplanada dos Ministérios',
'BSB_004': u'Estádio Nacional Mané Garrincha',
'BSB_005': u'Parque Sarah Kubitschek (Parque da Cidade)',
'BSB_006': u'Placas FIFA',
'BSB_007': u'Ponte JK e Lago Paranoá',
'CBA_001': u'Chapada dos Guimarães',
'CBA_002': u'Arena Pantanal',
'CBA_003': u'Nobres (MT) - Gruta da Lagoa Azul',
'CBA_004': u'Pantanal',
'CBA_005': u'Praça Alencastro (Matriz)',
'CUR_001': u'Jardim Botânico',
'CUR_002': u'Praça XV de Novembro (Boca Maldita)',
'CUR_003': u'Mobilidade Urbana',
'CUR_004': u'Museu Oscar Niemeyer',
'CUR_005': u'Opera de Arame',
'CUR_006': u'Parque Tanguá',
'CUR_007': u'Aeroporto Internacional Afonso Pena',
'CUR_008': u'Antonina (PR)',
'CUR_009': u'Arena da Baixada',
'CUR_010': u'Trem da Serra do Mar',
'FTL_001': u'Pratos típicos da região ',
'FTL_002': u'Centro da cidade',
'FTL_003': u'Decoração para a Copa',
'FTL_004': u'Centro Dragão-do-mar de Arte e Cultura',
'FTL_005': u'Mercado Central',
'FTL_006': u'Praia de Iracema',
'FTL_007': u'Praia do Futuro',
'FTL_008': u'Paracuru (CE) - Parque Eólico de Paracuru',
'FTL_009': u'Imagens panorâmicas da cidade',
'FTL_010': u'Paracuru (CE)',
'FTL_011': u'Ponte dos Ingleses',
'FTL_012': u'Placas FIFA',
'MAN_001': u'Arena da Amazônia',
'MAN_002': u'Floresta amazônica',
'MAN_003': u'Mercado Municipal Adolfo Lisboa',
'MAN_004': u'Porto',
'MAN_005': u'Praça São Sebastião',
'MAN_006': u'Praia da Ponta Negra',
'MAN_007': u'Rio Negro e Ponte Rio Negro',
'MAN_008': u'Teatro Amazonas ',
'MAN_009': u'Imagens aéreas',
'MAN_010': u'Aeroporto Internacional Eduardo Gomes',
'NTL_001': u'Arena das Dunas',
'NTL_002': u'Centro Histórico',
'NTL_003': u'Dunas',
'NTL_004': u'Praia da Pipa',
'NTL_005': u'Praia da Ponta Negra',
'NTL_006': u'Maior cajueiro do mundo',
'NTL_007': u'Ponte Newton Navarro e Forte dos Reis Magos',
'PTA_001': u'Estádio Beira Rio',
'PTA_002': u'Parque da Redenção',
'PTA_003': u'Mercado Público',
'PTA_004': u'Usina do Gasômetro',
'PTA_005': u'Aeromóvel',
'PTA_006': u'Monumento aos Açorianos',
'PTA_007': u'Orla do rio Guaíba',
'PTA_008': u'Ponte do rio Guaíba',
'PTA_009': u'Praça Marechal Deodoro (Matriz)',
'PTA_010': u'Prefeitura Municipal',
'PTA_011': u'Viaduto Otávio Rocha',
'PTA_012': u'Gramado (RS) e Canela (RS)',
'RCF_001': u'Recife Antigo',
'RCF_002': u'Marco Zero',
'RCF_003': u'Igreja Nossa Senhora do Carmo',
'RCF_004': u'Oficina Brennand',
'RCF_005': u'Rua da Aurora',
'RCF_006': u'Artesanato',
'RCF_007': u'Teatro Santa Isabel',
'RCF_008': u'Praia do Pina',
'RCF_009': u'Praia da Boa Viagem',
'RCF_010': u'Pátio de São Pedro',
'RCF_011': u'Bairro Brasília Teimosa',
'RCF_012': u'Bonecos Gigantes de Olinda',
'RCF_013': u'Ponte Mauricio de Nassau',
'RCF_014': u'Decoração para a Copa',
'RIO_001': u'Estádio do Maracanã',
'RIO_002': u'Praias',
'RIO_003': u'Aeroporto Tom Jobim (Galeão)',
'RIO_004': u'Centro da cidade',
'RIO_005': u'Escadaria da Lapa',
'RIO_006': u'Feira de São Cristóvão',
'RIO_007': u'Parque Quinta da Boa Vista',
'RIO_008': u'Jardim Botânico',
'SAL_001': u'Praça da Liberdade',
'SAL_002': u'Acarajé (comida típica)',
'SAL_003': u'Farol de Santo Antônio (Farol da Barra)',
'SAL_004': u'Forte de São Marcelo',
'SAL_005': u'Mercado Modelo',
'SAL_006': u'Manancial Dique do Tororó',
'SAL_007': u'Igreja Nosso Senhor do Bonfim',
'SAL_008': u'Decoração para a Copa',
'SAL_009': u'Igreja e Convento de São Francisco',
'SAL_010': u'Bairro Stella Maris',
'SAL_011': u'Praia de Ondina',
'SAL_012': u'Praia de Itapuã',
'SAL_013': u'Bairro Rio Vermelho',
'SAL_014': u'Pelourinho',
'SAL_015': u'Praça Castro Alves',
'SAL_016': u'Ponta do Humaitá',
'SAL_017': u'Pessoas',
'SAL_018': u'Placas FIFA',
'SAO_001': u'Arena Corinthians',
'SAO_002': u'Imagens aéreas',
'SAO_003': u'Centro da Cidade',
'SAO_004': u'Avenida Paulista',
'SAO_005': u'Parque do Ibirapuera',
'SAO_006': u'Bairro da Liberdade',
'SAO_007': u'Museu do Ipiranga',
'SAO_008': u'Via Radial Leste',
'SAO_009': u'Estação da Luz',
'SAO_010': u'Ponte Estaiada',
'SAO_011': u'Grafite',
'TEMATICAS_001': u'Mobilidade Urbana',
'TEMATICAS_002': u'Pessoas',
'TEMATICAS_003': u'Placas FIFA',
'TEMATICAS_004': u'Ruas decoradas'
}

def incluiThumbs():
    
    strInicio = '<!--  ** CODIGO GERADO 1 ** -->\n'
    strFim = '<!--  ** FIM CODIGO GERADO 1 ** -->\n'
        
    dirList = os.listdir(diretorio)
    for subDir in dirList:

        print subDir
        subDiretorio = os.listdir(diretorio+subDir)
        aux = subDir.lower()

        f = open(htmls+aux+'.html', 'r+')
        linhas = f.readlines()
        f.close()
        
        inicio = linhas.index(strInicio)
        linInicio = linhas[:inicio + 1]

        fim = linhas.index(strFim)
        linFim = linhas[fim:]
    
        linMeio = []

        
        for subSub in subDiretorio:

            aux2 = subDir + '_' + subSub
            categ = categorias[aux2].encode("UTF-8")
            s = subSub.encode('utf-8')
        
            linMeio.append('<h3>'+ s + ' ' +  categ + '</h3>\n')
                
        
            arquivos = [f for f in os.listdir(diretorio+subDir+'/'+subSub) if f.endswith('.mp4')]

            linMeio.append('<div>\n')
            linMeio.append('<ul id="itemContainer'+subSub+'">\n')
            
            for arq in arquivos:
                   nome = arq.split('.')
                   aux3 = nome[0].split('_', 1)
                   ident = aux3[1]               
                   linMeio.append('<li>\n')
                   linMeio.append('<a href="#modal-'+ident+'"><img src="_preview/'+ subDir + '/' + subSub + '/' + nome[0] + '.jpg"/></a>\n')
                   linMeio.append('<a href="http://videoscopa2014.planalto.gov.br/'+ subDir + '/' + subSub + '/' + nome[0] +'.mp4"')
                   linMeio.append(''' onClick="ga('send', 'event', \''''+subDir+'''\', 'click', \''''+nome[0]+'''\')" ''')
                   linMeio.append('><img src="_images/botaodownload.png" alt="Download"/></a>\n')
                   linMeio.append('</li>\n')

            linMeio.append('</ul>\n')
            linMeio.append('<div class="holder" id="holder'+subSub+'"> </div>\n')
            linMeio.append('</div>\n')

        f = open(htmls+aux+'.html', 'w')
        linhas = linInicio + linMeio + linFim
        for aux in linhas:
            f.write(aux)
        f.close()
        


def incluiPopups():

    strInicio = '<!--  ** CODIGO GERADO 2 ** -->\n'
    strFim = '<!--  ** FIM CODIGO GERADO 2 ** -->\n'

    dirList = os.listdir(diretorio)
    for subDir in dirList:

        print subDir
        subDiretorio = os.listdir(diretorio+subDir)
        aux = subDir.lower()

        f = open(htmls+aux+'.html', 'r+')
        linhas = f.readlines()
        f.close()

        inicio = linhas.index(strInicio)
        linInicio = linhas[:inicio + 1]

        fim = linhas.index(strFim)
        linFim = linhas[fim:]

        linMeio = []

        for subSub in subDiretorio:

            aux2 = subDir + '_' + subSub
            categ = categorias[aux2].encode("UTF-8")
            s = subSub.encode('utf-8')

            arquivos = [f for f in os.listdir(diretorio+subDir+'/'+subSub) if f.endswith('.mp4')]

            for arq in arquivos:

                nome = arq.split('.')
                aux3 = nome[0].split('_', 1)
                ident = aux3[1]               
                
                linMeio.append('<div class="remodal" data-remodal-id="modal-' + ident + '">\n')
                linMeio.append('<div id="wrapperFancybox">\n')
                linMeio.append('<p class="tituloFancybox">' +subDir + '_' +  ident + '</p>\n')
                linMeio.append('<div class="video-container">\n')
                linMeio.append('<video src="_preview/'  + subDir + '/' + subSub + '/' + nome[0] + '.mp4" preload="none"  id="' + ident + '"></video>\n')
                linMeio.append('<script>$("#' + ident + '").mediaelementplayer({defaultVideoWidth: 640, defaultVideoHeight: 360,});</script>\n')
                linMeio.append('</div>\n')
#                linMeio.append('<p class="pFancybox">Lorem ipsum dolor sit amet, cosect adipisicing elit,sed do.</p>\n')
                linMeio.append('<a href="http://videoscopa2014.planalto.gov.br/'+ subDir + '/' + subSub + '/' + nome[0] +'.mp4"><img src="_images/botaodownload.png" alt="Download"/></a>\n')
                if subDir == 'BHZ':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Daniel Paranayba. Assistente de produção: Wesley Braga</p>')
                if subDir == 'BSB':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Márcio Andrade e Daniel Paranayba. Produtor Executivo: Thomas Freitas e Pedro Cardoso. Assistente de produção: Wesley Braga</p>')
                if subDir == 'CBA':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga </p>')
                if subDir == 'CUR':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga</p>')
                if subDir == 'FTL':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga </p>')
                if subDir == 'MAN':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga </p>')
                if subDir == 'NTL':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Thomas Freitas. Assistente de produção: Wesley Braga </p>')
                if subDir == 'PTA':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga</p>')
                if subDir == 'RCF':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga</p>')
                if subDir == 'RIO':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Márcio de Andrade. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga </p>')
                if subDir == 'SAL':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Márcio de Andrade. Produtor executivo: Thomas Freitas. Assistente de produção: Wesley Braga </p>')
                if subDir == 'SAO':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Daniel Paranayba. Produtor Executivo: Pedro Cardoso. Assistente de produção: Wesley Braga </p>')
                if subDir == 'TEMATICAS':
                    linMeio.append('<p class="creditos"><img src="_images/creditos.png" />Repórter cinematográfico: Daniel Paranayba e Márcio de Andrade. Produtor Executivo: Pedro Cardoso e Thomas Freitas. Assistente de produção: Wesley Braga</p>')
                linMeio.append('</div>\n')
                linMeio.append('</div>\n')

        f = open(htmls+aux+'.html', 'w')
        linhas = linInicio + linMeio + linFim
        for aux in linhas:
            f.write(aux)
        f.close()


def main():    
    limpa_lixos()
    incluiThumbs()    
    incluiPopups()
    
if  __name__ =='__main__':main()
    