import requests
import pandas as pd

url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEzMTk1LCJpYXQiOjE3NzM5MjExOTUsImp0aSI6ImU2ZGFhM2U5ZGEzMzQzNzJiMzAwMTNmNzNkMTVkNzczIiwidXNlcl9pZCI6IjExMCJ9.aNw1HPkLXRviOgrZmrX7eCp6ZSBv0M-gLcQ6XT3nz2c"
resp = requests.get(
    f"{url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={'data_base': '2026-03-23'},
)
dados = resp.json()
df = pd.DataFrame(dados)
maximo = df["roe"].max()
filtro = df["roe"]==maximo
df[filtro]


url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEzMTk1LCJpYXQiOjE3NzM5MjExOTUsImp0aSI6ImU2ZGFhM2U5ZGEzMzQzNzJiMzAwMTNmNzNkMTVkNzczIiwidXNlcl9pZCI6IjExMCJ9.aNw1HPkLXRviOgrZmrX7eCp6ZSBv0M-gLcQ6XT3nz2c"
params = = {"ticker": "ibov", "data_uni":"2025-03-21", }
