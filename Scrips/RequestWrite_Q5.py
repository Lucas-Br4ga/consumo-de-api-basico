import requests
r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})
document = open("../FileWrite/Write_Q5.txt","w")
if (r.status_code == 200):
 print("Success")
 document.write(r.text)
else:
 print('Nao houve sucesso na requisicao.')
