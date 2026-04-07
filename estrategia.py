import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE2Nzk2LCJpYXQiOjE3NzQ1MjQ3OTYsImp0aSI6IjFmZTg2MzE3NzU3MTRmNDY4Y2UyZWFmMTdkZmUxYWQ4IiwidXNlcl9pZCI6IjExMiJ9.MwFBcwADjVPl8mqIn06OT7cvU-Aao12HiWiQQkwCjYc"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2025-03-21"}
)

dados = resp.json()
df = pd.DataFrame(dados)
df2 = df[["ticker", "roe", "p_vp"]]
df2["rank_roe"] = df2["roe"].rank()
df2["rank_p_vp"] = df2["p_vp"].rank(ascending=True)
df2["rank_final"] = (df2["rank_roe"] + df2["rank_p_vp"]) / 2
df2.sort_values("rank_final", ascending=False)

