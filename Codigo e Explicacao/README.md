# Explicação do Código - Automação de E-mails com Gmail API e Excel

Este documento fornece uma explicação detalhada de cada linha do código  que automatiza o envio de e-mails usando a API do Gmail e uma planilha do Excel USANDO Python.

## Importação de Bibliotecas

```python
import os
import base64
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
```

- `os`: Permite interagir com o sistema operacional, útil para verificar arquivos.
- `base64`: Necessário para codificar a mensagem de e-mail em um formato aceito pelo Gmail.
- `pandas`: Biblioteca para manipulação de dados, usada para ler a planilha de e-mails.
- `google.auth.transport.requests`, `google.oauth2.credentials`, `google_auth_oauthlib.flow`: Bibliotecas do Google para autenticação e autorização via OAuth 2.0.
- `googleapiclient.discovery`: Usada para construir o serviço do Gmail.
- `email.mime.text.MIMEText`: Permite criar a estrutura da mensagem de e-mail.

## Escopo da Autenticação

```python
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
```

Define o escopo de permissão necessário para enviar e-mails via API do Gmail.

## Função de Autenticação

```python
def autenticar_gmail():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds
```

- Verifica se o arquivo `token.json` existe e carrega as credenciais.
- Se o token estiver expirado, ele é atualizado.
- Caso contrário, inicia um novo fluxo de autenticação usando `credentials.json`.
- Salva o token de acesso para reutilização futura.

## Função para Enviar um E-mail

```python
def enviar_email(destinatario, assunto, mensagem):
    creds = autenticar_gmail()
    service = build("gmail", "v1", credentials=creds)

    msg = MIMEText(mensagem)
    msg["to"] = destinatario
    msg["subject"] = assunto
    msg = {"raw": base64.urlsafe_b64encode(msg.as_bytes()).decode()}

    service.users().messages().send(userId="me", body=msg).execute()
    print(f"E-mail enviado para {destinatario}")
```

- Obtém as credenciais autenticadas.
- Cria um serviço da API do Gmail.
- Constrói a mensagem de e-mail.
- Codifica a mensagem em base64 para o formato aceito pela API.
- Envia o e-mail e exibe uma confirmação.

## Função para Enviar E-mails a partir de um Arquivo Excel

```python
def enviar_emails_excel(arquivo_excel):
    try:
        df = pd.read_excel(arquivo_excel)

        if "Email" not in df.columns:
            print("Erro: A planilha deve conter uma coluna chamada 'Email'.")
            return

        for email in df["Email"].dropna():
            enviar_email(email, "Assunto Automático", "Este é um e-mail enviado via API do Gmail!")

    except Exception as e:
        print(f"Erro ao processar a planilha: {e}")
```

- Lê o arquivo Excel contendo os e-mails.
- Verifica se há uma coluna chamada `Email`.
- Itera sobre os e-mails válidos e os envia um por um.

## Execução do Programa

```python
enviar_emails_excel("emails.xlsx")
```

- Chama a função para enviar e-mails, utilizando os endereços presentes no arquivo `emails.xlsx`.
