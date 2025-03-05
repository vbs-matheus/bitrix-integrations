from findor_webhook.function import *

# Função principal, chamada pelo AWS Lambda para executar o código
def lambda_handler(event, context): 
    # Extraindo parâmetros do evento recebido
    campaign_name = event.get("campaign_name")
    username = event.get("username")
    user_identifier = event.get("user_identifier")
    user_email = event.get("user_email")
    DEAL_ID = event.get("DEAL_ID")
    Utm_Mkt = event.get("Utm_Mkt")
    user_segment = event.get("user_segment")

    # Chamando a função principal com os parâmetros
    response = POST_Findor(campaign_name, username, user_identifier, user_email, DEAL_ID, Utm_Mkt, user_segment)

    # Verificando se a resposta é válida
    if response:
        return {"statusCode": response.status_code, "body": response.text}
    else:
        return {"statusCode": 500, "body": json.dumps({"error": "Failed to make POST request"})}