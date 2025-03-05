import json
import os
import requests
from env import *


def get_fields(method:str):

    if "crm." in method:
        url = f"{citopharma_url}{citopharma_token}{method}"
        payload = {}
        headers = {
            "Cookie": "qmb=0."
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response.encoding = "utf-8"
        return response.json()


def filter_fields_json(data):

    if data is not None:
        filtered_data = {
                key: value for key, value in data["result"].items() 
                if value.get("type") == "enumeration" or value.get("propertyType") == "L"
            }
        
        #Gerar Json para visualizar informações
        if os.path.exists("Company - 02/company_docs/filtered_fields.json"):
            os.remove("Company - 02/company_docs/filtered_fields.json")
        
        with open("Company - 02/company_docs/filtered_fields.json", "w", encoding="utf-8") as file:
            data = json.dump(filtered_data, file, indent=4, ensure_ascii=False)

        return filtered_data
    
    return None

def search_id(data, id_field=str, item_value=str):
    
    if id_field in data:
        if "values" in data[id_field]:
            for item in data[id_field].get("values", {}).values():
                if item.get("VALUE") == item_value:
                    return item["ID"]
        elif "items" in data[id_field]:
            for item in data[id_field].get("items", []):
                if item.get("VALUE") == item_value:
                    return item["ID"]
        
    return None



contact_data = get_fields("crm.contact.fields")
filtered_json = filter_fields_json(contact_data)
# id_search = search_id(filtered_json, "UF_CRM_651C5B773931F", "PF")
# print(id_search)

