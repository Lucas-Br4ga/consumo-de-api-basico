import requests
r = requests.get("https://viacep.com.br/abc/")
if (r.status_code == 200):

    print(r)
    print("Json:", r.json())

else:
 print('Nao houve sucesso na requisicao.')
