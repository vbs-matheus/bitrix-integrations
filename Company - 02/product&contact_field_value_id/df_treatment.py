import pandas as pd

df = pd.read_excel('contact_fields_info.xlsx')
df['id_bitrix'] = df['id_bitrix'].str.replace(r'UfCrm', 'UF_CRM_', regex=True)

salvar_ajustes = df.to_excel('ajustado.xlsx', index=False)