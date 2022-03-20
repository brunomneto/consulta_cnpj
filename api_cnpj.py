
"""
Created on Sun Mar 20 15:50:54 2022
@author: brunomneto
"""

import requests

def consulta():
     
    while True:
        cnpj = str(input('\nDigite o CNPJ a ser consultado: '))
        
        info = requests.get('https://www.receitaws.com.br/v1/cnpj/' + cnpj)
        
        # print(info)
        
        info_cnpj = info.json()
        
        if info_cnpj['status'] != 'OK':
            print('Erro na consulta. Tente novamente.')
        
        else:
            lista = ['nome','natureza_juridica','abertura','situacao','logradouro',
                     'numero','bairro','municipio','uf','cep','telefone']
        
            x = 0
            print('\n' + '-' * 50)
            for i in lista:
                nome = lista[x]
                print('{}:'.format(nome.capitalize().replace('_',' ')), info_cnpj[i])
                x += 1
        
            if str(info_cnpj["atividade_principal"][:]).find('84.') > -1:
                print('Entidade Governamental')
            
            if info_cnpj['natureza_juridica'][0:5] == '213-5':
                print('CNPJ é MEI')
            
            novaconsulta = str(input('\nDeseja fazer uma nova consulta? [S/N] ').strip().upper())

            while novaconsulta not in 'SN':
                novaconsulta = str(input('Resposta inválida. Deseja fazer uma nova consulta? [S/N] - ')).strip().upper()

            if novaconsulta == 'S':
                continue
            
            else:
                break


consulta()
