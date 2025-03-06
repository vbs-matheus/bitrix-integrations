module.exports = async ({ logger, configVars }, stepResults) => {
  // JSON com os campos da entidade 'company' no Bitrix24
  const bitrixFields = stepResults.getCompanyFields;

  // Mapeamento de campos Protheus para Bitrix24
  const fieldMapping = {
    "TITLE": "razaosocial",
    "UF_CRM_1696269392": "cpfcnpj",
    "UF_CRM_672E133CBE1EA": "tipopessoa",
    "UF_CRM_1701868652": "estado",
    "UF_CRM_1701868652": "estadocobranca",
    "UF_CRM_1728307861": "recolheinss",
    "UF_CRM_1728307883": "recolhecofins",
    "UF_CRM_1728307902": "recolhecsll",
    "UF_CRM_1728307923": "recolhepis",
    "UF_CRM_1728308486": "recolheirrf",
    "UF_CRM_1701872892": "clienteempenho",
    "UF_CRM_1701872531": "venproibido",
    "UF_CRM_1728309045": "recolheiss"
}

  // Função para buscar o ID do campo no Bitrix com base no valor preenchido no Protheus
  const searchId = (data, idField, itemValue) => {
      if (data[idField]) {
          if (data[idField].items) {
              const item = data[idField].items.find(i => i.VALUE === itemValue);
              return item ? item.ID : null;
          } else if (data[idField].values) {
              const item = Object.values(data[idField].values).find(i => i.VALUE === itemValue);
              return item ? item.ID : null;
          }
      }
      return null;
  };

  // Dados dos clientes retornados pelo Protheus
  const clients = stepResults.listClients.results.items;

  // Prepara os clientes substituindo os valores pelos IDs esperados no Bitrix
  const preparedClients = clients.map(client => {
    const preparedClient = {};
    Object.entries(fieldMapping).forEach(([bitrixField, protheusField]) => {
      const value = client[protheusField];
      const id = searchId(bitrixFields, bitrixField, value);
      if (id !== null) {
        preparedClient[bitrixField] = id;
      } else {
        preparedClient[bitrixField] = value; // Mantém o valor original se não encontrar ID
      }
    });
    return preparedClient;
  });

  // Retorna os clientes preparados corretamente
  return {
    data: preparedClients
  };
};
