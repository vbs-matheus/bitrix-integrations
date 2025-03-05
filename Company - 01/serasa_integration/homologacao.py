import requests
from env import token_serasa 

class GerarToken:
    def __init__(self):
        self.url = "https://api.serasaexperian.com.br/security/iam/v1/client-identities/login"

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": token_serasa,
            "Cookie": "visid_incap_1333078=ccOmza5KS9ie2kim2aJYzMroF2cAAAAAQUIPAAAAAABmWeIMAfGTDvQZS9uatSHO",
        }

        self.payload = ""

    def login(self):
        response = requests.post(self.url, headers=self.headers, data=self.payload)
        homologacao = response.json()
        token_type = homologacao.get("tokenType")
        access_token = homologacao.get("accessToken")
        return token_type, access_token

