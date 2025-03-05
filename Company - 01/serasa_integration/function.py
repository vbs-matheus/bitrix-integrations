from homologacao import GerarToken
import requests
import json
from datetime import datetime


def consultar_relatorio(tipo_relatorio, uf, cpf, id_card):
    # Gerar a Consultar Inicial no Serasa
    client = GerarToken()
    token_type, access_token = client.login()

    url = f"https://api.serasaexperian.com.br/credit-services/person-information-report/v1/creditreport?reportName={tipo_relatorio}&federalUnit={uf}&optionalFeatures=PARTICIPACAO_SOCIETARIA"

    headers_serasa = {
        "X-Document-id": f"{cpf}",
        "Content-Type": "application/json",
        "Authorization": f"{token_type} {access_token}",
    }

    response_serasa = requests.get(url, headers=headers_serasa).json()
    # return response_serasa
    # Extrair as anotações negativas do relatório

    negative_data = response_serasa["reports"][0].get("negativeData", {})

    # PEFIN_RESUMO

    pefin_summary = negative_data.get("pefin", {}).get("summary", {})
    qtd_pefin_resumo = str(pefin_summary.get("count", "N/D"))
    vlr_pefin_resumo = str(pefin_summary.get("balance", "N/D"))
    data_pefin_resumo = "ND"
    if "lastOccurrence" in pefin_summary:
        data_pefin_resumo = datetime.strptime(
            str(pefin_summary.get("lastOccurrence", "")), "%Y-%m-%d"
        ).strftime("%d/%m/%Y")

    # REFIN_RESUMO
    refin_summary = negative_data.get("refin", {}).get("summary", {})
    qtd_refin_resumo = str(refin_summary.get("count", ""))
    vlr_refin_resumo = str(refin_summary.get("balance", ""))
    data_refin_resumo = "ND"
    if "lastOccurrence" in refin_summary:
        data_refin_resumo = datetime.strptime(
            str(refin_summary.get("lastOccurrence", "")), "%Y-%m-%d"
        ).strftime("%d/%m/%Y")

    # PEFIN_COMPLETO
    pefin = negative_data.get("pefin", {}).get("pefinResponse", [])
    Pefin_Data = []
    Pefin_Modalidade = []
    Pefin_Valor = []
    Pefin_Origem = []

    for categoria in pefin:
        Pefin_Data.append(
            datetime.strptime(categoria.get("occurrenceDate", ""), "%Y-%m-%d").strftime(
                "%d/%m/%Y"
            )
            if categoria.get("occurrenceDate", "")
            else ""
        )
        Pefin_Modalidade.append(categoria.get("legalNature", "N/D"))
        Pefin_Valor.append(categoria.get("amount", "0"))
        Pefin_Origem.append(categoria.get("creditorName", "N/D"))

    # REFIN_COMPLETO
    refin = negative_data.get("refin", {}).get("refinResponse", [])
    Refin_Data = []
    Refin_Modalidade = []
    Refin_Valor = []
    Refin_Origem = []

    for categoria in refin:
        Refin_Data.append(
            datetime.strptime(categoria.get("occurrenceDate", ""), "%Y-%m-%d").strftime(
                "%d/%m/%Y"
            )
            if categoria.get("occurrenceDate", "")
            else ""
        )
        Refin_Modalidade.append(categoria.get("legalNature", ""))
        Refin_Valor.append(categoria.get("amount", "0"))
        Refin_Origem.append(categoria.get("creditorName", ""))

    # QUADRO SOCIETÁRIO

    quadro_societario = (
        response_serasa.get("optionalFeatures", {})
        .get("partner", {})
        .get("partnershipResponse", [])
    )

    if not quadro_societario:
        empresa_cnpj = ["N/D"]
        empresa_nome = ["N/D"]
        empresa_participacao = ["N/D"]
        empresa_status = ["N/D"]
        empresa_uf = ["N/D"]
        empresa_ultima_atualizacao = ["N/D"]
        empresa_anotacao_negativa = ["N/D"]
        iterar_empresa = "Não há registro de quadro societário"
    else:
        empresa_cnpj = []
        empresa_nome = []
        empresa_participacao = []
        empresa_status = []
        empresa_uf = []
        empresa_ultima_atualizacao = []
        empresa_anotacao_negativa = []
        iterar_empresa = ""

        for parceria in quadro_societario:
            empresa_cnpj.append(parceria.get("businessDocument", "N/P"))
            empresa_nome.append(parceria.get("companyName", "N/P"))
            empresa_status.append(parceria.get("companyStatus", "N/P"))
            empresa_participacao.append(
                f'{parceria.get("participationPercentage", "0%")}%'
            )
            empresa_uf.append(parceria.get("companyState", "N/P"))
            empresa_ultima_atualizacao.append(
                datetime.strptime(parceria.get("updateDate", ""), "%Y-%m-%d").strftime(
                    "%d/%m/%Y"
                )
                if parceria.get("updateDate", "")
                else ""
            )
            empresa_anotacao_negativa.append(
                "Sim" if parceria.get("hasNegative", False) else "Não"
            )
            iterar_empresa += (
                f"Razão Social: {parceria.get('companyName', 'N/P')},"
                f"CNPJ: {parceria.get('businessDocument', 'N/P')},"
                f"Status: {parceria.get('companyStatus', 'N/P')},"
                f"Porcentagem de participação: {parceria.get('participationPercentage', '0')}%,"
                f"UF: {parceria.get('participationPercentage', '0')}%,"
                # f"{datetime.strptime(parceria.get('updateDate', ''), '%Y-%m-%d').strftime('%d/%m/%Y') if parceria.get('updateDate', '') else ''},"
                f"Anotação Negativa: {'SIM' if parceria.get('hasNegative', False) else 'NÃO'}|"
            )

    # Atualizar card no Bitrix

    url = f"https://crm.hub-bnk.com/rest/1/6jzpwbnt07v17gi2/crm.item.update?entityTypeId=132&id={id_card}"

    payload = json.dumps(
        {
            "fields": {
                "ufCrm166ResumoPefinData": f"{data_pefin_resumo}",
                "ufCrm166ResumoPefinValor": f"{vlr_pefin_resumo}",
                "ufCrm166ResumoPefinQtd": f"{qtd_pefin_resumo}",
                "ufCrm166ResumoRefinData": f"{data_refin_resumo}",
                "ufCrm166ResumoRefinValor": f"{vlr_refin_resumo}",
                "ufCrm166ResumoRefinQtd": f"{qtd_refin_resumo}",
                "ufCrm166PefinData": Pefin_Data,
                "ufCrm166PefinModalidade": Pefin_Modalidade,
                "ufCrm166PefinValor": Pefin_Valor,
                "ufCrm166PefinOrigem": Pefin_Origem,
                "ufCrm166RefinData": Refin_Data,
                "ufCrm166RefinModalidade": Refin_Modalidade,
                "ufCrm166RefinValor": Refin_Valor,
                "ufCrm166RefinOrigem": Refin_Origem,
                "ufCrm166CnpjSerasaSocietario": empresa_cnpj,
                "ufCrm166NomesEmpresasSerasa": empresa_nome,
                "ufCrm166ParticipacaoEmpresasSerasa": empresa_participacao,
                "ufCrm166UfEmpresaSerasa": empresa_uf,
                "ufCrm166AnotacaoNegativaSerasa": empresa_anotacao_negativa,
                "ufCrm166UltimaAtualizacaoEmpresas": empresa_ultima_atualizacao,
                "ufCrm166StatusEmpresa": empresa_status,
                "ufCrm166IterarInformacoesEmpresa": iterar_empresa,
            }
        }
    )

    headers = {"Content-Type": "application/json", "Cookie": "qmb=0."}

    response_bitrix_atualizar_cards = requests.request(
        "POST", url, headers=headers, data=payload
    )

    # Puxa automação para criar o PDF:

    url = "https://crm.hub-bnk.com/rest/1/6jzpwbnt07v17gi2/bizproc.workflow.start"
    payload = json.dumps(
        {
            "TEMPLATE_ID": 7445,
            "DOCUMENT_ID": [
                "crm",
                "Bitrix\\Crm\\Integration\\BizProc\\Document\\Dynamic",
                f"DYNAMIC_132_{id_card}",
            ],
        }
    )

    response_bitrix_gerar_pdf = requests.request(
        "POST", url, headers=headers, data=payload
    )
    return response_bitrix_atualizar_cards, response_bitrix_gerar_pdf

