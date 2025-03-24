# 🌐 Biblioteca Requests Python - Exemplos de Utilização

## 📋 Índice

- [Requisição de CEP em formato XML](#requisição-de-cep-em-formato-xml)
- [Requisição em Loop para Múltiplos CEPs](#requisição-em-loop-para-múltiplos-ceps)
- [Busca de CEP por Endereço](#busca-de-cep-por-endereço)
- [Tratamento de Erros em Requisições](#tratamento-de-erros-em-requisições)
- [Salvando Resultado de Requisições em Arquivo](#salvando-resultado-de-requisições-em-arquivo)
- [Requisitos](#requisitos)
- [Como Executar](#como-executar)

## 🔍 Requisição de CEP em formato XML

**Arquivo:** `RequestXML_Q1.py`

Este script demonstra como realizar uma requisição simples para obter dados de um CEP específico em formato XML.

```python
import requests
url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):
    print("XML:", r.text)
else:
    print('Nao houve sucesso na requisicao.')
```

### ⚙️ Como funciona:
1. Importa a biblioteca requests
2. Define a URL base do serviço ViaCEP
3. Especifica o CEP que deseja consultar
4. Determina o formato de resposta (XML)
5. Executa a requisição GET concatenando os parâmetros
6. Verifica se a requisição foi bem-sucedida (código 200)
7. Exibe o conteúdo XML retornado pela API

### 📝 Exemplo de saída:
```xml
<xmlcep>
  <cep>30140071</cep>
  <logradouro>Rua dos Aimorés</logradouro>
  <complemento>até 699/700</complemento>
  <bairro>Funcionários</bairro>
  <localidade>Belo Horizonte</localidade>
  <uf>MG</uf>
  <ibge>3106200</ibge>
  <gia></gia>
  <ddd>31</ddd>
  <siafi>4123</siafi>
</xmlcep>
```

---

## 🔄 Requisição em Loop para Múltiplos CEPs

**Arquivo:** `LoopRequest_Q2.py`

Este script demonstra como realizar requisições para múltiplos CEPs utilizando um loop.

```python
import requests
url = 'https://viacep.com.br/ws/'
ceps = ["30140071", "30140072", "30140073", "30140074", "30140075"]
formato = '/json/'
for cep in ceps:
    r = requests.get(url + cep + formato)
    if (r.status_code == 200):
        print(f"Imprimindo as informações do CEP:{cep}")
        print()
        print('JSON : ', r.json())
        print()
    else:
        print('Nao houve sucesso na requisicao.')
```

### ⚙️ Como funciona:
1. Define uma lista com múltiplos CEPs para consulta
2. Para cada CEP na lista, executa uma requisição GET
3. Formata as informações retornadas em JSON
4. Exibe os dados de cada CEP de forma organizada

### 📊 Fluxo do processo:
```
Início ➡️ Percorre lista de CEPs ➡️ Faz requisição para cada CEP ➡️ Verifica sucesso ➡️ Exibe resultado ➡️ Fim
```

### 📝 Exemplo de saída parcial:
```json
Imprimindo as informações do CEP:30140071

JSON :  {'cep': '30140-071', 'logradouro': 'Rua dos Aimorés', 'complemento': 'até 699/700', 'bairro': 'Funcionários', 'localidade': 'Belo Horizonte', 'uf': 'MG', 'ibge': '3106200', 'gia': '', 'ddd': '31', 'siafi': '4123'}

Imprimindo as informações do CEP:30140072
...
```

---

## 🏙️ Busca de CEP por Endereço

**Arquivo:** `RequestRua_Q3.py`

Este script demonstra como realizar uma busca reversa, obtendo informações de CEP a partir de dados do endereço.

```python
import requests
import pandas as pd
from io import StringIO
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
```

### 🔍 Estrutura da URL:
```
https://viacep.com.br/ws/[UF]/[CIDADE]/[LOGRADOURO]/[FORMATO]/
```

### ⚙️ Como funciona:
1. Define os parâmetros de busca: UF, cidade e logradouro
2. Utiliza f-string para formatar a URL com todos os parâmetros
3. Executa a requisição GET para busca por endereço
4. Exibe os resultados em formato JSON

### 📝 Exemplo de saída:
```json
Json: [
  {
    "cep": "30140-070",
    "logradouro": "Rua dos Aimorés",
    "complemento": "até 699/700",
    "bairro": "Funcionários",
    "localidade": "Belo Horizonte",
    "uf": "MG",
    "ibge": "3106200",
    "gia": "",
    "ddd": "31",
    "siafi": "4123"
  },
  {
    "cep": "30140-071",
    "logradouro": "Rua dos Aimorés",
    "complemento": "até 699/700",
    "bairro": "Funcionários",
    "localidade": "Belo Horizonte",
    "uf": "MG",
    "ibge": "3106200",
    "gia": "",
    "ddd": "31",
    "siafi": "4123"
  }
]
```

---

## ⚠️ Tratamento de Erros em Requisições

**Arquivo:** `RequestErro_Q4.py`

Este script demonstra como lidar com erros em requisições HTTP, tentando acessar um endpoint inválido.

```python
import requests
import pandas as pd
from io import StringIO
r = requests.get("https://viacep.com.br/abc/")
if (r.status_code == 200):
    print(r)
    print("Json:", r.json())
else:
    print('Nao houve sucesso na requisicao.')
```

### 🚦 Códigos de Status HTTP Comuns:
```
200 - OK (Sucesso)
400 - Bad Request (Requisição inválida)
404 - Not Found (Não encontrado)
500 - Internal Server Error (Erro interno do servidor)
```

### ⚙️ Como funciona:
1. Tenta realizar uma requisição para um caminho inexistente ("/abc/")
2. Verifica o código de status HTTP da resposta
3. Como o caminho não existe, o código de status não será 200
4. Exibe a mensagem de erro quando a requisição falha

### 📝 Saída esperada:
```
Nao houve sucesso na requisicao.
```

---

## 💾 Salvando Resultado de Requisições em Arquivo

**Arquivo:** `RequestWrite_Q5.py`

Este script demonstra como salvar o resultado de uma requisição HTTP em um arquivo de texto.

```python
import requests
r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})
document = open("../FileWrite/Write_Q5.txt","w")
if (r.status_code == 200):
    print("Success")
    document.write(r.text)
else:
    print('Nao houve sucesso na requisicao.')
```

### 📋 Processo de Escrita em Arquivo:
```
1. Realiza requisição HTTP ➡️ 2. Verifica sucesso ➡️ 3. Abre arquivo para escrita ➡️ 4. Escreve resposta no arquivo
```

### ⚙️ Como funciona:
1. Realiza uma busca no Google pelo termo "elson de abreu"
2. Abre um arquivo de texto para escrita
3. Se a requisição for bem-sucedida, salva o conteúdo HTML da página no arquivo
4. Exibe uma mensagem de sucesso após salvar o conteúdo

---

## 📋 Requisitos

Para executar estes scripts, você precisará ter:

- Python 3.6 ou superior
- Biblioteca Requests (`pip install requests`)
- Biblioteca Pandas (para alguns exemplos - `pip install pandas`)

## 🚀 Como Executar

1. Clone este repositório
2. Instale as dependências:
   ```bash
   pip install requests pandas
   ```
3. Execute o script desejado:
   ```bash
   python Scrips/RequestXML_Q1.py
   ```
   
---

### 📝 Notas Importantes

- Certifique-se de ter conexão com a internet para que as requisições funcionem corretamente
- A API ViaCEP utilizada nos exemplos é gratuita e de uso público
- Crie a pasta `FileWrite` no diretório pai se for executar o script `RequestWrite_Q5.py`

---

## 📊 Tabela Comparativa dos Scripts

| Script | Funcionalidade | Formato | Particularidade |
|--------|----------------|---------|-----------------|
| RequestXML_Q1.py | Consulta CEP único | XML | Retorna dados em XML |
| LoopRequest_Q2.py | Consulta múltiplos CEPs | JSON | Usa loop para processar lista |
| RequestRua_Q3.py | Busca por endereço | JSON | Busca reversa (endereço → CEP) |
| RequestErro_Q4.py | Tratamento de erros | JSON | Demonstra falha proposital |
| RequestWrite_Q5.py | Salvar em arquivo | HTML | Armazena resposta em arquivo |

---

## 🔄 Diagrama do Fluxo de Requisições

```
┌────────────┐     ┌─────────────┐     ┌────────────┐     ┌──────────────┐
│  Parâmetros │────▶│  Requisição  │────▶│  Verificação │────▶│  Processamento │
└────────────┘     └─────────────┘     │   de Status  │     └──────────────┘
                                       └────────────┘
                                             │
                                             ▼
                                    ┌─────────────────┐
                                    │    Tratamento    │
                                    │     de Erro      │
                                    └─────────────────┘
```
