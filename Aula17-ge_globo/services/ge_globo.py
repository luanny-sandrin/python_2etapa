# Service GE — igual à Aula 16 (busca ao vivo no site).
# Aula 17 adiciona ge_persistencia.py para gravar cada sincronização no SQLite.

from __future__ import annotations

import re
from typing import TypedDict
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL_GE: str = "https://ge.globo.com/"
TIMEOUT: int = 15
USER_AGENT: str = "Mozilla/5.0 (compatible; TecTI-Aula17/1.0; +aula-educacional)"

REGEX_SUBSTRING: re.Pattern[str] = re.compile(r"sele[cç][aã]o", re.IGNORECASE)
REGEX_PALAVRA: re.Pattern[str] = re.compile(r"\bsele[cç][aã]o\b", re.IGNORECASE)


class Mencao(TypedDict):
    texto: str
    trecho: str
    url: str | None
    tag: str


class ResultadoBusca(TypedDict):
    fonte: str
    termo_busca: str
    modo_busca: str
    total: int
    mencoes: list[Mencao]


def _padrao_busca(modo: str) -> re.Pattern[str]:
    if modo == "palavra":
        return REGEX_PALAVRA
    return REGEX_SUBSTRING


def _trecho_com_destaque(
    texto: str,
    padrao: re.Pattern[str],
    janela: int = 60,
) -> str:
    match = padrao.search(texto)
    if not match:
        return texto[:120]
    inicio = max(0, match.start() - janela // 2)
    fim = min(len(texto), match.end() + janela // 2)
    trecho = texto[inicio:fim].strip()
    if inicio > 0:
        trecho = "…" + trecho
    if fim < len(texto):
        trecho = trecho + "…"
    return trecho


def buscar_mencoes_selecao(modo: str = "substring") -> ResultadoBusca:
    padrao: re.Pattern[str] = _padrao_busca(modo)

    try:
        resposta: requests.Response = requests.get(
            URL_GE,
            timeout=TIMEOUT,
            headers={"User-Agent": USER_AGENT},
        )
        resposta.raise_for_status()
    except requests.RequestException as erro:
        raise ConnectionError(f"Não foi possível acessar o GE: {erro}") from erro

    resposta.encoding = resposta.apparent_encoding or "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")

    vistos: set[tuple[str, str | None]] = set()
    mencoes: list[Mencao] = []

    for tag in soup.find_all(["a", "h1", "h2", "h3", "h4", "p", "span"]):
        texto = tag.get_text(" ", strip=True)
        if not texto or not padrao.search(texto):
            continue
        if len(texto) < 3:
            continue

        url: str | None = None
        if tag.name == "a" and tag.get("href"):
            url = urljoin(URL_GE, tag["href"])

        chave = (texto[:200], url)
        if chave in vistos:
            continue
        vistos.add(chave)

        mencoes.append(
            Mencao(
                texto=texto,
                trecho=_trecho_com_destaque(texto, padrao),
                url=url,
                tag=str(tag.name),
            )
        )

    return ResultadoBusca(
        fonte=URL_GE,
        termo_busca="seleção",
        modo_busca=modo,
        total=len(mencoes),
        mencoes=mencoes,
    )
