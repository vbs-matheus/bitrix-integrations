from rejected_transfers_notification.function import *

# Função principal, chamada pelo AWS Lambda para executar o código
def lambda_handler(event, context):
    # Extraindo parâmetros do evento recebido
    id_solicitacao = event.get("id_solicitacao")
    email_solicitante = event.get("email_solicitante")

    # Chamando a função principal com os parâmetros
    response = gerar_email(id_solicitacao, url_bitrix, email_solicitante)

    # Retornando a resposta
    return {"statusCode": response, "body": json.dumps(response.json())}