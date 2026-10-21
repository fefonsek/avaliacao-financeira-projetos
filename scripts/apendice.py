"""Gera _apendice.qmd com a Tabela 2 do artigo em dois slides."""
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
d = pd.read_csv(RAIZ / "dados" / "tabela2.csv")
PROPOSTO = {10, 12, 28, 35, 45}


def br(x, casas=0):
    s = f"{x:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s.replace("-", "−")


def tabela(parte):
    linhas = ["<table class='grade apendice'>",
              "<tr><th>Grupo</th><th>Projeto</th><th>DI (R&#36;)</th><th>TMA (%)</th>"
              "<th>N</th><th>VPL (R&#36;)</th><th>IL (%)</th><th>MTIR (%)</th>"
              "<th>PBD (anos)</th><th>GA<sub>FT</sub> (%)</th></tr>"]
    for _, r in parte.iterrows():
        cls = " class='base'" if r.projeto in PROPOSTO else ""
        linhas.append(
            f"<tr{cls}><td>{r.grupo}</td><td>{r.projeto}</td><td>{br(r.di)}</td>"
            f"<td>{r.tma}</td><td>{r.n}</td><td>{br(r.vpl)}</td><td>{br(r.il, 2)}</td>"
            f"<td>{br(r.mtir, 2)}</td><td>{br(r.pbd, 2)}</td><td>{br(r.gaft, 2)}</td></tr>")
    linhas.append("</table>")
    return "\n".join(linhas)


saida = []
for i, (ini, fim) in enumerate([(0, 23), (23, 45)], start=1):
    saida.append(f"## Apêndice: Tabela 2 ({i}/2) {{.smaller .apendice-slide}}\n")
    saida.append(tabela(d.iloc[ini:fim]))
    saida.append("\n[Em verde, os 5 projetos escolhidos pelo modelo proposto. "
                 "Fonte: Abensur (2012), Tabela 2.]{.fonte}\n")
    saida.append("::: {.notes}\nSlide de apoio para as perguntas. "
                 "Não apresento, só uso se alguém pedir um projeto específico.\n:::\n")

(RAIZ / "_apendice.qmd").write_text("\n".join(saida), encoding="utf-8")
print("ok")
