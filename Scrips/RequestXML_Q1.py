import requests
url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):

    print("XML:", r.text)


else:
 print('Nao houve sucesso na requisicao.')
