import requests
url = 'https://viacep.com.br/ws'
uf = "mg"
localidade = "belo horizonte"
logradouro = 'rua dos aimores'
formato = 'json'
r = requests.get(f"{url}/{uf}/{localidade}/{logradouro}/{formato}/")
if (r.status_code == 200):

    print("Json:", r.json())

else:
 print('Nao houve sucesso na requisicao.')
