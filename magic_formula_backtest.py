# config.py

API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE2Nzk2LCJpYXQiOjE3NzQ1MjQ3OTYsImp0aSI6IjFmZTg2MzE3NzU3MTRmNDY4Y2UyZWFmMTdkZmUxYWQ4IiwidXNlcl9pZCI6IjExMiJ9.MwFBcwADjVPl8mqIn06OT7cvU-Aao12HiWiQQkwCjYc"
BASE_URL  = "https://laboratoriodefinancas.com/api/v2"

INICIO    = "2020-01-01"
FIM       = "2024-12-31"
TOP_N     = 20          # quantas ações entram no portfólio
CAPITAL   = 100_000     # capital inicial simulado em reais


# data.py

import requests
import pandas as pd
from config import API_TOKEN, BASE_URL

HEADERS = {"Authorization": f"Token {API_TOKEN}"}

def get_ibrx100() -> list[str]:
    """
    Retorna a lista de tickers do IBrX-100.
    O endpoint /carteiras retorna composições de índices.
    """
    url = f"{BASE_URL}/carteiras"
    params = {"indice": "ibrx100"}
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()          # levanta erro se status != 200
    dados = r.json()
    tickers = [item["ticker"] for item in dados]
    return tickers


def get_indicadores(ticker: str) -> pd.DataFrame:
    """
    Retorna série histórica de ROIC e Earning Yield para um ticker.
    Colunas esperadas: data, roic, earning_yield
    """
    url = f"{BASE_URL}/indicadores-fundamentalistas"
    params = {"ticker": ticker}
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    df["data"] = pd.to_datetime(df["data"])
    return df


def get_precos(ticker: str, inicio: str, fim: str) -> pd.DataFrame:
    """
    Retorna preços de fechamento ajustados para um ticker.
    Colunas esperadas: data, fechamento
    """
    url = f"{BASE_URL}/precos"
    params = {"ticker": ticker, "data_inicio": inicio, "data_fim": fim}
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    df = pd.DataFrame(r.json())
    df["data"] = pd.to_datetime(df["data"])
    df = df.sort_values("data").reset_index(drop=True)
    return df


