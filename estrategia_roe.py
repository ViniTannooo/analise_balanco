import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE2Nzk2LCJpYXQiOjE3NzQ1MjQ3OTYsImp0aSI6IjFmZTg2MzE3NzU3MTRmNDY4Y2UyZWFmMTdkZmUxYWQ4IiwidXNlcl9pZCI6IjExMiJ9.MwFBcwADjVPl8mqIn06OT7cvU-Aao12HiWiQQkwCjYc"
params = {"ticker": "BBSE3", "data_ini": "2001-01-01", "data_fim": "2026-03-26"}

resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params
)

dados = resp.json()
df_preco = pd.DataFrame(dados)

filtro1 = df_preco["data"]=="2026-03-23"
preco_final = df_preco.loc[filtro1, "fechamento"].iloc[0]
preco_final = float(preco_final)



