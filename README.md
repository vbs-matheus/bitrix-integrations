# bitrix-integrations
Repositório de integrações criadas entre o CRM Bitrix24 e outras plataformas a partir de API. As integrações estão separadas por subpastas.

## Funcionalidades
* Conexão entre o crm Bitrix24 e outras plataformas.
* Utilização de webhooks
* Tratamento de dados dentro do CRM para rápida eficiência do projeto

## Ferramentas Utilizadas
### Python 3.10 ou superior
#### Biblitecas:
  (disponíveis no [requirements.txt](https://github.com/vbs-matheus/bitrix-integrations/blob/main/requirements.txt))
### Bitrix24
O Bitrix24 funciona como origem e destino dos dados a serem atulizados.
### Lambda Aws
Produto Amazon, o AWS Lambda é um serviço de computação sem servidor que permite executar código em resposta a eventos. Alguns dos projetos neste repositório ficam armazenados no Lambda e são iniciados através de ferramentas de integração, terceiras como o [Maker](https://www.make.com/en), ou por webhook configurado no próprio sistema do Lambda Aws.
## Pré-requisitos
Para os projetos com funções 'lambda_handler', ou seja, desenvolvidos para serem inseridos no AWS Lambda, é importante fazer a instalação do [requirements.txt](https://github.com/vbs-matheus/bitrix-integrations/blob/main/requirements.txt) na pasta correspondente do projeto, executando o código: 
  'pip install -r requirements.txt -t python_libs'
### Como funciona
Os códigos presentes nesse repositório foram desenvolvidos para esperar resposta de eventos no sistema do CRM e tem seus gatilhos iniciados via webhooks de ferramentas integradoras.
