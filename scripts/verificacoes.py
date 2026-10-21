"""Reproduz as conferências do slide "Um olhar estatístico".

Todos os números saem da Tabela 2 de Abensur (2012), transcrita em
dados/tabela2.csv. O fator f1 = 1,4896226 aparece na Figura 1 do artigo.

Uso: python scripts/verificacoes.py
"""
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
d = pd.read_csv(RAIZ / "dados" / "tabela2.csv")

F1 = 1.4896226
PROPOSTO = [10, 12, 28, 35, 45]
SO_IL = [1, 4, 5, 10, 12, 19, 24, 28, 30, 35, 37, 43, 44, 45]
METAS = [1, 4, 6, 15, 25, 31, 36, 43, 44]

# 1. Conferência das Tabelas 3 e 5
for nome, proj in [("Proposto", PROPOSTO), ("Só IL", SO_IL), ("Metas", METAS)]:
    x = d[d.projeto.isin(proj)]
    print(f"{nome:9s} n={len(x):2d}  DI={x.di.sum():>9,.0f}  VPL={x.vpl.sum():>9,.0f}"
          f"  soma IL={x.il.sum():8.2f}  soma GA={x.gaft.sum():8.2f}  PBDmax={x.pbd.max()}")

# 2. Correlação entre rentabilidade e a medida de risco
print("\nCorrelação IL x GA_FT:", round(d.il.corr(d.gaft), 4))

# 3. A função objetivo vira uma nota por projeto
d["nota"] = F1 * d.il - d.pbd - d.gaft
d["viavel"] = (d.vpl > 0) & (d.pbd <= d.n) & (d.mtir > d.tma)
cand = d[d.viavel & (d.nota > 0)]
melhor = cand.loc[cand.groupby("grupo").nota.idxmax()]
# no grupo P os projetos são independentes: todos com nota positiva entram
escolha = pd.concat([melhor[melhor.grupo != "P"], cand[cand.grupo == "P"]])
print("\nProjetos viáveis com nota positiva (melhor de cada grupo):",
      sorted(escolha.projeto.astype(int).tolist()))
print("Carteira do artigo:", PROPOSTO)
print(escolha[["grupo", "projeto", "il", "pbd", "gaft", "nota"]].round(2).to_string(index=False))

# 4. Projetos que violam PBD <= vida útil
print("\nViolam a restrição de liquidez:", d[d.pbd > d.n].projeto.tolist())
