from serasa_integration.function import *

# Função principal que chama a função de consulta no AWS Lambda e gera o relatório via Serasa
def lambda_handler(event, context):
    # Extraindo parâmetros do evento recebido
    tipo_relatorio = event.get("tipo_relatorio")
    uf = event.get("uf")
    cpf = event.get("cpf")
    id_card = event.get("id_card")

    # # Validando se todos os parâmetros necessários estão presentes
    # if not all([tipo_relatorio, uf, cpf, id_card]):
    #     return {
    #         "statusCode": 400
    #     }

    # Chamando a função principal com os parâmetros
    response = consultar_relatorio(tipo_relatorio, uf, cpf, id_card)

    # Retornando a resposta
    return {"statusCode": 200, "body": json.dumps(response.json())}