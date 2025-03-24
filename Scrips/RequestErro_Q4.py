import requests
r = requests.get("https://viacep.com.br/abc/")
if (r.status_code == 200):

    print("Json:", r.json())

else:
 print(r)
 print('Nao houve sucesso na requisicao.')
