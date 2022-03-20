# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 21:24:27 2021

@author: ruran
"""

import requests
# import json
# from tkinter import *

def consulta():
    
    consulta = True
    
    while consulta == True:
        cnpj = str(input('Digite o CNPJ a ser consultado: '))
        
        info = requests.get('https://www.receitaws.com.br/v1/cnpj/' + cnpj)
        
        # print(info)
        
        info_cnpj = info.json()
        
        if info_cnpj['status'] != 'OK':
            print('Erro na consulta. Tente novamente.')
        
        else:
            lista = ['nome','natureza_juridica','abertura','situacao','logradouro',
                     'numero','bairro','municipio','uf','cep','telefone']
        
            x = 0
            for i in lista:
                nome = lista[x]
                print('{}:'.format(nome.capitalize().replace('_',' ')), info_cnpj[i])
                x += 1
        
            if str(info_cnpj["atividade_principal"][:]).find('84.') > -1:
                print('Entidade Governamental')
            
            if info_cnpj['natureza_juridica'][0:5] == '213-5':
                print('CNPJ é MEI')
            
            while True:
            
                novaconsulta = str(input('Deseja fazer uma nova consulta? [S/N] ').strip().upper())    
                
                if novaconsulta == 'S':
                    break
                
                elif novaconsulta == 'N':
                    consulta = False
                    break
                
                else:
                    print('Comando inválido')
                    continue

consulta()