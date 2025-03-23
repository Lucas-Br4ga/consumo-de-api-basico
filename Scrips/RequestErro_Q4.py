import requests
import pandas as pd
from io import StringIO
r = requests.get("https://viacep.com.br/abc/")
if (r.status_code == 200):

    print(r)
    print("Json:", r.json())

else:
 print('Nao houve sucesso na requisicao.')
