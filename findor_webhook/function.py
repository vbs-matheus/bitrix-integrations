import requests
import json
from env import url_findor, company_identifier

# Função para fazer uma requisição POST para a API do Findor
def POST_Findor(campaign_name, username, user_identifier, user_email, DEAL_ID, Utm_Mkt, user_segment):
    # Montando o payload da requisição
    payload = json.dumps({
        "company_identifier": company_identifier,
        "campaign_name": campaign_name,
        "username": username,
        "user_identifier": user_identifier,
        "user_email": user_email,
        "DEAL_ID": DEAL_ID,
        "Utm_Mkt": Utm_Mkt,
        "user_segment": user_segment
    })

    headers = {
        'Content-Type': 'application/json'
    }
    # Fazendo tentativa de requisição POST para a API do Findor e tratando possíveis erros de conexão ou HTTP
    try:
        response = requests.post(url_findor, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None
    