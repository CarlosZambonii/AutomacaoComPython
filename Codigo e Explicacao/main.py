import os
import base64
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

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

def enviar_email(destinatario, assunto, mensagem):
    creds = autenticar_gmail()
    service = build("gmail", "v1", credentials=creds)

    msg = MIMEText(mensagem)
    msg["to"] = destinatario
    msg["subject"] = assunto
    msg = {"raw": base64.urlsafe_b64encode(msg.as_bytes()).decode()}

    service.users().messages().send(userId="me", body=msg).execute()
    print(f"E-mail enviado para {destinatario}")

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

enviar_emails_excel("emails.xlsx")
