# 📧 Automação de Envio de E-mails com Python e API do Gmail  

Este projeto foi desenvolvido como parte de uma **Iniciação Científica** na **UFSCar**, com o objetivo de **auxiliar e agilizar o processo de envio de e-mails**. Ele permite enviar e-mails individuais, em massa a partir de uma planilha Excel ou CSV.
📌 **Desenvolvido por**: [Carlos Eduardo Zamboni da Luz](https://www.linkedin.com/in/carlos-zamboni-546086266/)  
📌 **Repositório GitHub**: [AutomacaoPython](https://github.com/CarlosZambonii/AutomacaoPython.git)  

---

## 🚀 Tecnologias Utilizadas  

- **Python 3.x** 🐍  
- `google-auth`, `google-auth-oauthlib`, `googleapiclient` (Integração com API do Gmail)  
- `pandas`, `openpyxl` (Bibliotecas Python para leitura e manipulação de arquivos Excel)  
- `email.mime` (Criação e envio de e-mails formatados)  

---

## 🔑 Configuração da API do Gmail no **Google Cloud Console**  

Para utilizar a API do Gmail, siga estes passos:  

### **1️⃣ Criando um projeto no Google Cloud Console**  
1. Acesse o **[Google Cloud Console](https://console.cloud.google.com/)** e faça login com sua conta do Google.  
2. No topo da página, clique em **Selecionar um projeto** → **Novo projeto**.  
3. Dê um nome ao projeto (exemplo: `AutomacaoPython`) e clique em **Criar**.  

### **2️⃣ Habilitando a API do Gmail**  
1. No menu lateral, vá para **APIs e Serviços** → **Biblioteca**.  
2. Pesquise por **Gmail API** e clique em **Ativar**.  

### **3️⃣ Criando credenciais OAuth 2.0**  
1. Vá para **APIs e Serviços** → **Credenciais**.  
2. Clique em **Criar credenciais** → **ID do Cliente OAuth**.  
3. Se solicitado, configure a **Tela de Consentimento OAuth**:  
   - Escolha **Externo** se quiser testar com outras contas de e-mail.  
   - Preencha as informações e clique em **Salvar e Continuar**.  
4. Escolha o tipo de aplicativo: **Aplicativo de Área de Trabalho**.  
5. Clique em **Criar** e faça o download do arquivo **`credentials.json`**.  
6. Mova o arquivo `credentials.json` para a pasta do seu projeto.  

### **4️⃣ Primeira Autenticação**  
Ao rodar o script pela primeira vez, uma janela será aberta para autorizar a conta do Google. Após a autenticação, um arquivo `token.json` será gerado automaticamente para armazenar o acesso.  

---

## 📂 Estrutura do Projeto  

```
📂 AutomacaoComPython
│── 📄 main.py           # Código principal
│── 📄 requirements.txt  # Dependências do projeto
│── 📄 README.md         # Documentação do projeto
│── 📄 credentials.json  # Credenciais da API do Gmail 
│── 📄 token.json        # Token de autenticação
│── 📄 emails.xlsx       # Planilha com e-mails
```

---

## 📝 Licença  

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.  

📌 **Desenvolvido por**: [Carlos Eduardo Zamboni da Luz](https://www.linkedin.com/in/carlos-zamboni-546086266/)  
📌 **Repositório GitHub**: [AutomacaoComPython](https://github.com/CarlosZambonii/AutomacaoComPython)  
