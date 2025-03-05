import requests
import json
from class_email import Mail
from env import url_bitrix, token_bitrix, email_login, dw_pass_login


def gerar_email(id_solicitacao, email_solicitante):
    # Consulta os cards rejeitados na solicitação de transferência e os motivos de rejeição

    url = f"{url_bitrix}/{token_bitrix}/crm.item.list"

    headers = {"Content-Type": "application/json", "Cookie": "qmb=0."}

    payload = json.dumps(
        {
            "entityTypeId": 168,
            "filter": {
                "ufCrm263IdSolicitacaoTransferencia": f"{id_solicitacao}",
                "stageId": "DT168_471:FAIL",
                "ufCrm263MotivoStatusTransf": [179629, 168697, 168683, 172325, 168687],
            },
        }
    )

    response_bitrix_buscar_informacoes = requests.request(
        "POST", url, headers=headers, data=payload
    ).json()

    # Extrair as cards que foram rejeitados na solicitação

    total = int(response_bitrix_buscar_informacoes.get("total"))

    if total != 0:
        items = response_bitrix_buscar_informacoes["result"]["items"]
        cards_rejeitados = [
            {
                "id": item["id"],
                "codigo_cliente": item.get("ufCrm263CodigoCliente", "não preenchido"),
                "motivo_rejeicao": item.get(
                    "ufCrm263MotivoStatusTransf", "N/A"
                ),
            }
            for item in items
        ]
    else:
        response_final = "Nenhum cliente rejeitado"
        return response_final

    # Ajustar o motivo de rejeição para um texto mais amigável
    def ajustar_motivo_rejeicao(motivo_rejeicao):
        motivo_ajustado = {
            168687: "Cliente não encontrado",
            179629: "Conta não faz mais parte da base do escritório",
            168697: "Sigla de assessor não encontrada",
            168683: "Código de Assessor Destino Inválido",
            172325: "Solicitação Duplicada"
        }
        return motivo_ajustado.get(motivo_rejeicao, "Não informado")

    # Ajustar o corpo do E-mail:
    corpo_email = ""
    for card in cards_rejeitados:
        id_card = card["id"]
        codigo_cliente = card["codigo_cliente"]
        motivo_ajustado = ajustar_motivo_rejeicao(card["motivo_rejeicao"])
        corpo_email = f'{corpo_email}<br><strong>• Código do Cliente:<a href="{url_bitrix}/crm/type/168/details/{id_card}/">{codigo_cliente}</a></strong> | <strong>Motivo da Recusa:</strong>{motivo_ajustado}</li>'

    # Conectar o E-mail:
    conexao = Mail(
    "smtp.office365.com",
    587,
    email_login,
    dw_pass_login,
    )

    # Enviar o E-mail:

    conexao.send(
    subject=f"Solicitação de Transferência nº{id_solicitacao}: Lista de Clientes Rejeitados",
	id_solicitacao=id_solicitacao,
	corpo_email=corpo_email,
    email=email_solicitante
    )
